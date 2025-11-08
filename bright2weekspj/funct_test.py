def print_model(unprinted_design, completed_design):
  while unprinted_design:
     current_design = unprinted_design.pop()
     print(f"List of unprinted design:{current_design}")
     completed_design.append(current_design)

def show_completed(completed_design):
   print(f"\nList of completed model{completed_design}")
   for completed_designer in completed_design:
    print(completed_designer)

unprinted_design = ['moto', 'apple', 'sony', 'samsung'] 
completed_design = []
print_model(unprinted_design,completed_design)
show_completed(completed_design)

from funct_practice import make_album as ma
ma('artist','title')
    

    
