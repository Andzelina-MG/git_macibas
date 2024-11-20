# Izveidot programmu, kas prasa lietotājam ievadīt skaitli n,
# tad programma aprēķina n+nn+nnn
# rezultāts tiks parādīts terminālī

# 23-->23+2323+232323 
# 7-->7+77+777

# 1. daļa - datu ievade
n=input("Ievadi skaitli: ")

# 2. daļa - aprēķins
summa=int(n)+int(n*2)+int(n*3)

# 3. daļa - datu izvade
print(n, "+", n*2, "+", n*3, "=", summa)
print(f"{n} + {n*2} + {n*3} = {summa}")
