CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select
        salary
      from (
        select
            salary,
            ROW_NUMBER() over (order by salary desc) as salary_rank
        from (
            select distinct salary
            from Employee
            order by salary
        ) t1
      ) t2
      where salary_rank=N
  );
END