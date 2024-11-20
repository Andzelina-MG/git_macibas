# Datu nolasīšana no faila
# failu tipi ---> .txt, .csv, .json
# .txt - neformatēts
# .csv - tabula, kurā dati tiek atdalīti ar komatiem
# .json - formāts, kādā veida ir uzrakstīti dati

# Kā nolasīt datus - I līmenis
# mode - atvēršanas režīms (katru reizi verot vaļā dokumentu ir jānosaka veids, kā strādās ar failiem)
with open("pasaka.txt","r",encoding="utf-8") as gg:
    poga=gg.readlines()
    # read
    # readline
    # readlines

print(type(poga))
print(poga)
for rinda in poga:
    print(rinda.strip())

for i,rinda in enumerate(poga):
    print(f"{i+1}.rinda - {rinda.strip()}")


