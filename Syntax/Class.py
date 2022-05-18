class Stu:
    def __init__(self,id,seat):
        self.Id=id
        self.Seat=seat
    
    def show(self):
        print(f'My ID is {self.Id},and my seat is {self.Seat}')

Student=Stu(123,"3A2B")
Student.show() # My ID is 123,and my seat is 3A2B
