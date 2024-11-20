# Izvadīt elementus apgrieztā secībā - I līmenis
saraksts1=[5,2,1,2,1,12]
summa=0
saraksts1.reverse() # Reverse - apgriezts
for elements in saraksts1:
    print(elements)

# Izvadīt elementus apgrieztā secībā - II līmenis
saraksts1=[5,2,1,2,1,12]
summa=0
skaititajs=0
for elements in saraksts1:
    print(saraksts1[len(saraksts1)-skaititajs])
    skaititajs+=1