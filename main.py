import sys
import mydbsave
from booking import BookRoom


class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.bookroom = BookRoom
        self.all_data = mydbsave.mycol
        self.choices = {
            "1": self.show_bookings,
            #"2": self.search_booking,
            "3": self.add_booking,
            #"4": self.modify_booking,
            "5": self.delete_booking,
            "6": self.quit
        }

    def display_menu(self):
        print(
            """
        Admin menu of Hostel
        1. Show all Bokings
        2. Search booking
        3. Add Booking
        4. Modify booking
        5. Delete booking     
        6. Quit
        """
              )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def show_bookings(self):
        for i in self.all_data.find():
            print(i)

    def add_booking(self):
        f_name = input("Please enter your first name: ")
        l_name = input("Please enter your last name: ")
        mail = input("please enter your email: ")
        room_size = input("Please enter the room size: ")
        days_stay = input("Please chose days of stay: ")

        self.bookroom(f_name, l_name, mail, room_size, days_stay)

    def search_booking(self):
        pass

    def modify_booking(self):
        pass


    def delete_booking(self):
        print("""1. Delete one
                 2. Delete all""")
        del_choice = input("Please chose: ")
        if del_choice == "1":
            del_choice_one = input("Please input email: ")
            myquery = {'male': del_choice_one}
            self.all_data.delete_one(myquery)
            print("User with {del_choice_one} was deleted")
        if del_choice == "2":
            self.all_data.delete_many({})
            print("all deleted")


    def quit(self):
        """
         To leave the menu
        """
        print("Thanks you for using your Booking")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()