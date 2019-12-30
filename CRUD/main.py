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
        print("Client already in client\'s list".center(50, "*"))

# all clients


def list_clients():

    for idx, client in enumerate(clients):
        print("")
        print("ID | Name | Company | Email | Position")
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
        if client["name"] != client_name:
            continue
        else:
            return True


def update_client(client_id, updated_client):
    global clients

    for idx in enumerate(clients):
        if idx == client_id:

            return True
        

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

# get client name


def _get_client_field(field_name, message= "What is the client {}?."):
    field = None

    while not field:
        field = input("What is the client {}? : ".format(field_name))

    return field


def _get_client_from_user():
    client = {
        "name": _get_client_field("name"),
        "company": _get_client_field("company"),
        "email": _get_client_field("email"),
        "position": _get_client_field("position"),
    }

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
            client = _get_client_from_user()

            add_client(client)
            list_clients()

        elif command == "U":
            print("UPDATE CLIENT".center(50, "="))
            list_clients()
            print("")
            client_id = int(_get_client_field("id"))

            while True:
                try:
                    updated_client = _get_client_from_user()
                    clients[client_id] = updated_client
                
                    update_client(client_id, updated_client)
                    list_clients()
                    break

                except IndexError: 
                    print("")
                    print("Client not in clien\'s list".center(50))
                    break

        elif command == "L":
            print("LIST CLIENT\'S".center(50, "="))
            list_clients()

        elif command == "D":
            client_id = int(_get_client_field("id"))

            delete_client(client_id)
            print("")
            list_clients()

        elif command == "S":
            print("SEARCH CLIENT".center(50, "="))
            print("")

            client_name = _get_client_field("name")
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
