# Reizinājuma funkcija - saraksta elementu reizinājums
saraksts1=[5,2,1,2,1,12]
reizinajums=1
for elements in saraksts1:
    reizinajums=reizinajums*elements
print("Reizinajums =", reizinajums)

saraksts1=[5,2,1,2,1,12]
reizinajums=1
for elements in saraksts1:
    print("Tekošais elements =", elements, "Tekošais reizinājums =", reizinajums)
    reizinajums=reizinajums*elements
print("Reizinajums =", reizinajums)