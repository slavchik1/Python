class School:
    total = 0

    def __init__(self, name):
        self.name = name
        School.total += 1

    @classmethod
    def show_total(cls):
        return cls.total


student = School("Mark")
student2 = School("Alex")
print(School.show_total())
