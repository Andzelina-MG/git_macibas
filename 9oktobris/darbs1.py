# f noformēšana pie izdrukas ...
# f-string pielietojums ... simbolu virkni
"""
aka="Trešdiena"
print(aka)
print(f"Šodien ir {aka}.")
lapa=4.56734556
print(type(lapa))
print(f"Man ir skaitlis {lapa:.2f}")

# Izdrukāt PI ar 5 cipariem aiz komata
import math
a=math.pi
print(f"PI ir: {a:.5f}")
print(f"Pi ir: {math.pi:.5f}")
print(f"Pi ir: {math.pi:.0f}") # aiz komata nav neviens skaitlis - vesels skaitlis

# Par tekstu un tā garumu
print(f"{aka:.3}")
"""

# Ievadi vārdu un izvadi pēdējo burtu
aa=input("Ievadi vārdu: ") # aa - Kas tas ir par datu tipu? --> paka

# 1. risinājums
pedejais_burts=aa[-1]
print(f"Pēdējais simbols ir: {pedejais_burts}.")

# 2. risinājums 
# len - Kas tas ir? Simbolu skaitu mainīgajā
pedejais_burts1=aa[len(aa)-1]
print(f"Pēdējais simbols ir: {pedejais_burts}.")

skaitlis=str(1234)
# Noteikt ciparu skaitu
ciparu_skaits=len(skaitlis)
print(ciparu_skaits)




