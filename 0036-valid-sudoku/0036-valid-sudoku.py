class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele != ".":
                    if ele in row[r] or ele in col[c] or ele in box[r//3, c//3]: return False
                    row[r].add(ele)
                    col[c].add(ele)
                box[r//3, c//3].add(ele)
        return True