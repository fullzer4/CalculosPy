NPS = int(input("Quantos decibeis o comodo tem: "))

NPS = NPS/20
NPS = 10**NPS
NPS = NPS * 2 * 10**-5

print("")
print("A pressao sonora do seu ambiente é: ", NPS)