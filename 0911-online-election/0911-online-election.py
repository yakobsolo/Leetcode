class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leading = [persons[0]]
        count = Counter()
        mx = persons[0]
        count[mx] = 1
        leng = len(times)
        for i in range(1, leng):
            count[persons[i]] +=1
            if count[persons[i]] >=count[mx]:
                mx = persons[i]
            self.leading.append(mx)
           
    def q(self, t: int) -> int:
        val = bisect_right(self.times, t)
        return self.leading[val -1]
    
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
