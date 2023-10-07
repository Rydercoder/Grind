class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        carry = 1  # Initialize the carry to 1
        
        # Iterate through the digits from right to left
        for i in range(n - 1, -1, -1):
            if carry == 0:
                break  # No need to continue if there's no carry
                
            current_sum = digits[i] + carry  # Add the carry to the current digit
            carry = current_sum // 10  # Update the carry for the next iteration
            digits[i] = current_sum % 10  # Update the current digit
        
        # If there is still a carry after the loop (e.g., when incrementing 9), insert it as a new most significant digit
        if carry > 0:
            digits.insert(0, carry)
        
        return digits
                    