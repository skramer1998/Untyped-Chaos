from django.contrib.auth.models import User
class Account:

    def __init__(self, id, first, middle, last, email, phone, address):
        self.userID = id
        self.userName = first + " " + middle + " " + last
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address
        self.user = User.objects.create_user(self.userID, self.userEmail)
        # create an account in the user DB. No password at first default permissions for user are none individual
        # group status should be set with the flags "is_TA" in a later step.

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

