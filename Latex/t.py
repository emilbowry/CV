def f(x):
	if x == True:
		return True
	return False


def g(x):
	if not f(x):
		return True
	return False


# this seems off because we can define it arbitrariliy recursively i.e


def f_prime_prime(x):
	if x == True:
		return True
	return False


def f_prime(x):
	if x == True:
		return True
	return False


def f(x):
	if x == True:
		return True
	return False


def g(x):
	if not f(x):
		return True
	return False
