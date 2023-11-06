# Joshua Guajardo     PSID:1811892

class ItemToPurchase:
    def __init__(self, item='none', price=0, quantity=0):
        self.item_name = item
        self.item_price = price
        self.item_quantity = quantity

    def cost_per_item(self):
        total_cost = 0
        total_cost = self.item_price * self.item_quantity
        return total_cost

    def print_item_cost(self):
        total_item = self.cost_per_item()
        print(f'{self.item_name} {self.item_quantity:.0f} @ ${self.item_price:.0f} = ${total_item:.0f}')


if __name__ == "__main__":
    # Type main section of code here
    print('Item 1')
    item1_name = input('Enter the item name:\n')
    item1_price = float(input('Enter the item price:\n'))
    item1_quantity = int(input('Enter the item quantity:\n\n'))
    item_1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    print('Item 2')
    item2_name = input('Enter the item name:\n')
    item2_price = float(input('Enter the item price:\n'))
    item2_quantity = int(input('Enter the item quantity:\n\n'))
    item_2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    total_cost = item_1.cost_per_item() + item_2.cost_per_item()

    print('TOTAL COST')
    item_1.print_item_cost()
    item_2.print_item_cost()
    print()
    print(f'Total: ${total_cost:.0f}')