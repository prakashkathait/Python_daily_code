'''Fruit Ripeness checker 
Problem: Determine if a fruit is ripe, overripe or unripe based on its color.
(eg. Banana: Green -Unripe,
Yellow-Ripe,
Brown- Overripe)'''

fruit = "Banana"
color ={"Green": "Unripe",
        "Yellow": "Ripe",
        "Brown": "Overripe"}
fruit_color = input("Enter the fruit color: ")

if fruit_color == "Green":
    print(color[fruit_color])
elif fruit_color == "Yellow":
    print(color[fruit_color])
else:
    print(color["Brown"])