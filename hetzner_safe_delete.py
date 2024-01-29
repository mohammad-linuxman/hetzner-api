import requests
from personal_token import api_token



# Define the Hetzner Cloud API URL
api_url = 'https://api.hetzner.cloud/v1/'

# Headers with Authorization
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# Function to get server details by name
def get_server_details(server_name):
    # Get list of servers
    response = requests.get(f'{api_url}servers', headers=headers)
    servers = response.json().get('servers', [])

    # Find the server by name
    server = next((s for s in servers if s['name'] == server_name), None)

    return server

# Function to delete server by ID
def delete_server_by_id(server_id):
    response = requests.delete(f'{api_url}servers/{server_id}', headers=headers)
    return response.status_code 
    #return response.status_code == 204  # 204 means successful deletion

server_name = input("Enter the server name: ")
server_id = input("Enter the server ID: ")

def main():
     server_details = get_server_details(server_name)
     
     if server_details and server_details['id'] == int(server_id):
         public_ip = server_details.get('public_net', {}).get('ipv4', {}).get('ip')
         
         print(f"Server Name: {server_details['name']}")
         print(f"Server ID: {server_details['id']}")
         print(f"Public IP: {public_ip}")
     
         confirm_deletion = input("Do you want to delete this server? (yes/no): ")
         
         if confirm_deletion.lower() == 'yes':
             #if delete_server_by_id(server_id):
             if 200  <=  delete_server_by_id(server_id)  <= 299 :
                 print(f"Server '{server_name}' with ID '{server_id}' deleted successfully.")
             else:
                 print(f"Failed to delete server '{server_name}' with ID '{server_id}'.")
         else:
             print("Deletion canceled.")
     else:
         print(f"Server with name '{server_name}' and ID '{server_id}' not found.")


if __name__ == "__main__":
    main()

