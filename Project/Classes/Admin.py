class Admin:

    def __init__(self):
        """Constructor for Admin."""
        self.userName = ""
        self.ID = ""
        self.email = ""
        self.phone = ""
        self.address = ""

    def __createCourse__(self, course):
        # return data
        pass

    def __createAccount__(self, account):
        # return data
        pass

    def __modifyAccounts__(self, account):
        # return data
        pass

    def grantGroupStatus(user, groupName):
        if groupName == "TA" or groupName == "Instructor" or groupName == "Admin":
            user.user.group.add(groupName)
            user.user.save()
            print(user.userName + " has been added to "+ groupName)
            return True
        elif groupName == "Supervisor":
            print("admin accounts cannot add Supervisor status")
            return False
        else:
            print("that's not a group. the 4 groups are TA, Instructor, Admin, and Supervisor")
            return False


    def __sendAllNoti__(self, other):
        # return data
        pass

    def __seePrivateInfo__(self, other):
        # return data
        pass