class Solution:
    def numTeams(self, rating: List[int]) -> int:
        asc = dsc = 0
        for i, v in enumerate(rating):
            llt = lgt = rlt = rgt = 0
            for l in rating[:i]:
                if l < v:
                    llt += 1
                elif l > v:
                    lgt += 1
            for r in rating[i+1:]:
                if r < v:
                    rlt += 1
                elif r > v:
                    rgt += 1
            asc += llt * rgt
            dsc += lgt * rlt
        return asc + dsc
