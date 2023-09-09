while True:
    n = int(input("Quer ver a tabuada de qual valor?"))
    if n < 0:
        break
    for i in range(1,11):
        r = i * n
        print(f"{n} x {i} = {r}")
print(f'{n} não! Só números positivos paizão')
print('FIM')



