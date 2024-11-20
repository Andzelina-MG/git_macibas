# Izvadīt visus nepāra skaitļus diapazonā no 0 līdz 100
skaititajs=0
while skaititajs<=100:
    if skaititajs%2!=0: # Ja skaitītājs dalījumā ar 2, atlikums nav vienāds ar 0, tad ir nepāra skaitlis
       print(skaititajs)
       skaititajs+=1 

# Izvadīt visus pāra skaitļus diapazonā no 0 līdz 100
skaititajs=0
while skaititajs<=100:
    if skaititajs%2==0: # Ja skaitītājs dalījumā ar 2, atlikums ir vienāds ar 0, tad ir pāra skaitlis
       print(skaititajs)
       skaititajs+=1