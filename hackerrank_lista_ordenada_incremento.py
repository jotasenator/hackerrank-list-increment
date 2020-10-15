

l=[2,1,5,8]

lista1=[sorted(l[:i+1]) for i in range(len(l))]

lista2=[i[j]*(j+1) for i in lista1 for j in range(len(i))]



print(lista1)
print(lista2)
print(sum(lista2))

'''lista1=[]
print(lista)
for i in lista:
	for j in range(len(i)):
		lista1.append(i[j]*(j+1))
print(lista1)
print(sum(lista1))'''

