import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                
                # skip . 
                if board[r][c] == '.':
                    continue


                # tuple to define which of the 9 boxes currently located in
                box_id = (r// 3, c // 3)

                if value in cols[c]:
                    return False
                cols[c].add(value)

                if value in rows[r]:
                    return False   
                rows[r].add(value)
                
                if value in boxes[box_id]:
                    return False
                boxes[box_id].add(value)

        return True
                
