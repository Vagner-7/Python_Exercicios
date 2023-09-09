s = 0
c = 0
for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            s += num
            c += 1
print(f"a soma de todos valores impares e multiplos de três é {s}")
print(f"a quantidade de todos valores impares e multiplos de três é {c}")



