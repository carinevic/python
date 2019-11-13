celsius = int(input("pls enter integer numb: "))


def fahrenheit(cel):
    return round((((1.8 * 10) * (cel * 10)) / 100 + 32), 1)


print("the equivalent of " + str(celsius) + " deg celsius is " + str(fahrenheit(celsius)) + ".")

