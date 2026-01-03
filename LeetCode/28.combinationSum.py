class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        i = 0
        result = []
        while i < len(candidates):
            extra = target % candidates[i] 
            n = target // candidates[i]
            if extra == 0:
                temp_result = []
                for k in range(target // candidates[i]):
                    temp_result.append(candidates[i])
                result.append(temp_result)
            else:
                temp_result = []
                temp_sum = 0
                j = 0
                while( j < n):
                    temp_result.append(candidates[i])
                    temp_sum += candidates[i]
                    if temp_sum > target:
                        break
                    extra = target % temp_sum
                    try:
                        found_index = candidates[i + 1:].index(extra)
                        temp_sum += extra
                        temp_result.append(extra)
                        if temp_sum == target:
                            result.append(temp_result)
                            break
                    except ValueError:
                        j += 1
            i += 1
        return result
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res

        return make_combination(0, [], 0)
s = Solution()
print(s.combinationSum2([2,3,5], 8))
        

            