class Restaurant:
    def menu(self, item):
        self.menu1 = {
            1: [150, "Chicken Biryani"],
            2: [250, "Mutton Biryani"],
            3: [100, "Veg Biryani"]
        }
        return self.menu1[item][1], self.menu1[item][0]


class FoodCourt(Restaurant):

    def display_menu(self):
        print("\n------ MENU ------")
        print("1. Chicken Biryani  - ₹150")
        print("2. Mutton Biryani   - ₹250")
        print("3. Veg Biryani      - ₹100")
        print("------------------")

    def order(self):
        self.total = 0
        self.orders = []

        while True:
            self.display_menu()

            item = int(input("Select Item: "))
            qty = int(input("Enter Quantity: "))

            item_name, price = self.menu(item)

            amount = price * qty
            self.total += amount

            self.orders.append([item_name, qty, amount])

            ch = input("Do you want to order another item? (yes/no): ")

            if ch.lower() != "yes":
                break

        self.billing()

    def billing(self):
        packing_charge = 20

        print("\n" + "=" * 40)
        print("\t\tBILL")
        print("=" * 40)

        for item in self.orders:
            print(f"{item[0]} x {item[1]} = ₹{item[2]}")

        print("-" * 40)
        print(f"Food Total     : ₹{self.total}")
        print(f"Packing Charge : ₹{packing_charge}")
        print(f"Grand Total    : ₹{self.total + packing_charge}")
        print("=" * 40)


class Customer(FoodCourt):
    pass


obj = Customer()
obj.order()