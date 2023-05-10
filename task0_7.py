def to_celsius(farenheit):

    celsius = (farenheit - 32) * (5/9)
    return celsius


def to_farenheit(celsius):

    return (celsius * (9/5)) + 32


if __name__ ==  "__main__":
    print(f"""100°F is equal to {to_celsius(100)}°C
    While 27°C is equal to {to_farenheit(100)}°F
    """) 