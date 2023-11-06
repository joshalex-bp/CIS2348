# Joshua Guajardo    PSID: 1811892



class FoodItem:
    # TODO: Define constructor with parameters to initialize instance
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    #       attributes (name, fat, carbs, protein)

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')


if __name__ == "__main__":
        item_name = input()
        amount_fat = float(input())
        amount_carbs = float(input())
        amount_protein = float(input())
        num_servings = float(input())

        i_name = 'None'
        f_amount = 0.00
        carbs_amount = 0.00
        protein_amount = 0.00
        food_item = FoodItem(i_name, f_amount, carbs_amount, protein_amount)
        food_item.print_info()
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(1.0):.2f}')



        print()

        food_item_2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item_2.print_info()
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item_2.get_calories(num_servings):.2f}')
