# Aprēķināt ievadītajam decimāldaļskaitlim ciparu summu

skaitlis=input("Lūdzu, ievadiet pirmo decimāldaļskaitli: ")
skaitlis1=input("Lūdzu, ievadiet otro decimāldaļskaitli: ")

cip_summa=sum(int(cipars) for cipars in skaitlis)
    # cipars - cikla skaitītājs

print(f"Skaitļa {skaitlis} ciparu summa ir: {cip_summa}.")


"""
cip_summa=0
while skaitlis1>0:
cip_summa+=skaitlis1%10
skaitlis1//=10
"""