total = int(input("o numero de segundos: "))
horas =total // 3600
minutos =(total % 3600) // 60
segundos = total % 60

print(f"{horas}:{minutos}:{segundos}")