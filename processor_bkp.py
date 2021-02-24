def get_matrix(name=''):
    print(f"Enter size of {name} matrix:")
    n, m = map(int, input().split())
    print(f"Enter {name} matrix:")
    return [[float(num) for num in input().split()] for _ in range(n)]


def matrix_by_number_multiplication(A, c):
    return [[A[n][m] * float(c) for m in range(len(A[n]))] for n in range(len(A))]


def matrix_addition(A, B):
    C = []
    if len(A) != len(B):
        print("ERROR")
    else:
        for n in range(len(A)):
            if len(A[n]) != len(B[n]):
                print("ERROR")
                break
            else:
                tmp = []
                for m in range(len(A[n])):
                    tmp.append(str(float(A[n][m]) + float(B[n][m])))
                C.append(tmp)
    return C


def matrix_by_matix_multiplication(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)

    if len(B) != len(A[0]):
        print("ERROR")
    else:
        # parcours des lignes de A
        for i in range(len(A)):
            # parcours de colonnes de B
            for j in range(len(B[0])):
                # parcours des elements (lignes) de B
                for k in range(len(B)):
                    C[i][j] += float(A[i][k]) * float(B[k][j])
    return C


def matrix_transposition():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    trans_choice = input()
    A = get_matrix()
    B = []
    for i in range(len(A)):
        B.append([])
        for j in range(len(A[0])):
            B[i].append(0)

    if trans_choice == '1':
        for m in range(len(A)):
            for n in range(len(A[m])):
                B[n][m] = A[m][n]
        A = B
    elif trans_choice == '2':
        for m in range(len(A)):
            for n in range(len(A[m])):
                B[len(A[m]) - n - 1][len(A[m]) - m - 1] = A[m][n]
        A = B
    elif trans_choice == '3':
        [m.reverse() for m in A]
    elif trans_choice == '4':
        A.reverse()
    return A


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def matrix_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * matrix_determinant(get_matrix_minor(matrix, 0, c))
    return determinant


while True:
    print()
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input()
    C = None

    if choice == '0':
        break
    elif choice == '1':
        A = get_matrix('first')
        B = get_matrix('second')
        C = matrix_addition(A, B)
    elif choice == '2':
        A = get_matrix('first')
        c = input('Enter constant: ')
        C = matrix_by_number_multiplication(A, c)
    elif choice == '3':
        A = get_matrix('first')
        B = get_matrix('second')
        C = matrix_by_matix_multiplication(A, B)
    elif choice == '4':
        C = matrix_transposition()
    elif choice == '5':
        A = get_matrix()
        C = matrix_determinant(A)
        print("The result is:")
        print(C)
        C = None
    elif choice == '6':
        pass

    if C is not None:
        print("The result is:")
        [print(*line) for line in C]
