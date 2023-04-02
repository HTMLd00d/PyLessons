n = int(input())
count_tail = 0
count_head = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_tail += 1
    else:
        count_head += 1
if count_head > count_tail:
    print(count_tail)
else:
    print(count_head)
