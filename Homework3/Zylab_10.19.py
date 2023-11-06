#Joshua Guajardo   PSID:1811892


class ItemToPurchase:
    def __init__(self, item='none', price=0, quantity=0, description='none'):
        self.item_name = item
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def cost_per_item(self):
        total_cost = 0
        total_cost = self.item_price * self.item_quantity
        return total_cost

    def print_item_cost(self):
        total_item = self.cost_per_item()
        print(f'{self.item_name} {self.item_quantity:.0f} @ ${self.item_price:.0f} = ${total_item:.0f}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, cust_name='none', current_date='January 1, 2016'):
        self.customer_name = cust_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_item:
            if item.item_name == item_name:
                self.cart_item.remove(item)
                return
            else:
                print('Item not found in cart. Nothing removed')

    def modify_item(self, item):
        for i in range(len(self.cart_items)):
            if self.cart_item[i].item_name == item.item_name:
                self.cart_item[i].item_quantity = item.item_quantity
                return
            else:
                print('Item not found in cart. Nothing is modified.')

    def get_num_items_in_cart(self):
        number_of_items = 0
        for i in self.cart_items:
            number_of_items += i.item_quantity
        return number_of_items

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_quantity * i.item_price
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print('Shopping cart is empty')
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f'Number of Items: {self.get_num_in_cart()}')
            cost = self.get_cost_of_cart()
            for i in self.cart_items:
                i.print_item_cost()
            print(f'Total: ${cost}')

    def print_description(self):
        if len(self.cart_items) == 0:
            print('Shopping cart is empty')
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print('Item Description')
            for i in self.cart_items:
                i.print_item_description()



def print_menu(shop_cart):
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print('o - Output shopping cart')
    print('q - Quit')
    print()

def main():
    print("Enter customer's name:")
    cust_name = input()
    print("Enter today's date:\n")
    today_date = input()
    print('Customer name:', cust_name)
    print("Today's date:", today_date)
    print()

    shop_cart = ShoppingCart(cust_name, today_date)
    print_menu(shop_cart)
    while True:

        user_choice = input("Choose an option:\n")

        if user_choice == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)

            shop_cart.add_item(item)

        elif user_choice == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shop_cart.remove_item(item_name)

        elif user_choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(item_name, item_quantity == new_quantity)
            shop_cart.modify_item(item)

        elif user_choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shop_cart.print_descriptions()

        elif user_choice == "o":
            print("\nOUTPUT SHOPPING CART")
            shop_cart.print_total()

        elif user_choice == "q":
            break

if __name__ == "__main__":
    main()