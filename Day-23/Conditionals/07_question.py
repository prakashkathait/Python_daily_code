'''Coffee customization:
problem: Customize a coffee order: "Small","Medium",or "Large" with an option for "Extra shot" of espresso'''

order_size = "medium"
extra_shot = True 

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("order :",coffee)