class Automobile:

    def __init__(self):
        self.make = " "
        self.model = " "
        self.color = " "
        self.year = 0
        self.mileage = 0
        

    def add_vehicle(self):
        self.year = int(input("Enter year: "))
        self.make = input("Enter make: ")
        self.model = input("Enter model: ")
        self.color = input("Enter color: ")
        self.mileage = int(input("Enter mileage: "))

    def __str__(self):
        #made forematting adjustments for readability
        return('Year: %d\n Make: %s\n Model: %s\n Color: %s\n Mileage: %d\n' %
              (self.year, self.make, self.model, self. color, self.mileage))

vehicle_list = []

def edit(vehicle_list):
    pos = int(input('Enter the position of the vehicle to edit: '))
    new_vehicle = car.add_vehicle()
    new_vehicle = car.__str__()
    vehicle_list[pos-1] = new_vehicle
    print('Vehicle was updated')
    
user=True
while user:
    print ("""
    1.Add a Vehicle
    2.Delete a Vehicle
    3.View Inventory
    4.Update Inventory
    5.Export Inventory
    6.Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        car = Automobile()
        car.add_vehicle()
        vehicle_list.append(car.__str__())
     
    elif ans=="2":
        for i in vehicle_list:
            vehicle_list.pop(int(input('Enter position of vehicle to remove: ')))
            print('Successfully removed vehicle')
    elif ans=="3":
        #adjusted this slightly so that you can see the position of each vehicle. That way, if the end user wanted to delete a given vehicle, they would know what position to delete.
        print("\nThere are currently ", len(vehicle_list), " vehicles in the inventory:")
        i=0
        while i < len(vehicle_list):
            print('\nPosition: ', i, '\n',vehicle_list[i])
            i+=1
    elif ans=="4":
        edit(vehicle_list)
    elif ans=='5':
        f = open('vehicle_inv.txt', 'w')
        f.write(str(vehicle_list))
        f.close()
        #probably good to add a success comment e.g...
        print('Successfully wrote vehicle inventory to a text file in the working directory')
    #need to add condition to exit program if user enters '6. Quit'
    elif ans=='6':
        break
    else:
        print('try again')
         



