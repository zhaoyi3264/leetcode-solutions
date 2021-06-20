class Solution:
    def decodeString(self, s: str) -> str:
        strings = []
        nums = []
        ans = ''
        num = ''
        
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                nums.append(int(num))
                num = ''
                strings.append(ans)
                ans = ''
            elif c == ']':
                pop = strings.pop()
                rep = nums.pop()
                ans = pop + ans * rep
            else:
                ans += c
        return ans
