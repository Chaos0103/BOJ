def turn(side, n):
    for _ in range(n):
        tmp = side[0][0]
        side[0][0] = side[2][0]
        side[2][0] = side[2][2]
        side[2][2] = side[0][2]
        side[0][2] = tmp

        tmp = side[0][1]
        side[0][1] = side[1][0]
        side[1][0] = side[2][1]
        side[2][1] = side[1][2]
        side[1][2] = tmp


for _ in range(int(input())):
    n = int(input())
    data = list(input().split())
    up_side = [['w'] * 3 for _ in range(3)]
    down_side = [['y'] * 3 for _ in range(3)]
    right_side = [['b'] * 3 for _ in range(3)]
    left_side = [['g'] * 3 for _ in range(3)]
    behind_side = [['o'] * 3 for _ in range(3)]
    front_side = [['r'] * 3 for _ in range(3)]
    for d in data:
        if d[0] == 'U':
            if d[1] == '-':
                cycle = 1
                c = 3
            else:
                cycle = 3
                c = 1
            for _ in range(cycle):
                for i in range(3):
                    tmp = front_side[0][i]
                    front_side[0][i] = left_side[0][i]
                    left_side[0][i] = behind_side[2][2-i]
                    behind_side[2][2-i] = right_side[0][i]
                    right_side[0][i] = tmp
            turn(up_side, c)
        elif d[0] == 'D':
            if d[1] == '+':
                cycle = 1
            else:
                cycle = 3
            for _ in range(cycle):
                for i in range(3):
                    tmp = front_side[2][i]
                    front_side[2][i] = left_side[2][i]
                    left_side[2][i] = behind_side[0][2-i]
                    behind_side[0][2-i] = right_side[2][i]
                    right_side[2][i] = tmp
            turn(down_side, cycle)
        elif d[0] == 'F':
            if d[1] == '+':
                cycle = 1
            else:
                cycle = 3
            for _ in range(cycle):
                for i in range(3):
                    tmp = up_side[2][i]
                    up_side[2][i] = left_side[2-i][2]
                    left_side[2-i][2] = down_side[0][2-i]
                    down_side[0][2-i] = right_side[i][0]
                    right_side[i][0] = tmp
            turn(front_side, cycle)
        elif d[0] == 'B':
            if d[1] == '+':
                cycle = 1
            else:
                cycle = 3
            for _ in range(cycle):
                for i in range(3):
                    tmp = up_side[0][2-i]
                    up_side[0][2-i] = right_side[2-i][2]
                    right_side[2-i][2] = down_side[2][i]
                    down_side[2][i] = left_side[i][0]
                    left_side[i][0] = tmp
            turn(behind_side, cycle)
        elif d[0] == 'L':
            if d[1] == '+':
                cycle = 1
            else:
                cycle = 3
            for _ in range(cycle):
                for i in range(3):
                    tmp = up_side[i][0]
                    up_side[i][0] = behind_side[i][0]
                    behind_side[i][0] = down_side[i][0]
                    down_side[i][0] = front_side[i][0]
                    front_side[i][0] = tmp
            turn(left_side, cycle)
        elif d[0] == 'R':
            if d[1] == '+':
                cycle = 1
            else:
                cycle = 3
            for _ in range(cycle):
                for i in range(3):
                    tmp = up_side[i][2]
                    up_side[i][2] = front_side[i][2]
                    front_side[i][2] = down_side[i][2]
                    down_side[i][2] = behind_side[i][2]
                    behind_side[i][2] = tmp
            turn(right_side, cycle)

    for a in range(3):
        for b in range(3):
            print(up_side[a][b], end='')
        print()
