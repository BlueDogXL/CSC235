## below code was generated with chatgpt with the input "write a python script that takes recipe ingredients input by the user and multiplies them by a number of batches"

# def get_ingredient_input():
#     """Prompts the user for ingredients and their quantities."""
#     ingredients = {}
#     print("Enter ingredients and quantities. Type 'done' when finished.")
    
#     while True:
#         ingredient = input("Enter ingredient (or 'done' to finish): ")
#         if ingredient.lower() == 'done':
#             break
#         quantity = input(f"Enter the quantity for {ingredient}: ")
        
#         # Store the ingredient and quantity in the dictionary
#         ingredients[ingredient] = quantity
        
#     return ingredients

# def multiply_ingredients(ingredients, batches):
#     """Multiply ingredient quantities by the number of batches."""
#     multiplied_ingredients = {}
    
#     for ingredient, quantity in ingredients.items():
#         try:
#             quantity_value = float(quantity)
#             multiplied_ingredients[ingredient] = quantity_value * batches
#         except ValueError:
#             print(f"Invalid quantity for {ingredient}: {quantity}. Please enter a valid number.")
#             multiplied_ingredients[ingredient] = quantity  # Keep original if invalid input
            
#     return multiplied_ingredients

# def main():
#     print("Welcome to the Recipe Multiplier!")
    
#     # Get the number of batches from the user
#     try:
#         batches = int(input("How many batches would you like to prepare? "))
#     except ValueError:
#         print("Invalid number of batches. Please enter an integer.")
#         return
    
#     # Get the ingredients input from the user
#     ingredients = get_ingredient_input()
    
#     # Multiply ingredients by the number of batches
#     multiplied_ingredients = multiply_ingredients(ingredients, batches)
    
#     # Print the results
#     print("\nYour ingredients for", batches, "batches are:")
#     for ingredient, quantity in multiplied_ingredients.items():
#         print(f"{ingredient}: {quantity}")

# if __name__ == "__main__":
#     main()

## end of chatgpt-generated code.

## i mean, it works, i guess. didn't run into any syntax errors at all.
## BUT you can only multiply recipes by whole numbers, so you can't halve a recipe. which is a pretty common use case when you're doing recipe math.
## below i've lightly modified the code myself to suit my needs.


def get_ingredient_input():
    # Prompts the user for ingredients and their quantities.
    ingredients = {}
    
    while True:
        ingredient = input("Enter an ingredient (or 'done' to finish): ")
        if ingredient.lower() == 'done':
            break
        quantity = input(f"Enter the quantity for {ingredient}: ")
        
        # Store the ingredient and quantity in the dictionary
        ingredients[ingredient] = quantity
        
    return ingredients

def multiply_ingredients(ingredients, batches):
    # Multiply ingredient quantities by the number of batches.
    
    multiplied_ingredients = {}
    
    for ingredient, quantity in ingredients.items():
        try:
            quantity_value = float(quantity)
            multiplied_ingredients[ingredient] = quantity_value * batches
        except ValueError:
            print(f"Invalid quantity for {ingredient}: {quantity}. Please enter a valid number.")
            multiplied_ingredients[ingredient] = quantity  # Keep original if invalid input
            
    return multiplied_ingredients

def main():
    print("Welcome to the Recipe Multiplier!")
    
    # Get the number of batches from the user
    try:
        batches = float(input("How many batches would you like to prepare? "))
    except ValueError:
        print("Invalid number of batches. Please enter an number.")
        return
    
    # Get the ingredients input from the user
    ingredients = get_ingredient_input()
    
    # Multiply ingredients by the number of batches
    multiplied_ingredients = multiply_ingredients(ingredients, batches)
    
    # Print the results
    print("\nYour ingredients for", batches, "batches are:")
    for ingredient, quantity in multiplied_ingredients.items():
        print(f"{ingredient}: {quantity}")

if __name__ == "__main__":
    main()