x = list(map(int, input().split()))
N = len(x)
over = []
for i in range(N-1):
    for j in range(0, N-i-1):
        if(x[j] > x[j+1]):
            x[j+1], x[j] = x[j], x[j+1]
        over.append(x.copy())

print(over)
print(x)