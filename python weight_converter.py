#Weight conversion (Warning only this is approx)

unit = input ("Enter a unit Kg(Kilograms)/lb(Pounds): ")
if unit == "":
    print ("Sorry invalid input")
    exit()
weight = input ("Enter a weight: ")
if weight == "":
    print ("Sorry invalid input")
    exit()
weight_1 = float(weight)
if unit == "Kg":
    pounds = weight_1 * 2.205
    print (f"The weight in pound is {round(pounds, 2)} lb")
elif unit == "lb":
    weight = weight_1 * 0.453
    print (f"The weight in kilogram is {round(weight, 2)} kg")
    exit()