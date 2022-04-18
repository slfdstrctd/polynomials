def polinom(_vars, vector, _max, truth_table):
    triangle = [[0] * 64 for i in range(64)]

    print("Исходный вектор:")
    for i in range(_max):
        triangle[0][i] = vector[i]
        print(triangle[0][i], end=" ")

    tri_max = _max - 1
    for i in range(1, _max):
        for j in range(tri_max):
            triangle[i][j] = triangle[i - 1][j] ^ triangle[i - 1][j + 1]
        tri_max = tri_max - 1

    print("\nРезультат: ")
    check = 0
    if triangle[0][0]:
        print("1")
    for i in range(_max):
        if triangle[i][0]:
            for j in range(_vars):
                if truth_table[i][j]:
                    print("x_" + str(j + 1), end="")
                    check = check + 1

            if i != _max:
                print("+", end="")

    if not check and not triangle[0][0]:
        print("0")
    print("\b \n")


def generate_table(table, _vars, _max):
    for _i in range(_max):
        for _j in range(_vars):
            table[_i][_vars - _j - 1] = ((_i >> _j) & 1) == 1


_vars = 3

tt = [[0] * 6 for i in range(64)]

v = [0, 1, 0, 0, 1, 0, 1, 1]
MAX_TABLE = pow(2, _vars)

generate_table(tt, _vars, MAX_TABLE)

polinom(_vars, v, MAX_TABLE, tt)
