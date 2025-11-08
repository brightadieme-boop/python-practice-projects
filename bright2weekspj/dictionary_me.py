car_race_game = {'postition_right': 0, 'position_left': 25 , 'speed': 'fast'}
print('original position: ',car_race_game['postition_right'])
if car_race_game ['speed'] == 'slow':
    increament_car = 1
elif car_race_game ['speed'] == 'medium':
    increament_car = 2
else:
    increament_car = 3
#fast car
car_race_game['postition_right'] = car_race_game['postition_right'] + increament_car
print('new position: ', car_race_game['postition_right'])




