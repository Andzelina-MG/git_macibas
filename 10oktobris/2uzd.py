# Aprēķināt ievadītajiem skaitļiem ciparu summu

# 1 daļa - datu ievade
skaitlis=float(input("Lūdzu, ievadiet pirmo decimālskaitli: "))
skaitlis1=float(input("Lūdzu, ievadiet otro decimālskaitli: "))

# 2. daļa - aprēķins
cip_summa=0
while skaitlis1>0:
    cip_summa+=skaitlis1%10
    skaitlis1//=10

#
cip_summa=sum(float(cipars)) for cipars in skaitlis)
    # cipars - cikla skaitītājs

print(f"Skaitļa {skaitlis} ciparu summa ir: {cip_summa}.")


