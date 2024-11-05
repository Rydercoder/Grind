class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0 as per problem definition
        if not needle:
            return 0
        
        # Get lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Iterate through haystack to find the first occurrence of needle
        for i in range(haystack_len - needle_len + 1):
            # Check if substring of haystack matches needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1

    