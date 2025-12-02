curr = 50

with open("data1.txt", "r") as f:
    seq = [line.strip() for line in f]

count = 0

for move in seq:
    direction = move[0]
    steps = int(move[1:])

    step = 1 if direction == "R" else -1

    for _ in range(steps):
        curr = (curr + step) % 100
        if curr == 0:
            count += 1

print(count)
