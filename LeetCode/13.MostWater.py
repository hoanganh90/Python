class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        maxArea = []
        while(True):
            maxElement = 0
            for j in range(i+1, len(height)):
                area = (j-i) * min([height[i], height[j]])
                if area > maxElement:
                    maxElement = area
            maxArea.append(maxElement)
            i +=1
            if i == len(height):
                break
        return max(maxArea)
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))