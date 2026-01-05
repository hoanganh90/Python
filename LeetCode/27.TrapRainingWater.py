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
        while i < len(height)-2:
            found_container = False
            if height[i] > 0 and i < len(height):
                found_container = True
                first_border = i
                t = i + 1
                j = i + 2
                while True:
                    if height[j] > height[t] and height[j] >= height[i]:
                        found_container = True
                        second_border = j
                        break
                    else:
                        t += 1
                        j += 1
                        found_container = False
                    if j >= len(height):
                        break
                if found_container == True:
                    result += self.calculateWater(height[first_border:second_border + 1])
                    i = second_border
                else:
                    i += 1
            else:
                i += 1
        return result
    def trap2(self, height: list[int]) -> int:
        i = 0
        result = 0
        if len(height) < 3:
            return 0
        elif len(height) == 3:
            if height[1] < height[0] and height[1] < height[2]:
                return self.calculateWater(height)
            else:
                return 0
        while i < len(height) - 2:
            tmp_i = i
            if height[i] > 0:
                while True:
                    x = tmp_i
                    y = tmp_i + 1
                    z = tmp_i + 2
                    
                    if height[y] > height[x] and height[y] > height[z] and height[y] >= height[i]:
                        result += self.calculateWater(height[i:y + 1])
                        i = y
                        break
                    else:
                        tmp_i +=1
                    if tmp_i >= len(height) -2:
                        break
            else:
                i += 1
                
s = Solution()
print(s.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
                    
