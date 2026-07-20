class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def test() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print()
    print("Testing WaterError...")
    try:
        raise WaterError(" Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print()
    print("Testing catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
