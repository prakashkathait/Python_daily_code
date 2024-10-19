n = int(input())  #no. of groups
rooms = list(map(int,input().split()))
actual_rooms = list(set(rooms))*n
difference = sum(actual_rooms) - sum(rooms)
print(int(difference/(n-1)))