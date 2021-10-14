import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


class SaveDB:
    def save_db(self, f_name, l_name, mail, room_size, days_stay, booking_date):
        self.data = {"f_name": f_name,
                     "l_name": l_name,
                     "email": mail,
                     "room_size": room_size,
                     "days_stay": days_stay,
                     "booking_date": booking_date}

        if self.data not in mycol.find():
            mycol.insert_one(self.data)

        for i in mycol.find():
            print(i)


