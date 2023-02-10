import os
bines=['402318','413406','417849','493158','518899','522174','528851','547074','547096','548236','439120','549138','549631','549949','528843']

file=open('pedido.txt','r')
contador=0
tota=0
for line in file:
	code=line.rstrip('\r').rstrip('\n')
	ab=code.split(',')
	bin=ab[0]
	cantidad=ab[1]
	print(ab)
	print(cantidad)
	if bin in bines:
		contador=contador+int(cantidad)
		print(bin+","+str(cantidad)+" especial")
	tota=tota+int(cantidad)

print("<----------------------->")
print("Especiales:"+str(contador))
print("Totales:"+str(tota))
