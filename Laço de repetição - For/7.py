num = int(input())
s = 0

for i in range(1, num +1):
    if num % i == 0:
        s += 1
if s == 2:
    print(f"o número {num} foi divisível {s} vezes, logo é primo")
else:
    print(f"O número {num} foi divisível {s} vezes, logo não é primo")
