from datetime import datetime
from mydbsave import SaveDB


class Users:
    """
    Main information about clients
    """
    def __init__(self, f_name, l_name, mail):
        self.f_name = f_name
        self.l_name = l_name
        self.mail = mail


class BookRoom(Users):

    def __init__(self, f_name, l_name, mail, room_size, days_stay):
        super().__init__(f_name, l_name, mail)
        self.all_data = SaveDB
        self.room_size = room_size
        self.days_stay = days_stay
        booking_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.booking_date = booking_time

        self.all_data().save_db(self.f_name, self.l_name, self.mail, self.room_size, self.days_stay, self.booking_date)
