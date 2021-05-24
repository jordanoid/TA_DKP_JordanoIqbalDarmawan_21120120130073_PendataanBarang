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