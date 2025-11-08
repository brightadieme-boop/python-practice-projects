name = input("what is your name ? ")
hour = input("how many hours did you sleep? ")
feel = input("how do you feel this morning? ")
print("hello " + name + "!" " you slept " + hour + " hours and you feel " + feel + " this morning" )

if float(hour) < 6:
    print("Try to get more rest tomorrow")