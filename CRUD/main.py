import sys


clients = [
    {
        "name": "Pablo",
        "company": "Google",
        "email": "pablo@google.com",
        "position": "Software Engineer",
    },
    {
        "name": "Ricardo",
        "company": "Facebook",
        "email": "ricargo@facebook.com",
        "position": "Data Engineer",
    }
]


def add_client(client):
    global clients

    if client not in clients:
        clients.append(client)
        print("")
        print("Client Created".center(50, "*"))

    else:
        print("")
        print("The client {} was already created".format(
            client).center(50, "*"))

# all clients


def list_clients():

    for idx, client in enumerate(clients):
        print("")
        print("Idx | Name | Company | Email | Position")
        print("")
        print("{uid} | {name} | {company} | {email} | {position}".format(

            uid=idx,
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"],
        ))
        print("".center(50, "="))


def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _update_client(client):
    global clients

    for idx, client in enumerate(clients):

        if idx in clients:
            clients.pop(idx)
            client = {
                "name": _get_client_field("name"),
                "company": _get_client_field("company"),
                "email": _get_client_field("email"),
                "position": _get_client_field("position")
            }
            clients.append(client)
            print("")
            print("Update Client".center(50, "*"))
            print("")
            list_clients()
        else:
            print("")
            print("The client does not exist")


def delete_client(client_name):

    if client_name in clients:
        clients.remove(client_name)
        print("")
        print("Client Removed".center(50, "*"))

    else:
        print("")
        print("The client {} is not in clients list".format(
            client_name).center(50, "*"))

# get client name


def _get_client_field(field_name):
    field = None

    while not field:
        field = input("What is the client {}? : ".format(field_name))

    return field


def _get_client_name():
    client = None

    while not client:
        client = input("What is the client name? ")

        if client == "exit":
            client_name = None
            break

    if not client:
        sys.exit()
    return client


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
# command lines

        if command == "C":
            print("CREATE CLIENT".center(50, "="))
            print("")

            client = {
                "name": _get_client_field("name"),
                "company": _get_client_field("company"),
                "email": _get_client_field("email"),
                "position": _get_client_field("position"),

            }
            add_client(client)
            list_clients()

        elif command == "U":
            print("UPDATE CLIENT".center(50, "="))
            print("")

            client = {
                "name": _get_client_field("name"),
            }
            _update_client(client)

        elif command == "L":
            print("LIST CLIENT\'S".center(50, "="))
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

# print welcome message


if __name__ == "__main__":
    print("WELCOME TO PLATZI VENTAS".center(50, "="))
    run()

# Santiago Gomez Florez
