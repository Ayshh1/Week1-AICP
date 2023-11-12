
item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = ['Compact', 'Tower', '8 GB', '16 GB', '32 GB', '1 TB HDD', '2 TB HDD', '4 TB HDD', '240 GB SSD', '480 GB SSD',
                 '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer', 'Standard Version', 'Professional Version']
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]


basic_case = 'A1'
basic_ram = 'B1'
basic_hdd = 'C1'
basic_price = 200.00


def get_user_choice(category):
    print(f"\n{category} Options:")
    for i, code in enumerate(item_codes):
        if code.startswith(category):
            print(f"{code}: {descriptions[i]} - ${prices[i]}")
    
    user_choice = input(f"Choose a {category} (Enter item code): ").upper()
    

    while user_choice not in item_codes or not user_choice.startswith(category):
        print("Invalid choice. Please enter a valid item code.")
        user_choice = input(f"Choose a {category} (Enter item code): ").upper()
    
    return user_choice


def calculate_total_price(case, ram, hdd):
    total_price = basic_price
    chosen_items = []

    
    for i in range(len(item_codes)):
        if item_codes[i] == case or item_codes[i] == ram or item_codes[i] == hdd:
            total_price += prices[i]
            chosen_items.append(descriptions[i])

    
    print("\nChosen Items:")
    for item in chosen_items:
        print(f"- {item}")
    
    print(f"\nTotal Price: ${total_price:.2f}")


print("WELOME TO OUR ONLINE COMPUTER SHOP!")


chosen_case = get_user_choice('A')
chosen_ram = get_user_choice('B')
chosen_hdd = get_user_choice('C')


calculate_total_price(chosen_case, chosen_ram, chosen_hdd)
