# intiate a class
class employee:
    #Class attributes - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}") 

# Create an instance of the class
sam = employee()

# Access the attributes of the class
print(sam.salary)

# Call the method of the class
sam.travel("New York")