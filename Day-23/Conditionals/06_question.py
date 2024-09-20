''''Transportation mode Selection:
problem statement - Choose a mode of transportation based on the distance (eg. <3km: walk,
3-15km: Bike,
>15Km: Car)'''

distance = 15
if distance <3:
    activity ="Walk"
elif distance < 16:
    activity = "Bike"
else:
    activity = "Car"

print(activity)