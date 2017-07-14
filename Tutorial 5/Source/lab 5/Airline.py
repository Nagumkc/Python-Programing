class Book():
    def make_reservation111(self, **kwargsns):
        raise NotImplementedError

class Air(Book):
    CLASS_BUS = 'Business Class'
    CLASS_FT = 'First Class'
    CLASS_PREMIUM_EC = 'Premium Economy'
    CLASS_Emy = 'Regular Economy'

    def __init__(self, air_name):
        super(Air, self).__init__()
        self.air_name= air_name
        self.seats = {
            self.CLASS_BUS: 50,
            self.CLASS_FT: 50,
            self.CLASS_PREMIUM_EC: 100,
            self.CLASS_Emy: 150,
        }
        self.prices = {
            self.CLASS_BUS: 2500,
            self.CLASS_FT: 2000,
            self.CLASS_PREMIUM_EC: 1800,
            self.CLASS_Emy: 1500,
        }

    def is_ava(self, booking_class):
        return self.seats[booking_class] > 0

    def make_res(self, booking_class):
        if self.is_ava(booking_class):
            self.seats[booking_class] -= 1
    def show(self,booking_class):
            print(booking_class,"seats left:",self.seats[booking_class],"prices:",self.prices[booking_class])

airline = Air("Quantas")
s=input("enter which type of booking")
booking_class = str(s)
airline.show(booking_class)