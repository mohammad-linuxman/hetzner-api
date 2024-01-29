from hcloud import Client
from personal_token import api_token
client = Client(token=api_token)


def list_servers():
    servers = client.servers.get_all()
    for server in servers:
        print(f"Server ID: {server.id} , Name: {server.name} , Status: {server.status} ,  IP: {server.public_net.ipv4.ip}")

def power_on_server(server_id):
    server = client.servers.get_by_id(server_id)
    server.power_on()
    print(f"Server {server.name} is powering on.")

def power_off_server(server_id):
    server = client.servers.get_by_id(server_id)
    server.power_off()
    print(f"Server {server.name} is powering off.")

def main():
    print("Choose an action:")
    print("1. List Servers")
    print("2. Power On a Server")
    print("3. Power Off a Server")
    print("4. Create a Server")
    print("5. Safe Delete a Server")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        list_servers()
    elif choice == '2':
        server_id = input("Enter the ID of the server to power on: ")
        power_on_server(int(server_id))
    elif choice == '3':
        server_id = input("Enter the ID of the server to power off: ")
        power_off_server(int(server_id))
    elif choice == '4':
        import hetzner_create
        hetzner_create.main()
    elif choice == '5':
        import hetzner_safe_delete
        hetzner_safe_delete.main()
    else:
        print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
