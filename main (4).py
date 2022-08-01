class Vehicle:
  def __init__(self, make, model, color):
    self.make = make
    self.model = model
    self.color = color
  
  def getMake(self):
      return self.make
  
  def getModel(self):
      return self.model

  def getColor(self):
      return self.color

class Car(Vehicle):
  def __init__(self, make, model, color, numDoors):
    Vehicle.__init__(self, make, model, color)
    self.numDoors=numDoors
  
  def numDoors(Self):
      return Self.numDoors

  def printDetails(self):
      print("Car Make: ",self.make)
      print("Car Model: ",self.model)
      print("Car Color: ",self.color)
      print("Car Number of Doors: ",self.numDoors)

class Pickup(Vehicle):
  def __init__(self, make, model, color, bedLength):
    Vehicle.__init__(self, make, model, color)
    self.bedLength=bedLength
  
  def bedLength(self):
      return self.bedLength

  def printDetails(self):
      print("Pickup Make: ",self.make)
      print("Pickup Model: ",self.model)
      print("Pickup Color: ",self.color)
      print("Pickup Bed Length: ",self.bedLength)

garage=[]
while(True):
    option = int(input("Enter \n1 for Car \n2 for Pickup \n3 for Exit \n"))
    if(option==1):
      make=input("Enter Car Make: ")
      model=input("Enter Car Model: ")
      color=input("Enter Car Color: ")
      numDoors=int(input("Enter Number of Doors: "))
      p=Car(make,model, color, numDoors)
      garage.append(p)
    elif(option==2):
      make=input("Enter Pickup Make: ")
      model=input("Enter Pickup Model: ")
      color=input("Enter Pickup Color: ")
      bedLength=int(input("Enter Pickup Bed Length: "))
      t=Pickup(make, model, color, bedLength)
      garage.append(t)
    else:
      break

print("Vehicle Details is: ")
print("---------------------------")
for v in garage: 
  print(v.printDetails())

print("Adrian Ybarra, Intro to Programming, 7.24.22")