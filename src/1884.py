class Solution:
    def twoEggDrop(self, n: int) -> int:
        a = 1
        b = 1
        c = - 2 * n
    
        x = (-b + (b * b - 4 * a * c)**0.5) / 2.0
        
        return math.ceil(x)

