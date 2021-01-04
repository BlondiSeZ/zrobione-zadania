db = {
    "patryk" : '0000',
    "czarny" : 'bialy',
    "wojtek" : '6969',
    "kosa" : '9696',
    "ziomek" : '4242',
    "ciapa" : '1234'
}
while True:
    login = input("Login: ")
    password = input("Password: ")
    if password == db.get(login):
        if 'admin' != db.get(login):
            print("Logged in as a user ")
            break;
        else:
            print("Logged in as an admin ")
            break;
    else:
        print("incorrect password or login")