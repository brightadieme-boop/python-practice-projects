class Resturant:
    """A simple attempt to represent a resturant"""
    def __init__(self,name,type):
        """Initialize resturant name and cuisine type"""
        self.name = name
        self.type = type
    def describe_resturant(self):
        """Simulate resturant information"""
        print(f"Resturant name is {self.name} and its an {self.type} cuisine")
    def open_resturant(self):
        """Simulate openning of resturant"""
        print(f"The {self.name} resturant is now open")

the_resturant = Resturant('afrique','african')
the_resturant.describe_resturant()
the_resturant.open_resturant()
