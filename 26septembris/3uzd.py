# for cikls ar iterēšanu pār vārdnīcu (dictionary)
# iterēšana - darīt to pašu darbību vairākas reizes
# vārdnīca - specifiska pieraksta forma
# vārdnīca sastāv no atslēgām un to vērtībām

personas={"vārds": "Andželīna", "vecums": 16, "pilseta": "Grobiņa"}
print(personas)
for key, value in personas.items():
    print(f"{key} ---> {value}")