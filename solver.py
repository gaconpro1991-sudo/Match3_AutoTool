import copy
from matcher import analyze_matches

def smart_best_move(board):
    best = None
    best_score = -999

    for r in range(len(board)):
        for c in range(len(board[0])):
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr >= len(board) or nc >= len(board[0]):
                    continue

                tmp = copy.deepcopy(board)
                tmp[r][c], tmp[nr][nc] = tmp[nr][nc], tmp[r][c]

                score, matches = analyze_matches(tmp)

                # bỏ nước đi vô dụng
                if score == 0:
                    continue

                if matches == [3]:
                    score -= 2

                if 4 in matches:
                    score += 3
                if 5 in matches:
                    score += 6

                if score > best_score:
                    best_score = score
                    best = ((r, c), (nr, nc))

    return best
