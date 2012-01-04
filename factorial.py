def factorial(numero):
	assert numero >= 0
	if numero == 0:
		return 1
	else:
		return numero * factorial(numero-1)

print factorial(4)
