class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        count = 0
        for i in range(n):
            en, ex = energy[i], experience[i]
            if initialEnergy<=en:
                count += en-initialEnergy+1
                initialEnergy = 1
            else:
                initialEnergy -= en
            if initialExperience<=ex:
                count += ex-initialExperience+1
                initialExperience = (2 * ex)+1
            else:
                initialExperience += ex
        return count
                