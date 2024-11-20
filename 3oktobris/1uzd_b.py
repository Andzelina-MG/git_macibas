# Aprēķināt ievadītajam skaitlim ciparu summu
# 235-->2+3+5=10

skaitlis=input("Lūdzu, ievadi skaitli: ")

cip_summa=sum(int(cipars) for cipars in skaitlis) # cipars - cikla skaitītājs

print(f"Skaitļa {skaitlis} ciparu summa ir: {cip_summa}.")