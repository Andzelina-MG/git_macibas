# Izveidot programmu, kura prasa lietotājam ievadīt
# cilindra rādiusu un tā augstumu,
# tiek aprēķināts cilindra laukums un tilpums

import math

# math.pi

r=float(input("Lūdzu, ievadiet cilindra rādiusu: ")) # 2.34  2
h=float(input("Lūdzu, ievadiet cilindra augstumu: "))

laukums=2*math.pi*r**2+h*2*math.pi*r
tilpums=math.pi*r**2*h

# datu izvade
