class Solution:
    def createMap(self, str):
        str_dict = {}
        for x in str:
            str_dict[x] = str_dict.get(x,0) + 1
        return { k: v for k,v in sorted(str_dict.items(), key= lambda item: item[0]) }
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        temp_strs = strs.copy()
        i, j = 0, 0
        while True:
            new_item = temp_strs.pop(i)
            temp_result = [new_item]
            for j in range(0, len(temp_strs)):
                if self.createMap(new_item) == self.createMap(temp_strs[j]):
                   temp_result.append(temp_strs[j])
                   temp_strs.pop(j)
            result.append(temp_result)
            if len(temp_strs) <= 0:
                break
        return result
s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
