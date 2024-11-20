# Datu ievade terminālī
lapa=int(input("Ievadi skaitli: "))
print(type(lapa))
print(lapa**2)

# Skaitļa pārbaude (pāra vai nepāra)
lapa=int(input("Ievadi skaitli: "))
if lapa%2==0:
    print(f"{lapa} ir pāra skaitlis!")
elif lapa%2!=0:
    print(f"{lapa} ir nepāra skaitlis!")
else:
    print(f"{lapa} nav ne pāra, ne nepāra!")
    
# Vai dalās ar 27?
lapa=int(input("Ievadi skaitli: "))
if lapa%27==0:
    print(f"{lapa} dalās ar 27!")
else:
    print(f"{lapa} nedalās ar 27!")



