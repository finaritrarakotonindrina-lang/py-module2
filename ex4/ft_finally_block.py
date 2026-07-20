class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for n in plants:
            water_plant(n)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    plant_name = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plant_name)
    print()
    print("Testing invalid plants...")
    plant_name = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(plant_name)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
