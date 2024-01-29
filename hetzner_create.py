import requests
from personal_token import api_token


# Define server creation parameters
server_name = input("Enter Name of server: (default: test ): ") or "test"
server_server_type = input("Enter Flavor of server: (default: cx11 ): ") or "cx11"
server_location = input("Enter Location/Datacenter of server: (default: nbg1): ") or "nbg1"
server_image = input("Enter Image of server: (default: ubuntu-20.04): ") or "ubuntu-20.04"
server_ssh_keys = input("Enter your Public key: (default: id_rsa_me_pub): ") or "id_rsa_me_pub"


server_params = {
    "name": server_name,
    "server_type": server_server_type,
    "location": server_location,
    "image": server_image,
    "ssh_keys": [server_ssh_keys]
}

# Hetzner Cloud API endpoint for server creation
api_url = "https://api.hetzner.cloud/v1/servers"

# Make the API request to create the server
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

def main():
     response = requests.post(api_url, json=server_params, headers=headers)
     
     # Check the response
     if response.status_code == 200:
         print("Server created successfully!")
         print(response.json())
     else:
         print(f"Error creating server. Status code: {response.status_code}")
         print(response.text)

if __name__ == "__main__":
    main()


#######CX11
#1
#2 GB
#20 GB
#€0.005 / h
#€3.29
# / mo
#######CPX11
#2
#2 GB
#40 GB
#€0.006 / h
#€3.85
# / mo
#######CX21
#2
#4 GB
#40 GB
#€0.008 / h
#€4.85
# / mo
#######CPX21
#3
#4 GB
#80 GB
#€0.011 / h
#€7.05
# / mo


# To find Datacenter ID:
#curl -H "Authorization: Bearer $API_TOKEN"  "https://api.hetzner.cloud/v1/locations"
