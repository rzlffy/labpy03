max=0
while True:
	a=int(input('Masukkan bilangan='))
	if max < a:
		max = a
	if a==0:
		break
print('Bilangan terbesarnya adalah',max)