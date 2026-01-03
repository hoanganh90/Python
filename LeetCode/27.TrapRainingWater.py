class Solution:
    def calculateWater(self, mini_height: list[int]) -> int:
        top = min(mini_height[0], mini_height[len(mini_height) - 1])
        sum = 0
        for i in range(1, len(mini_height) - 1):
            sum += abs(top - mini_height[i])
        return sum
    def trap(self, height: list[int]) -> int:
        first_border = height[0]
        second_border = 0
        i = 0
        j = 0
        result = 0
        while i < len(height):
            if height[i] > 0:
                found_container = True
                first_border = i
                j = i + 1
                while True:
                    if height[j] >= height[i]:
                        found_container = False
                        second_border = j
                        break
                    else:
                        j += 1
                    if j >= len(height):
                        break
                result += self.calculateWater(height[first_border:second_border + 1])
                i = second_border
            else:
                i += 1
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
                    
