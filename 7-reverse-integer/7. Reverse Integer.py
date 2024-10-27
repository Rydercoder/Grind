class Solution:
    def reverse(self, x: int) -> int:
        
        min, max = -2**31, 2**31 - 1

        if x < 0:
            sign = -1
        else: 
            sign = 1
        reversed_x = int(str(abs(x))[::-1])

        result = sign * reversed_x

        if result < min or result > max:
            return 0
        return result
        