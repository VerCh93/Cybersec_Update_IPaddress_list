def update_file(ip_addresses, remove_ip_list):    #defining a function with two parameters
  with open(ip_addresses, "r") as file:           #reading initioal contents of a file
    imported_file = file.read()
  
  imported_file = imported_file.split()           #converting from string to list
  
  for ip in imported_file:                        #iterating through list
    if ip in remove_ip_list:                      #condition for matching ip addresses to be removed
      imported_file.remove(ip)
  
  new_ip_list = " ".join(imported_file)           #converting back to string
  
  with open(imported_file, "w") as file:          #rewriting file with new contents
    file.write(new_ip_list)

#calling the function with .txt file and a list of IP addresses to be removed
update_file("allowed_ip_addresses.txt", ["292.158.xxx.xxx", "292.768.xxx.xxx", "292.168.xxx.xxx"]) 

with open("allowed_ip_addresses.txt", "r") as file:     #reading the updated file
  updated = file.read()

#displaying contents of updated file
print(updated)