import pymysql #SQL interface library
connection = pymysql.connect(host='[redacted]', #details for server connection
                             user='[username]', #put your name here
                             password='[password]', #put your name here
                             db='[redacted')

userGroup = 0 #to be used when a user posts a message

#gets number of existing users
def getUserCount():
    try:
        with connection.cursor() as cursor: #we should only invoke cursor using connection.cursor()
            sql = """SELECT COUNT(*) FROM User"""
            cursor.execute(sql) #executes the sql statement
            result = str(cursor.fetchone()) #stores all the results into result
            result = int(''.join(x for x in result if x.isalnum()))
            return result            
            
    except:
        print("Something went wrong fetching data. Trying again.")
        getUserCount();

def getMessageCount():
    try:
        with connection.cursor() as cursor: #we should only invoke cursor using connection.cursor()
            sql = """SELECT COUNT(*) FROM Message"""
            cursor.execute(sql) #executes the sql statement
            result = str(cursor.fetchone()) #stores all the results into result
            result = int(''.join(x for x in result if x.isalnum()))
            return result     
            
    except:
        print("Something went wrong fetching data. Trying again.")
        getMessageCount();        
        
currentUserCount = getUserCount() #to be used on startup to know where to start new userIDs from
currentMessageCount = getMessageCount()

#main menu functions such as log in and create new account
def mainMenu():
    print("\nCurrent user count is: "+str(currentUserCount))
    print("1 - Log in")
    print("2 - Create account")
    choice = input("Please choose an option from the list above using the numbers: ").strip()
    if choice == "1":
        logIn()
    elif choice == "2":
        createAccount()
    else:
        print("There was an error with your request, returning to main menu...\n")
        mainMenu()
        

#handles log in functionality    
def logIn():
    username = input("\nEnter your username: ").strip()
    password = input("Enter your password: ").strip()
    authenticate(username, password)

def authenticate(username, password):
    sql = """SELECT `Group` FROM User WHERE Name=%s AND Password=%s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql,(username, password)) #executes the sql statement
            result = cursor.fetchone() #stores all the results into result
            result = str(result[0])
            result = ''.join(x for x in result if x.isalnum()) #removes special characters, leaving just the group name
            
            if result == "None":
                createJoinGroup(username, password)
            else:
                userGroup = result
                print("Welcome back to group " + result + " " + username +". Here are your messages and tasks:") #prints results
                
                sql = """SELECT `Owner` FROM User WHERE Name=%s AND Password=%s"""
                try:
                    with connection.cursor() as cursor: #invoke cursor using connection.cursor()
                        cursor.execute(sql,(username, password)) #executes the sql statement
                        result = cursor.fetchone() #stores all the results into result
                        result = str(result[0])
                        result = ''.join(x for x in result if x.isalnum()) #removes special characters, leaving just the group name
                        Owner = result #checks if user is owner of a group, 1 if yes, 0 if no
                    
                    
                except:
                    print("Something went wrong, please check your details and try again\n")
                    mainMenu()

                printMessages(userGroup, Owner, username, password)
    except:
        print("Something went wrong, please check your details and try again\n")
        mainMenu()

#account creation functionality
def createAccount():
    username = input("\nEnter your desired username: ").strip()
    if len(username) < 5:
        print("Username must be atleast 6 characters long")
        createAccount()
    password = input("Enter your  desired password: ").strip()
    if len(password) < 5:
        print("Password must be atleast 6 characters long")
        createAccount()
    sql = """SELECT Name FROM User WHERE Name = %s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql, (username)) #executes the sql statement
            result = cursor.fetchall() #stores all the results into result
            
    except:
        print("Something went wrong")
        mainMenu()
    if len(result) == 0:
        sql = """INSERT INTO User (`UserID`, `Name`, `Password`) VALUES (%s, %s, %s)"""
        try:
            with connection.cursor() as cursor: #invoke cursor using connection.cursor()
                cursor.execute(sql, (currentUserCount+1, username, password)) #executes the sql statement
                connection.commit()
                print("You are now able to log in")
                mainMenu()
            
        except:
            print("Something went wrong")
            mainMenu()
        
    else:
        print("That username is already taken")
        createAccount()

#prints the user's messages upon logging in
def printMessages(userGroup, Owner, username, password):
    sql = """SELECT * FROM Message WHERE `Group`=%s AND Complete=%s """
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql, (userGroup,0)) #executes the sql statement
            result = cursor.fetchall() #stores all the results into result
            for x in result:
                print("Message " + str(x[0]) +": " + x[2])
            print("")
            if Owner == "1":
                print("1 - Post a message")
                print("2 - Delete a message")
                print("3 - Delete the group")
                print("9 - Log out")
            else:
                print("1 - Post a message")
                print("2 - Delete a message")
                print("9 - Log out")
            choice = input("Please choose an option from the list above using the numbers: ").strip()
            
            if choice == "1":
                postMessage(username, password)
            elif choice == "2":
                deleteMessage(username, password)
            elif choice == "3" and Owner == "1":
                deleteGroup(userGroup, username, password)
            elif choice == "9":
                mainMenu()
            else:
                print("Something went wrong, please check your input and try again\n")
                mainMenu()
    except:
        print("Something went wrong, please check your details and try again\n")
        mainMenu()
    

#create/join group functionality
def createJoinGroup(username, password):
    choice = input("Please enter a group name to join/create, if the group does not exist you will create it: ").strip()
    
    if len(choice) < 5:
        print("Group name must be at least 6 characters long")
        createJoinGroup(username, password)
        
    sql = """UPDATE User SET `Group` = %s WHERE Name = %s AND Password = %s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql, (choice, username, password)) #executes the sql statement
            connection.commit()
    except:
        print("Something went wrong")
        mainMenu()

    sql = """SELECT COUNT(*) from User WHERE `Group` =%s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql, (choice)) #executes the sql statement
            result = cursor.fetchone()
    except:
        print("Something went wrong")
        mainMenu()
    if result[0] == 1:
        sql = """UPDATE User SET Owner = 1 WHERE Name = %s AND Password = %s"""
        try:
            with connection.cursor() as cursor: #invoke cursor using connection.cursor()
                cursor.execute(sql, (username, password)) #executes the sql statement
                connection.commit()
                print("Group created")
                mainMenu()
        except:
            print("Something went wrong")
            mainMenu()        

def postMessage(username, password):
    sql = """SELECT `Group` FROM User WHERE Name=%s AND Password=%s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql,(username, password)) #executes the sql statement
            result = cursor.fetchone() #stores all the results into result
            result = str(result[0])
            result = ''.join(x for x in result if x.isalnum()) #removes special characters, leaving just the group name
            userGroup = result
    except:
        print("Something went wrong, please check your details and try again\n")
        authenticate(username, password)

    sql = """SELECT `userID` FROM User WHERE Name=%s AND Password=%s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql,(username, password)) #executes the sql statement
            result = cursor.fetchone() #stores all the results into result
            result = str(result[0])
            result = ''.join(x for x in result if x.isalnum()) #removes special characters, leaving just the group name
            userID = result
    except:
        print("Something went wrong, please check your details and try again\n")
        authenticate(username, password)        
 
    currentMessageCount = getMessageCount()
    firstmsg = str(strip(input("Please enter your message, leave it blank to return to the main menu: ")))
    message = str(firstmsg) + " - Left by " + (username)
    
    if message == "":
        mainMenu()
    else:

        sql = """INSERT INTO Message (`MessageID`, `UserID`, `Message`, `Group`, `Complete`) VALUES (%s, %s, %s, %s, %s);"""
        try:
            with connection.cursor() as cursor: #invoke cursor using connection.cursor()
                cursor.execute(sql,(currentMessageCount+1, userID, message, userGroup, 0)) #executes the sql statement
                connection.commit()
                authenticate(username, password)
            
        except:
            print("Something went wrong, please check your details and try again\n")
            authenticate(username, password)       
        
        

def deleteMessage(username, password):
    sql = """SELECT `Group` FROM User WHERE Name=%s AND Password=%s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql,(username, password)) #executes the sql statement
            result = cursor.fetchone() #stores all the results into result
            result = str(result[0])
            result = ''.join(x for x in result if x.isalnum()) #removes special characters, leaving just the group name
            userGroup = result
    except:
        print("Something went wrong, please check your details and try again\n")
        authenticate(username, password)

    choice = input("Choose which message number to delete from above: ").strip()
    sql = """UPDATE Message SET Complete = 1 WHERE `Group` = %s AND MessageID = %s"""
    try:
        with connection.cursor() as cursor: #invoke cursor using connection.cursor()
            cursor.execute(sql,(str(userGroup), int(choice))) #executes the sql statement
            connection.commit()
            authenticate(username, password)
    except:
        print("Something went wrong, please check your details and try again\n")
        authenticate(username, password)    

def deleteGroup(userGroup, username, password):
    print("Are you sure? None of the group members will be able to see any existing messages")
    print("1 - Go back, this will return you to the main menu")
    print("2 - Delete group")
    choice = input("Please choose an option from the list above using the numbers: ").strip()
    if choice == "1":
        authenticate(username, password)     
    elif choice == "2":
        try:
            with connection.cursor() as cursor: 
                sql = """UPDATE User SET `Group` = NULL, Owner = NULL WHERE `Group` =%s"""
                cursor.execute(sql, (userGroup)) #executes the sql statement
                connection.commit()
                mainMenu()
                
        except:
            print("Something went wrong fetching data. Trying again.")
            getUserCount();        
    else:
        mainMenu()
        
mainMenu()
    
