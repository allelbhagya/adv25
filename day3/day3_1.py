def max_joltage(s):
    best = -1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            val = int(s[i]) * 10 + int(s[j])
            if val > best:
                best = val
    return best


with open("data3.txt", "r") as f:
    seq = [line.strip() for line in f]

res = 0
for i in seq:
    res+=max_joltage(i)
print(res)