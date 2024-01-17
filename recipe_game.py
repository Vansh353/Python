recipe_item = []

def add_to_recipe(recipe_id, recipe_name, recipe_type, recipe_desc):
    global recipe_item
    
    new_recipe = {
        "id": recipe_id,
        "name": recipe_name,
        "type": recipe_type,
        "desc": recipe_desc
    }
    recipe_item.append(new_recipe)
    print("Recipe Added Succesfully")
    
def update_recipe(recipe_id, recipe_name, recipe_type, recipe_desc):
    global recipe_item
    for recipe in recipe_item:
        if recipe['id'] == update_id:
            recipe['name'] = recipe_name
            recipe['type'] = recipe_type
            recipe['desc'] = recipe_desc
            print(f"Recipe with ID {update_id} updated successfully")
            return
    
    print(f"Recipe with ID {update_id} not found")
temp=1
while temp: 
        
    temp= int(input(" 0) Exit\n 1) Start \n"))  
    recipe_no = 1
    flag=1
    print("Welcome to Recipe App")
    if temp==1:

        while flag:
            recipe_functions = int(input("Recipe App Functions \n 1) Add Recipe \n 2) Update Recipe \n 3) Delete Recipe \n 4) View Recipe \n 5) Exit \n "))

            if recipe_functions == 1:
                recipe_function_id = recipe_no
                recipe_no+=1
                
                # For Inputting Name
                recipe_function_name = input("Enter the Recipe Name \n")
                
                # For Inputting Type
                recipe_function_type = input("Enter the Recipe Type \n")
                
                # For Inputting Desc
                recipe_function_desc = input("Enter the Recipe Description \n")
                
                add_to_recipe(recipe_function_id, recipe_function_name, recipe_function_type, recipe_function_desc)
            
            elif recipe_functions ==2:
                
                print("Enter the id you want to update: ")
                update_id=int(input())
                
                recipe_name_update=input("Enter New Name: ")
                
                
                recipe_type_update=input("Enter New Type: ")
                
                
                recipe_desc_update=input("Enter New Desc: ")
                
                update_recipe(update_id,recipe_name_update,recipe_type_update,recipe_desc_update)
                
            
            elif recipe_functions==3:
                
                print("Enter the id you want to delete: ")
                delete_id=int(input())
                
                for recipe in recipe_item:
                    if delete_id==recipe['id']:
                        recipe_item.remove(recipe)
                
                
            elif recipe_functions == 4:
                recipe_no1=1
                print("All Recipes:")
                
                for recipe in recipe_item:
                    recipe['id']=recipe_no1
                    recipe_no1+=1
                
                    print(f"ID: {recipe['id']}, Name: {recipe['name']}, Type: {recipe['type']}, Desc: {recipe['desc']}")
            
            elif recipe_functions==5:
                flag=0
        
    else:
        temp=0
            
    
    