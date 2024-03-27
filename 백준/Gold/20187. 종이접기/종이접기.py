def RL(matrix): #왼쪽으로 펼치는 그림

    tmp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tmp[i][len(matrix[0])-1-j] = convertX(matrix[i][j])

    return tmp

def DU(matrix):  # 아래로 펼치는 그림
    tmp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tmp[len(matrix)-1-i][j] = convertY(matrix[i][j])

    return tmp



def convertX(num):
    if num == 0 :
        return 1
    if num == 2 :
        return 3
    if num == 1:
        return 0
    if num == 3 :
        return 2

def convertY(num):
    if num == 0:
        return 2
    if num == 2:
        return 0
    if num == 1:
        return 3
    if num == 3:
        return 1

n = int(input())
opList = input().split()
opList.reverse()
matrix = [[int(input())]]
# print(matrix)


for op in opList:

    if op == 'R':
        appendix = RL(matrix)

        for i in range(len(matrix)):
            appendix[i].extend(matrix[i])

        matrix= [i[:] for i in appendix]
        #
        # print('R')
        # print(matrix)


    if op == 'L':
        appendix = RL(matrix)

        for i in range(len(matrix)):
            matrix[i].extend(appendix[i][:])
        #
        # print('L')
        # for i in matrix:
        #     print(i)

    if op == 'D':
        appendix = DU(matrix)

        appendix += matrix
        matrix = [i[:] for i in appendix]
        # print('D')
        # for i in matrix:
        #     print(i)

    if op == 'U':
        appendix = DU(matrix)
        matrix += [i[:] for i in appendix]
        #
        # print('U')
        # for i in matrix:
        #     print(i)


for i in matrix:
    print(*i)