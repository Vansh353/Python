recipe_item = []

def add_to_recipe(recipe_id, recipe_name, recipe_type, recipe_desc):
    new_recipe = {
        "id": recipe_id,
        "name": recipe_name,
        "type": recipe_type,
        "desc": recipe_desc
    }
    recipe_item.append(new_recipe)
    print("Recipe Added Succesfully")
    
def update_recipe(recipe_id):
    for recipe in recipe_item:
        if recipe['id'] != recipe_id:
            print(f"Recipe with ID {recipe_id} not found")
            
        
        elif recipe['id'] == recipe_id:
            recipe_name=input("Enter New Name: ")
    
            
            recipe_type=input("Enter New Type: ")
            
        
            recipe_desc=input("Enter New Desc: ")
            recipe['name'] = recipe_name
            recipe['type'] = recipe_type
            recipe['desc'] = recipe_desc
            print(f"Recipe with ID {recipe_id} updated successfully")
            return
        
            
            

temp=1
while temp: 
        
    temp= int(input(" \n 0) Exit \n 1) Start \n Enter Value: "))  
    recipe_no = 1
    flag=1
    
    if temp==1:

        while flag:
            recipe_functions = int(input("\n Recipe App Functions \n\n 1)Add Recipe \n\n 2) Update Recipe \n\n 3) Delete Recipe \n\n 4) View Recipe \n\n 5) Exit \n Enter Value:"))
            print("Welcome to Recipe App")
            if recipe_functions == 1:
                recipe_function_id = recipe_no
                recipe_no+=1
                
                # For Inputting Name
                recipe_function_name = input("Enter the Recipe Name \n")
                
                # For Inputting Type
                recipe_function_type = input("Enter the Recipe Type \n")
                
                # For Inputting Desc
                recipe_function_desc = input("Enter the Recipe Description \n")
                
                add_to_recipe(recipe_function_id, recipe_function_name,recipe_function_type, recipe_function_desc)
            
            elif recipe_functions ==2:
                
                print("Enter the id you want to update: ")
                update_id=int(input())
                
                
                if len(recipe_item)==0:
                    print(f"Recipe with ID {update_id} not found")
            
                       
                update_recipe(update_id)
                
            
            elif recipe_functions==3:
                
                print("Enter the id you want to delete: ")
                delete_id=int(input())
              
                if len(recipe_item)==0:
                    print(f"Recipe with ID {delete_id} not found")
                # elif delete_id not in recipe_item:
                #     print("ID Not Found")
                    
                else:   
                    flag=0                 
                    for recipe in recipe_item:
                        if delete_id==recipe['id']:
                            flag=1
                            recipe_item.remove(recipe)
                            print(f"Recipe with ID {delete_id} deleted successfully")
                        
                            #update for loop
                            for recipe in recipe_item:
                                recipe['id']=recipe_no1
                                recipe_no1+=1
                            
                            break
                            
                    if flag!=1:
                        print("ID Not found!")
              
                    
                
                
                
            elif recipe_functions == 4:
                recipe_no1=1
                print("All Recipes:")
                
                for recipe in recipe_item:
                  
                
                    print(f"ID: {recipe['id']}, Name: {recipe['name']}, Type: {recipe['type']}, Desc: {recipe['desc']}")
            
            elif recipe_functions==5:
                flag=0
        
    else:
        break
            
    
    