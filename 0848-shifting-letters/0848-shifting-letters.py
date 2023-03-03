class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift_leng = len(shifts)
        s = list(s)
        prefix = [shifts[0]%26]
        alphabets = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        total= sum(shifts)%26
        for i in range(1, shift_leng):
            prefix.append((shifts[i]+prefix[-1])%26)
            
        zro = ord(s[0]) - ord('a')
        s[0] = alphabets[(total)+zro]
        for i in range(1, shift_leng):
            index = ord(s[i]) - ord('a')
            s[i] = alphabets[(total-prefix[i-1]) + index]
                
                
                
        return ''.join(s)
        