class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            i = str(i)
            if '3' in i or '4' in i or '7' in i:
                continue
            elif '2' in i or '5' in i or '6' in i or '9' in i:
                count += 1
        return count
