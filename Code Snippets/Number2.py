# simple python login system

def login(users, username, password):
    for items in users:
        if username == items:
            if password == users[items]:
                return True
        else:
            return False


print(login({'user1' : 'password1', 'user2' : 'password2'}, 'user1', 'password1'))
