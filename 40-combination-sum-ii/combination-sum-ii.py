class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        path = []


        def backtrack(i: int, sum: int):

            if sum == target:
                res.append(path.copy())
            
            start_idx = i

            for elem in candidates[start_idx:]:

                new_sum = sum + elem

                if new_sum > target or (i>0 and i-1>=start_idx and candidates[i]==candidates[i-1]):
                    i += 1
                    continue
                
                path.append(elem)
                backtrack(i+1, new_sum)
                path.pop()

                i += 1
            
        
        backtrack(0, 0)
        return res
