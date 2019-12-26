import sys


clients = ["pablo", "ricardo", ]


def add_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
        print("")
        print("Client Created".center(50, "*"))

    else:
        print("")
        print("The client {} was already created".format(
            client_name).center(50, "*"))

#all clients
def list_clients():
    global clients

    print(clients)


def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _update_client(client_name):
    global clients

    if client_name in clients:
        update_name = str(input("What is the new client name? "))

        clients.remove(client_name)
        clients.append(update_name)
        print("")
        print("Update Client Name".center(50, "*"))

    else:
        print("")
        print("The client {} does not exist".format(
            client_name).center(50, "*"))

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
        print("")
        print("Client Removed".center(50, "*"))

    else:
        print("")
        print("The client {} is not in clients list".format(
            client_name).center(50, "*"))

#get client name

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("What is the client name? ")

        if client_name == "exit":
            client_name = None
            break

    if not client_name:
        sys.exit()
    return client_name


def run():
    while True:

        command = str(input("""
            What would you like to do today?

                [C]reate client
                [U]pdate client
                [L]ist clients
                [D]elete client
                [S]earch clients

                    [E]xit
        : """))

        command = command.upper()
#command lines
        if command == "C":
            print("CREATE CLIENT".center(50, "="))
            print("")

            client_name = _get_client_name()
            add_client(client_name)

            print("")
            list_clients()

        elif command == "U":
            print("UPDATE CLIENTt".center(50, "="))
            print("")

            client_name = _get_client_name()
            _update_client(client_name)

            print("")
            list_clients()

        elif command == "L":
            print("LIST CLIENT\'S".center(50, "="))
            print("")
            list_clients()

        elif command == "D":
            print("DELETE CLIENT".center(50, "="))
            print("")

            client_name = _get_client_name()
            delete_client(client_name)

            print("")
            list_clients()

        elif command == "S":
            print("SEARCH CLIENT".center(50, "="))
            print("")

            client_name = _get_client_name()
            found = search_client(client_name)

            if found:
                print("")
                print("The client: {} is in the client\'s list".format(client_name))
            else:
                print("")
                print("The client: {} is not in our client\'s list".format(client_name))

        elif command == "E":
            print("GOOD BYE".center(50, "="))
            print("")
            break

        else:
            print("Command invalid")

#print welcome message
if __name__ == "__main__":
    print("WELCOME TO PLATZI VENTAS".center(50, "="))
    run()

#Santiago Gomez Florez 