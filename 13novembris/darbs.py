# Jāizveido stabiņu diagramma
import matplotlib.pyplot as plt
# pip install matplotlib
# matplotlib - bibliotēka

# Nolasām datus
nosaukums='dati.txt'
kategorija=[] # Uz x ass
vertiba=[] # Uz y ass

# Atveram failu un nolasām datus - lasam katru rindu!
# with open('c:/Users/Lietotajs/Desktop/SKOLA 10. KLASE/PROGRAMMING1/13novembris/dati.txt', 'r', encoding='utf-8') as po:
with open('dati.text', 'r', encoding='utf-8') as po:
    for linijas in po:
        # Noņemt liekos tukšumus un sadalīt pa sarakstiem
        daljas=linijas.strip().split("-")
        if len(daljas)==2:
            kat=daljas[0].strip()
            kategorija.append(kat)
            vert=int(daljas[1].strip())
            vertiba.append(vert)

# Veidojam satbiņu diagrammu
plt.figure(figsize=(10,6)) # Ko tas nozīmē?
plt.bar(kategorija, vertiba, color='lightpink')

plt.xlabel("Pilsētas")
plt.ylabel("Skaits")

plt.title("Uzņēmumu skaits")
plt.show()


