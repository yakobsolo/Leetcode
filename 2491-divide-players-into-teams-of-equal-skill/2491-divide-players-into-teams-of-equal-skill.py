class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        creativty = 0
        i = 0
        j = len(skill)-1
        temp = skill[i] + skill[j]
        creativty += skill[i] * skill[j]

        i, j = i + 1, j-1
        while i<j:
            cur = skill[i] + skill[j]
            if cur == temp:
                creativty += skill[i] * skill[j]
            else:
                return -1
            i+=1
            j-=1
            
        return creativty
            
            