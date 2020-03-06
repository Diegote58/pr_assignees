import json

def getUsers():
        with open('models/users.json', 'r') as f:
            users = json.load(f)
        return users
    
def createUser(request):
    users = open("models/users.json", "r") # Open the JSON file for reading
    data = json.load(users) # Read the JSON into the buffer
    users.close() # Close the JSON file

    ## Working with buffered content
    last_user = data[-1]
    id = last_user['id'] + 1
    
    newUser = {"load": 0, "pr": [], "account": request.form['account'], "name": request.form['name'], "enabled": True, "id": id}
    data.append(newUser)
    ## Save our changes to JSON file
    update = open("models/users.json", "w+")
    update.write(json.dumps(data))
    update.close()

def updateUser(id):
    users = open("models/users.json", "r") # Open the JSON file for reading
    data = json.load(users) # Read the JSON into the buffer
    users.close() # Close the JSON file

    ## Working with buffered content
    for user in data:
        if user['id'] == id:
            if user['enabled'] == True:
                user['enabled'] = False
            else:
                user['enabled'] = True
            break
    
    ## Save our changes to JSON file
    update = open("models/users.json", "w+")
    update.write(json.dumps(data))
    update.close()
    
def deleteUser(id):
    users = open("models/users.json", "r") # Open the JSON file for reading
    data = json.load(users) # Read the JSON into the buffer
    users.close() # Close the JSON file

    ## Working with buffered content
    for user in data:
        if user['id'] == id:
            data.remove(user)
            break
    
    ## Save our changes to JSON file
    update = open("models/users.json", "w+")
    update.write(json.dumps(data))
    update.close()
    
def updateUserLoad(account, load):
    users = open("models/users.json", "r") # Open the JSON file for reading
    data = json.load(users) # Read the JSON into the buffer
    users.close() # Close the JSON file

    ## Working with buffered content
    for user in data:
        if user['account'] == account:
            user['load'] = user['load'] + load
        break

    ## Save our changes to JSON file
    update = open("models/users.json", "w+")
    update.write(json.dumps(data))
    update.close()