class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hig_alt = 0
        gains = 0
        for i in range(len(gain)):
            gains += gain[i]
            if gains > hig_alt:
                hig_alt = gains
        return hig_alt
                
            