def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5/0
    elif operation_number == 2:
        open()
    elif operation_number == 3:
        "me" + 45


def test_error_types() -> None:
    value = [0, 1, 2, 3]
    for n in value:
        try:
            garden_operations(n)
            print(f"Testing operation{n}...")
        except ValueError as e:
            print(f"{e}")
