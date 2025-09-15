# This program will convert the weight on each planet


user_input = int(input("Hello, what is the weight you would like to convert?"))
weight_on_earth= user_input
# Planet  Relative

def space_converter():
 weight_mercury=  90
 weight_venus =   91
 weight_mars =    38
 weight_jupiter = 234
 weight_satum =   106
 weight_uranus =  92
 weight_neptune = 119
 weight_pluto =   6.3 


 weight_on_earth %weight_mercury 
 weight_on_earth % weight_venus 
 weight_on_earth % weight_mars
 weight_on_earth % weight_jupiter  
 weight_on_earth % weight_satum
 weight_on_earth % weight_uranus
 weight_on_earth % weight_neptune
 weight_on_earth % weight_pluto

 print(f"Mercury = {weight_on_earth %weight_mercury}")
 print(f"Venus = {weight_on_earth % weight_venus} ")
 print(f"Mars = {weight_on_earth % weight_mars}")
 print(f"Jupiter = {weight_on_earth % weight_jupiter}")
 print(f"Satum = {weight_on_earth % weight_satum}")
 print(f"Uranus = {weight_on_earth % weight_uranus}")
 print(f"Neptune = {weight_on_earth % weight_neptune}")
 print(f"Pluto = {weight_on_earth % weight_pluto}")
space_converter()