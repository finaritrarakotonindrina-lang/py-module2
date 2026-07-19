def input_temperature(temp_str: str) -> int | None:
    temp_int = int(temp_str)
    if (temp_int < 0):
        print("Caught input_temperature error: "
              f"{temp_int}°C is too cold for plants (min 0°C)")
    elif (temp_int > 40):
        print()
    else:
        return temp_int
    return None


def test_temperature() -> None:
    value = "25"
    print(f"Input data is '{value}'")

    input_temperature(value)
    print(f"Temperature is now {value}°C")
    print()
    try:
        value = "abc"
        print(f"Input data is '{value}'")

        input_temperature(value)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    finally:
        print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
