class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.ay7aga = gpa               ########################
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        var = self.ay7aga
        if self.gpa >= 3.5:
            return True
        else:
            return False