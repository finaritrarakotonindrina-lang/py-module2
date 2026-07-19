def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if (temp_int < 0):
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif (temp_int > 40):
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return temp_int


def test_temperature() -> None:
    value = ["25", "abc", "100", "-50"]
    for n in value:
        print(f"input data is '{n}'")
        try:
            new_value = input_temperature(n)
            print(f"Temperature is now {new_value}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
