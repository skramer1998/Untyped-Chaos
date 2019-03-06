class Account:

    def __init__(self, name, id, email, phone, address):
        self.userName = name
        self.userID = id
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address

    def editSelf(self, name, id, email, phone, address):
        self.userName = name
        self.userID = id
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address

    def publicInfo(self, name):
        return 0
