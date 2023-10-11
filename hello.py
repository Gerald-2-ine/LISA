msg = "Hello world!"
print(msg)

a = 2 
b = 4
sum = a + b 
multiply = sum * b 
divide = multiply / a 
subtract = divide - b 

print(sum,'\n', multiply,'\n', divide,'\n', subtract)

name = "Monalisa"
age = 21
country = "Nigeria"
occupation = "Developer"

print("Name: ", name, "\n" "Age: ", age, "\n" "Country: ", country, "\n" "Occupation: ", occupation)
print(bool(a))

print(3>6)

print(multiply < subtract)

print(msg) if a > b & a == b else print('false')

pi = 3.142
radius = 1.3
height = 0.5

new_height = height * 100
new_radius = radius * radius
volume = 1/3 * (pi * new_height * new_radius)
pi_2 = 3.142 
radius_2 = 1.3
height_2 = 0.5

new_height_2 = height * 100
new_radius_2 = radius * radius
volume_2 = 1/3 * (pi * new_height * new_radius)

if volume > volume_2:
    print('first volume is greater with a value of: ', volume)   
else: print('second volume is greater with a value of: ', volume_2)

print('first volume is greater with a value of: ', volume) if volume > volume_2 else print('second volume is greater with a value of: ', volume_2)



