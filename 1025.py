n = input()
for i in range(len(n)):
    print("[", end='')
    print(int(n[i]) * (10**(4-i)), end='')
    print("]")
