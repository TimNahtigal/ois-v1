print("OIS je zakon!")

nadmvisina = input()

C = 6.674 * 10**-11
M = 5.972 * 10**24
r = 6.371 * 10**6

def izracun(nadmvisina):
    a = (C * M) / (r + nadmvisina)**2
    return a