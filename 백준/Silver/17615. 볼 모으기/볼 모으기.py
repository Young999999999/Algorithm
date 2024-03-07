n = int(input())
ball = list(input())

# i ) RRRRBBBB R공 옮기기
# ii ) RRRRBBBB B공 옮기기
# iii ) BBBBRRRR R공 옮기기
# iiii ) BBBBRRRR B공 옮기기

CNT = 100000000000
# i case
bit = 0
cnt = 0

for i in ball :
    if i == 'B':
        bit = 1
    if bit == 1 and i == 'R' :
       cnt += 1
CNT = min (cnt,CNT)
#print("i ", cnt)

# ii case
bit = 0
cnt = 0
for i in range(n-1,-1,-1):
    if ball[i] == 'R':
        bit = 1
    if bit == 1 and ball[i] == 'B' :
        cnt += 1

CNT = min(cnt,CNT)
#print("ii ", cnt)

# iii case

bit = 0
cnt = 0
for i in range(n-1,-1,-1):
    if ball[i] == 'B':
        bit = 1
    if bit == 1 and ball[i] == 'R' :
        cnt += 1
#print("iii ",cnt)

CNT = min(cnt,CNT)

# iiii case
bit = 0
cnt = 0

for i in ball :
    if i == 'R':
        bit = 1
    if bit == 1 and i == 'B' :
       cnt += 1

#print("iiii ",cnt)
CNT = min (cnt,CNT)
print(CNT)