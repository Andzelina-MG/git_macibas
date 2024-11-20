# Aprēķināt ievadītajam skaitlim ciparu summu
# 235-->2+3+5=10

# 1. daļa - datu ievade
skaitlis=int(input("Lūdzu, ievadiet skaitli: "))
skaitlis1=skaitlis

# 2. daļa - aprēķins
cip_summa=0
while skaitlis1>0:
    cip_summa+=skaitlis1%10  #235 (iegūst pēdējo ciparu)
    skaitlis1//=10   #skaitlis=skaitlis//10

# 3. daļa - datu izvade
print(f"Skaitļa {skaitlis} ciparu summa ir: {cip_summa}.")