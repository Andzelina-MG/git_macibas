# Nolasa skaitļus un aprēķina skaitļu summu
with open('dati.txt', 'r') as bums:
    sk=bums.readlines()
    # Kā katru rindu pārvērst par skaitli?
    # II līmenis
    # strip - noņem atstarpes
    skaitlis=[int(rinda.strip())    for rinda in sk]

print(type(sk[0]))
print(skaitlis)
summa=sum(skaitlis)

# Kā aprēķināt vidējo
videjaa=summa/len(skaitlis)
print(summa, videjaa)