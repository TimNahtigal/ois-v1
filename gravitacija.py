def izracunGravitacije(nadmvisina):
	C = 6.674 * 10**-11
	M = 5.972 * 10**24
	r = 6.371 * 10**6

    a = (C * M) / (r + nadmvisina)**2
    return a

def izpis(visina){
    print("Gravitacijski pospešek na " + visina + " km nadmorske višine je" + izracunGravitacije(visina * 1000) + " m/s^2\n")
}

print("OIS je zakon!")
print(izpis(0.0))
print(izpis(10.0))
print(izpis(1000.0))
print(izpis(10000))

