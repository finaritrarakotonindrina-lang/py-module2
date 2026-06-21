class PlantError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_name: str) -> None:
    print("Opening watering system")
    try:
        water_plant(plant_name)
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
    for n in plant_name:
        test_watering_system(n)
    print()
    print("Testing valid plants...")
    print("Testing invalid plants...")
    plant_name = ["Tomato", "lettuce", "Carrots"]
    print("Cleanup always happens, even with errors!")
    for n in plant_name:
        test_watering_system(n)


if __name__ == "__main__":
    main()
