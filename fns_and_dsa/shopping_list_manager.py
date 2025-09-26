# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("No item entered. Nothing added.")
        elif choice == '2':
            if not shopping_list:
                print("Shopping list is empty. Nothing to remove.")
                continue
            item = input("Enter the item to remove: ").strip()
            # remove first case-insensitive match while preserving original casing
            found = False
            for i, existing in enumerate(shopping_list):
                if existing.lower() == item.lower():
                    removed = shopping_list.pop(i)
                    print(f"'{removed}' has been removed from the list.")
                    found = True
                    break
            if not found:
                print(f"Item not found in the shopping list: {item}")
        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Current shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


