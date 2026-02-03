def analyze_matches(board):
    rows, cols = len(board), len(board[0])
    matches = []
    score = 0

    # horizontal
    for r in range(rows):
        cnt = 1
        for c in range(1, cols):
            if board[r][c] == board[r][c-1] and board[r][c] is not None:
                cnt += 1
            else:
                if cnt >= 3:
                    matches.append(cnt)
                cnt = 1
        if cnt >= 3:
            matches.append(cnt)

    # vertical
    for c in range(cols):
        cnt = 1
        for r in range(1, rows):
            if board[r][c] == board[r-1][c] and board[r][c] is not None:
                cnt += 1
            else:
                if cnt >= 3:
                    matches.append(cnt)
                cnt = 1
        if cnt >= 3:
            matches.append(cnt)

    for m in matches:
        if m == 3:
            score += 3
        elif m == 4:
            score += 8
        else:
            score += 15

    return score, matches
