while True:
    amount = input("¿Cantidad a invertir?: ")
    if amount.strip() == "":
        print("Por favor, ingrese un valor válido.")
    else:
        amount = float(amount)
        if amount < 0:
            print("La cantidad no puede ser negativa.")
        else:
            break

while True:
    annual_interest = input("¿Interés porcentual anual?: ")
    if annual_interest.strip() == "":
                print("Por favor, ingrese un valor válido.")
    else:
        annual_interest = float(annual_interest)
        if annual_interest < 0:
            print("La cantidad no puede ser negativa.")
        break

while True:
    years = input("¿Años?: ")
    if years.strip() == "":
        print("Por favor, ingrese un valor válido.")
    else:
        years = int(years)
        if years < 0:
            print("La cantidad no puede ser negativa.")
        break

for i in range(1, years + 1):
    capital = amount * (1 + annual_interest / 100) ** i
    capital = round(capital, 2)
    print("Capital after", i, "year(s):", capital)