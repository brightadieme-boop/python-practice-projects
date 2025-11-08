requested_food = ['turkey', 'yam', 'chicken', 'poundo', 'rice']
available_foods = ['turkey', 'yam', 'chicken','plantain']
for available_food in available_foods:
    if available_food in requested_food:
        print('adding', available_food.title(), 'to your order.')
    else:
        print('sorry ',available_food.title(), 'not available at the moment.')
