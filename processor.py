class Matrix:
    def __init__(self, rows=None, cols=None, array=None):
        if rows and cols:
            self.rows = rows
            self.cols = cols
        else:
            self.inputSize()
        if array:
            self.array = array
        else:
            self.array = []
            self.inputArray()

    def __str__(self):
        string = ''
        for row in self.array:
            for element in row:
                string += str(element) + ' '
            string += '\n'
        return string

    def __add__(self, other):
        if self.sameSize(other):
            result = self.array[:]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] += other.array[i][j]
            return Matrix(self.rows, self.cols, result)
        else:
            return "The operation cannot be performed."

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = self.array[:]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] *= other
            return Matrix(self.rows, self.cols, result)
        elif isinstance(other, Matrix) and self.cols == other.rows:
            result = []
            for i in range(self.rows):
                result.append([])
                for j in range(other.cols):
                    row = self.getRow(i)
                    col = other.getCol(j)
                    result[i].append(sum([row[i] * col[i] for i in range(len(row))]))
            return Matrix(self.rows, other.cols, result)
        else:
            return "The operation cannot be performed."

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = self.array[:]
            for i in range(self.rows):
                for j in range(self.cols):
                    if result[i][j]:
                        result[i][j] /= other
            return Matrix(self.rows, self.cols, result)

    def inputArray(self):
        for i in range(self.rows):
            row = input().split(maxsplit=self.cols)
            if hasFloat(row):
                self.array.append(list(map(float, row)))
            else:
                self.array.append(list(map(int, row)))

    def inputSize(self):
        self.rows, self.cols = map(int, input().split())

    def sameSize(self, other):
        if self.cols == other.cols and self.rows == other.rows:
            return True
        else:
            return False

    def getRow(self, index):
        return self.array[index]

    def getCol(self, index):
        return [elem[index] for elem in self.array]

    def transpose(self, line='Main diagonal'):
        if line == 'Main diagonal':
            result = [self.getCol(i) for i in range(self.cols)]
            return Matrix(self.cols, self.rows, result)
        elif line == 'Side diagonal':
            result = [reversed(self.getCol(i)) for i in reversed(range(self.cols))]
            return Matrix(self.cols, self.rows, result)
        elif line == 'Vertical line':
            result = [reversed(self.getRow(i)) for i in range(self.rows)]
            return Matrix(self.rows, self.cols, result)
        elif line == 'Horizontal line':
            result = [self.getRow(i) for i in reversed(range(self.rows))]
            return Matrix(self.rows, self.cols, result)

    def getDeterminant(self):
        if self.cols == self.rows:
            if self.cols == 1:
                return self.array[0][0]
            else:
                determinant = [self.array[0][i] * self.getMinor(0, i).getDeterminant() * coFactor(0, i)
                            for i in range(self.cols)]
                return sum(determinant)
        else:
            return "Can't calculate determinant for non-square matrix"

    def getMinor(self, row, col):
        result = []
        for i in range(self.rows):
            if i != row:
                result.append([self.array[i][j] for j in range(self.cols) if j != col])
        return Matrix(self.rows - 1, self.cols - 1, result)

    def coFactors(self):
        result = [[coFactor(i, j) * self.getMinor(i, j).getDeterminant() for j in range(self.cols)]
                  for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def inverted(self):
        determinant = self.getDeterminant()
        coFactors = self.coFactors().transpose()
        return coFactors / determinant


def coFactor(i, j):
    return (-1) ** (i + j)


def hasFloat(iterable):
    if sum(['.' in element for element in iterable]) > 0:
        return True
    return False


def showMenu(hashtable):
    for key, value in hashtable.items():
        print(f"{key}. {value}")


while True:
    menu = {1: 'Add matrices',
            2: 'Multiply matrix by a constant',
            3: 'Multiply matrices',
            4: 'Transpose matrix',
            5: 'Calculate a determinant',
            6: 'Inverse matrix',
            0: 'Exit'}
    showMenu(menu)
    choice = int(input("Your choice: "))
    if choice == 1:
        rowsA, colsA = map(int, input("Enter size of first matrix: ").split())
        print("Enter first matrix:")
        A = Matrix(rowsA, colsA)
        rowsB, colsB = map(int, input("Enter size of second matrix: ").split())
        print("Enter second matrix:")
        B = Matrix(rowsB, colsB)
        C = A + B
    elif choice == 2:
        rowsA, colsA = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        A = Matrix(rowsA, colsA)
        B = (input("Enter constant: "))
        if B.isdigit():
            B = int(B)
        else:
            B = float(B)
        C = A * B
    elif choice == 3:
        rowsA, colsA = map(int, input("Enter size of first matrix: ").split())
        print("Enter first matrix:")
        A = Matrix(rowsA, colsA)
        rowsB, colsB = map(int, input("Enter size of second matrix: ").split())
        print("Enter second matrix:")
        B = Matrix(rowsB, colsB)
        C = A * B
    elif choice == 4:
        menuTranspose = {1: 'Main diagonal',
                         2: 'Side diagonal',
                         3: 'Vertical line',
                         4: 'Horizontal line'}
        print()
        showMenu(menuTranspose)
        choice = menuTranspose[int(input("Your choice: "))]
        rowsA, colsA = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        A = Matrix(rowsA, colsA)
        C = A.transpose(choice)
    elif choice == 5:
        rowsA, colsA = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        A = Matrix(rowsA, colsA)
        C = A.getDeterminant()
    elif choice == 6:
        rowsA, colsA = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        A = Matrix(rowsA, colsA)
        C = A.inverted()
    elif choice == 0:
        break
    print(f"The result is:\n{C}")
