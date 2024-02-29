def izracunGravitacije(nadmvisina):
	C = 6.674 * 10**-11
	M = 5.972 * 10**24
	r = 6.371 * 10**6

	a = (C * M) / (r + nadmvisina)**2
	return a

def izpis(visina):
	print("Gravitacijski pospešek na " + str(visina) + " km nadmorske višine je " + str(izracunGravitacije(visina * 1000)) + " m/s^2")


print("OIS je zakon!")
izpis(int(input("Stevilo ")))

