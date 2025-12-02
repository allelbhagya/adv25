curr = 50

with open("data1.txt", "r") as f:
    seq = [line.strip() for line in f]

count = 0

for i in seq:
    if curr == 0:
        count+=1
    val = int(i[1:].strip())
    if i[0]=='R':
        curr = (curr + val) % 100
    elif i[0]=='L':
        curr = (curr-val)%100
print(count)
