numero = int(input('digite um número de 0 a 9999'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"a unidade é: {u}")
print(f"a dezena é: {d}")
print(f"a centena é: {c}")
print(f"a milhar é: {m}")