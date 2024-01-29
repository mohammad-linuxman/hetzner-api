### Interact with the Hetzner Cloud API and manage your servers


### Run Project

1. Clone project:
```
$ git clone https://github.com/mohammad-linuxman/hetzner-api.git
```


2. Change directory to project and create file named (personal_token.py ):
```
$ cd hetzner-api/
$ echo "api_token = 'YOUR_HETZNER_TOKEN' > personal_token.py"
```

3. Install requierments and run project
```
$ pip3 install hcloud
$ python3 hetzner_api.py
```


4. Result: 
   use one these tasks to run and enjoy ;)
```
$ python3 hetzner_api.py 
Choose an action:
1. List Servers
2. Power On a Server
3. Power Off a Server
4. Create a Server
5. Safe Delete a Server
Enter the number of your choice: 

```


### Create Alias (Optional)
To create a permanent alias in Linux, you  need to add the alias definition to one of your shell configuration files. 
The two most common shells are Bash and Zsh. Here are the steps for both:

For Bash:
```
$ echo "alias hetzner_api='cd /PATH_TO_CODE && python3  hetzner_api.py' " >> ~/.bashrc
$ source ~/.bashrc
```

For Zsh:
```
$ echo " alias hetzner_api='cd /PATH_TO_CODE && python3 hetzner_api.py' " >> ~/.zshrc
$ source ~/.zshrc
```





### Find other Datacenter IDs:
```
$curl -H "Authorization: Bearer $API_TOKEN"  "https://api.hetzner.cloud/v1/locations"
```

