class credential:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {"admin":"admin"}

    def check(self):
        for key in self.data:
            if key == self.username:
                if self.data[key] == self.password:
                    return True
                else:
                    return False
            else:
                return False

    def changeCredential(self, newUname, newPass):
        for key in self.data:
            self.data[newUname] =  self.data[key]
            del self.data[key]
        if newPass != "":
            self.data[newUname] = newPass