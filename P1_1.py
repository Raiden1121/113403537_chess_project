def can_king_move(checkerboard, current_position, target_position):
    x1, y1 = current_position
    x2, y2 = target_position

    if not (0 <= x2 < 8 and 0 <= y2 < 8):
        return "No"

    if (x1, y1) == (x2, y2):
        return "No"
          
    if checkerboard[x2][y2] == 1:
        return "No"

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx <= 1 and dy <= 1:
        return "Yes"

    return "No"


current_position = tuple(map(int, input().split()))  
target_position = tuple(map(int, input().split()))   


print(can_king_move(checkerboard, current_position, target_position))
