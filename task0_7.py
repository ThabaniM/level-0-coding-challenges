def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * (5 / 9)
    return celsius


def celsius_to_farenheit(celsius):
    return (celsius * (9 / 5)) + 32


if __name__ == "__main__":
    print(
        f"""100°F is equal to {farenheit_to_celsius(100)}°C
    While 27°C is equal to {celsius_to_farenheit(100)}°F
    """
    )
