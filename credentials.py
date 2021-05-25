class credential:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check(self):
        file = open("login_info.txt", "r")
        uname_verify = file.readline()
        pass_verify = file.readline()
        if self.username+"\n" == uname_verify:
            if self.password == pass_verify:
                return True
            else:
                return False
        else:
            return False
        file.close()

def changeCredential(newUname, newPass):
    if newUname and newPass == "":
        pass
    else:
        file = open("login_info.txt", "w")
        file.write(newUname+"\n")
        file.write(newPass)
        file.close()