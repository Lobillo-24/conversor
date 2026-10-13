def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def main():
    print("Conversor de temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción: ")
    valor = float(input("Introduce la temperatura: "))

    if opcion == "1":
        print(f"{valor} °C = {celsius_a_fahrenheit(valor):.2f} °F")
    elif opcion == "2":
        print(f"{valor} °F = {fahrenheit_a_celsius(valor):.2f} °C")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()