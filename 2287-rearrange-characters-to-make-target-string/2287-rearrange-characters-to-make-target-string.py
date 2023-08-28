class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = Counter(s)
        count_target = Counter(target)
        ans = len(s)
        for let in target:
            cnt_tar = count_target[let]
            cnt = count[let]
            if cnt_tar > cnt:
                return 0
            else:
                rem = cnt//cnt_tar
            ans = min(rem, ans)
        return ans
                
            