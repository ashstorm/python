vehicles=['bike', 'moped', 'car', 'cycle']
print(vehicles)
print(vehicles[0])
print(vehicles[-1])
print("My first vehicle was a "+ vehicles[2].title()+".")
vehicles.append('tram')
vehicles.insert(2,'truck')
print(vehicles)
del vehicles[-1]
print(vehicles)
popped_vehicle=vehicles.pop()
print(vehicles)
print(popped_vehicle)
vehicles.append('quad')
print(vehicles)
vehicles.remove('quad')
print(vehicles)
