class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        stack = []
        
        for n in s:
            stack.append(n)
        i=0
        while stack:
            s[i] = stack.pop()
            i = i + 1
        """
        l, r = 0, len(s)-1
        
        while l<r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1