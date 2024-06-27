import argparse
from equipment_inventory.equipment import Computer, Peripheral
from equipment_inventory.manager import InventoryManager

def main():
    parser = argparse.ArgumentParser(description="Inventory Management System")
    parser.add_argument('--add', type=str, help="Add new equipment")
    parser.add_argument('--view', action='store_true', help="View all equipment")
    parser.add_argument('--save', type=str, help="Save equipment list to file")
    parser.add_argument('--load', type=str, help="Load equipment list from file")
    args = parser.parse_args()

    manager = InventoryManager()

    if args.add:
        # Example: Add a new computer
        computer = Computer(id=1, name="Office PC", serial_number="123456", cpu="Intel i5", ram="16GB", storage="512GB SSD")
        manager.add_equipment(computer)

    if args.view:
        manager.view_equipment()

    if args.save:
        manager.save_to_file(args.save)

    if args.load:
        manager.load_from_file(args.load)

if __name__ == "__main__":
    main()
