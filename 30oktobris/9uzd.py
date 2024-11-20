# Saskaitīt tikai to elementa summu, kas ir nepāra
saraksts1=[5,2,1,2,1,12]
summa=0
for elements in saraksts1:
    if elements%2!=0: # Ja elementa dalījums ar 2, atlikums nav vienāds ar 0, tad saskaita
       summa+=elements
print("Summa =", summa)

# Saskaitīt tikai to elementa summu, kas ir pāra
saraksts1=[5,2,1,2,1,12]
summa=0
for elements in saraksts1:
    if elements%2==0: # Ja elementa dalījums ar 2, atlikums ir vienāds ar 0, tad saskaita
       summa+=elements
print("Summa =", summa)