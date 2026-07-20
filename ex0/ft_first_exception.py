def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    value = "25"
    print(f"Input data is '{value}'")
    print(f"Temperature is now {input_temperature(value)}°C")
    print()
    try:
        value = "abc"
        print(f"Input data is '{value}'")

        input_temperature(value)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
