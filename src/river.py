class River:

    def __init__(self, name, fish):
        self.name = name
        self.fish = fish

    def get_fish(self):
        return self.fish.pop()

    def fish_count(self):
        return len(self.fish)
    