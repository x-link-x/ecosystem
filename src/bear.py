

class Bear:
    
    def __init__(self, name, bear_type):
        self.name = name
        self.bear_type = bear_type
        self.stomach = []

        
    def bear_eats_fish(self, river):
        self.stomach.append(river.get_fish())

    def roar(self):
        return "ROOOOOAARRRRRR"

    def food_count(self):
        return len(self.stomach)
        
    
    
