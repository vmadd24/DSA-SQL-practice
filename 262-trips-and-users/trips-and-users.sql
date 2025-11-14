# Write your MySQL query statement below
with
    trips_users_temp as (
        select
            t1.client_id,
            t1.driver_id,
            t1.city_id,
            t1.status,
            t1.request_at,
            t2.banned as client_banned
        from trips t1 inner join users t2
            on t1.client_id = t2.users_id
    ),

    trips_users as (
        select
            t1.client_id,
            t1.driver_id,
            t1.city_id,
            t1.status,
            t1.request_at,
            t1.client_banned,
            t2.banned as driver_banned
        from trips_users_temp t1 inner join users t2
            on t1.driver_id = t2.users_id
    ),

    output_temp as (
        select
            request_at,
            sum(
                case
                    when not (status = 'completed') and client_banned = 'No' and driver_banned = 'No'  then 1
                    else 0
                end
            ) as cancelled_count,
            sum(
                case
                    when status = 'completed' and client_banned = 'No' and driver_banned = 'No' then 1
                    else 0
                end
            ) as complete_count
        from trips_users
        group by request_at
        having request_at between "2013-10-01" and "2013-10-03" and (complete_count > 0 or cancelled_count > 0)
    ),

    output as (
        select
            request_at as Day,
            round((cancelled_count*1.0)/(cancelled_count+complete_count), 2) as `Cancellation Rate`
        from output_temp
    )
    

select * from output;