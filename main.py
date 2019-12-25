import sys

clients = ["pablo" , "ricardo",]


def add_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
        print("Client created")

    else:
        print("The client {} was already created".format(client_name))


def list_clients():
    global clients

    print(clients)


def update_client(client_name, update_name):
    global clients

    if client_name in clients:
        clients = clients.remove(client_name ,update_name)
        print("Update client name")
    else:
        print("The client {} does not exist".format(client_name))


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.pop()
        print("Client removed")

    else:
        print("The client {} is not in clients list".format(client_name))

def _get_client_name():
    return input("What is the client name? ")


def _print_welcome():

    print("")
    print("What would you like to do today?".center(50, "="))
    print("")
    print("[C]reate client".center(50))
    print("[U]pdate client".center(50))
    print("[D]elete client".center(50))
    print("[S]how clients".center(50))
    print("[E]xit".center(50))


if __name__ == "__main__":
    print("WELCOME TO PLATZI VENTAS".center(50, "="))

    while True:
        _print_welcome()

        comman = input(": ")
        comman = comman.upper()

        if comman == "C":
            client_name = _get_client_name()
            add_client(client_name)
            print("")
            list_clients()

        elif comman == "U":

            client_name = _get_client_name()
            print("")
            update_name = input("What is the new client name? ")

            update_client(client_name, update_name)
            list_clients()

        elif comman == "D":

            client_name = _get_client_name()
            delete_client(client_name)
            print("")
            list_clients()

        elif comman == "S":

            list_clients()

        elif comman == "E":
            break

        else:
            print("Command Invalid")

