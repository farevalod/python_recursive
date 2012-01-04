def fib(numero):
	if (numero == 0) or (numero == 1):
		return 1
	else:
		return fib(numero-1)+fib(numero-2)

print fib(35)
