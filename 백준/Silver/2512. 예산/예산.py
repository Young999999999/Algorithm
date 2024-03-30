N = int(input())
req = list(map(int, input().split()))
M = int(input())
start = 1
end = max(req)
if sum(req) <= M:
    print(max(req))
else:
    for i in range(1000):
        mid = (start + end) // 2
        add_up = 0

        for i in req:
            if i <= mid:
                add_up += i
            else:
                add_up += mid
        if add_up > M:
            end = mid - 1

        elif add_up < M:
            start = mid + 1

    print(mid)