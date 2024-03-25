def match(a,b,status,note,depth) :

    if status == 0: #승
        aIDX = position[a]
        bIDX = position[b]
        note[aIDX] += 1
        note[bIDX+2] += 1
        if answer[aIDX] < note[aIDX] or answer[bIDX+2] < note[bIDX+2] :
            return


    elif status == 1: #무
        aIDX = position[a]
        bIDX = position[b]
        note[aIDX+1] += 1
        note[bIDX+1] += 1

        if answer[aIDX+1] < note[aIDX+1] or answer[bIDX+1] < note[bIDX+1] :
            return



    elif status == 2:  # 패
        aIDX = position[a]
        bIDX = position[b]
        note[aIDX + 2] += 1
        note[bIDX] += 1

        if answer[aIDX+2] < note[aIDX+2] or answer[bIDX] < note[bIDX] :
            return


    if depth == 15:
        result[str(note)] = 1
        return

    nextA ,nextB = allMatch[depth]

    match(nextA,nextB,0,note[:],depth+1)
    match(nextA, nextB, 1, note[:], depth + 1)
    match(nextA, nextB, 2, note[:], depth + 1)


result = {}
team = ['A','B','C','D','E','F']
allMatch = []

for i in range(6):
    for j in range(i+1,6):
        allMatch.append([team[i],team[j]])

position = {}
position['A'] = 0
position['B'] = 3
position['C'] = 6
position['D'] = 9
position['E'] = 12
position['F'] = 15

for i in range(4):
    answer = list(map(int,input().split()))
    note = answer[:]

    match('A', 'B', 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)
    match('A', 'B', 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)
    match('A', 'B', 2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)

    if result.get(str(answer)) != None :
        print(1, end=' ')
    else:
        print(0, end=' ')