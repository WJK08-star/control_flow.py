# This program will convert the weight on each planet


user_input = int(input("Hello, what is the weight you would like to convert?"))
weight_on_earth= user_input


def space_converter():
 weight_mercury=  0.38
 weight_venus =   0.91
 weight_mars =   0.38
 weight_jupiter = 2.34
 weight_satum =   1.06
 weight_uranus =  0.92
 weight_neptune = 1.19
 weight_pluto =   0.063 


 print(f"Mercury = {weight_on_earth * weight_mercury}lb")
 print(f"Venus = {weight_on_earth * weight_venus}lb")
 print(f"Mars = {weight_on_earth * weight_mars}")
 print(f"Jupiter = {weight_on_earth * weight_jupiter}lb")
 print(f"Satum = {weight_on_earth * weight_satum}")
 print(f"Uranus = {weight_on_earth * weight_uranus}lb")
 print(f"Neptune = {weight_on_earth * weight_neptune}lb")
 print(f"Pluto = {weight_on_earth * weight_pluto}lb")
space_converter()