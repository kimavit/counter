a = int(input())
b = int(input())
cnt = 0
for i in range(a, b+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        cnt = cnt+1
print(cnt)
