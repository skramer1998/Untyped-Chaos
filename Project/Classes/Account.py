from django.contrib.auth.models import User
class Account:

    def __init__(self, id, first, middle, last, email, phone, address):
        self.userID = id
        self.userName = first + " " + middle + " " + last
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address
        self.user = User.objects.create_user(self.userID, self.userEmail)
        self.user.first_name = first
        self.user.last_name = last
        self.user.groups = None
        self.user.save()
        # create an account in the user DB. No password at first, default permissions for user are none, individual
        # group status should be set in a later step.

        # should return false if not set otherwise true

    def editPassword(self, newPassword):
        # Validate permissions before being able to call this function
        print("confirm new password: ")
        if newPassword == input():
            if not self.user.has_usable_password():
                self.user.set_password(newPassword)
                self.user.save()
                print("new password set")
            else:
                print("type current password for " + self.user.username)
                if self.user.check_password(input()):
                    self.user.set_password(newPassword)
                    self.user.save()
                    print("new password set")
                else:
                    print("wrong password for " + self.user.username)
        else:
            print("the new passwords don't match, start again from the begining.")


    def editSelf(self, name, id, email, phone, address):
        self.user.username = name
        self.user.userEmail = email
        self.userName = name
        self.userID = id
        self.userEmail = email
        self.userPhone = phone
        self.userAddress = address
        self.user.save()
        # should return false if not set otherwise true

    def publicInfo(self, name):
        return 0

