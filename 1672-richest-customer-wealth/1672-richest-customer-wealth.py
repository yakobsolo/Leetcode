class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for account in accounts:
            wealth = max(wealth, sum(account))
        return wealth