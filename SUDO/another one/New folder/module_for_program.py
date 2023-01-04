class testimony:
    def __init__(self, name, age, dept, gpa, coding_status):
        self.name = name
        self.age = age
        self.dept = dept
        self.gpa = gpa
        self.coding_status = coding_status

    def on_line(self):
        if self.coding_status >= 76:
            return True
        else:
            return False