class Account:

    def __init__(self, id, first, middle, last, email, phone, address):
        self.userID = id
        self.userName = first + " " + middle + " " + last
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address

        # should return false if not set otherwise true

    def editSelf(self, name, id, email, phone, address):
        self.userName = name
        self.userID = id
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address

        # should return false if not set otherwise true

    def publicInfo(self, name):
        return 0
