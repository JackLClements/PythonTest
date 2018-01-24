# -*- coding: utf-8 -*-
"""
@author: Jack L. Clements
"""
import re
import os.path

class User: #Basic class representing a user, used to modify information where applicable
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def checkLogin(self, nUser, nPass):
        if nUser == self.username and nPass == self.password:
            return True
        else:
            return False
        
    def __str__(self): #mostly for debugging
        return self.username + ', ' + self.password
    
    def __repr__(self): #mostly for debugging
        return self.username + ', ' + self.password

def openDB(): #"Connects" to the database file, loading users into a list
    currentDir = os.getcwd()
    db = open(os.path.join(currentDir, 'PasswordDB.txt'), 'r+')
    userList = []
    entries = db.readlines() #list of users + passwords
    ps = re.compile(',')
    for i in range(len(entries)):
        testuser = ps.split(entries[i].strip())
        user = User(testuser[0], testuser[1])
        userList.append(user)
    db.close
    return userList

def closeDB(db): #Closes file
    currentDir = os.getcwd()
    file1 = open(os.path.join(currentDir, 'PasswordDB.txt'), 'w')
    for i in range(len(db)):
        file1.write(db[i].username + ',' + db[i].password + '\n') #Rewriting the "database" each time is not ideal, but without a language used to markup entires (SQL, etc.), this makes do
    file1.flush()
    file1.close()
    
def userExists(db, user): #Really ought to use hash table but done for time-efficiency, as this test does not need to scale
    for i in range(len(db)):
        if(db[i].username == user):
            return True
    return False

def login(db, username, password): #Returns a user object if their username + password are in database
    for i in range(len(db)):
        if(db[i].checkLogin(username, password)):
            return db[i]
    return None #This may be bad form, but is better than returning an incorrect object

def isIterativePass(password, nPassword): #Checks to see if new password is in form passwordn+1
    passwordList = list(password)
    nPasswordList = list(nPassword)
    if(int(passwordList[len(passwordList)-1])+1 == int(nPasswordList[len(nPasswordList)-1]) or password == nPassword): #note - casting is done to make integer operations available to check last value, to stop iteration
        return True
    else:
        return False
        

def register(username, db): #Registers a new user to the "database"
    pTest = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-\.]*)[a-zA-Z0-9_\-\.]*$')
    print username + ', please enter a password.'
    password = raw_input('Note - a password must contain at least one lowercase letter, one capital letter, one number and may contain the characters \, _ and - \n')
    password2 = raw_input('Please enter the password again for verification purposes: ')
    tries = 0
    while (password != password2 or bool(pTest.match(password)) != True) and tries < 3:
        tries += 1
        print 'Error - password does not match syntax. Please remember to include one lowercase and capital letter and one number.'
        password = raw_input('Please enter a new password: \n')
        password2 = raw_input('Please enter the password again for verification: \n')
        
    #use this check rather than if w/ recursion to save on stack space
    if tries >= 3:
        print 'You have reached the maximum amount of incorrect password attempts. User registration cancelled.'
    else:
        db.append(User(username, password))
        print 'Password set. User registered.'

def changePassword(db, username): #Changes a user's password
    pTest = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-\.]*)[a-zA-Z0-9_\-\.]*$')
    print username + ', please enter your old password.'
    password = raw_input('Please enter your old password: \n')
    userEntry = login(db, username, password) #returns memory location of user for rewriting later
    if(userEntry == None):
        print 'Incorrect old password.'
    else:
        nPassword = raw_input('Please enter a new password: \n')
        nPassword2 = raw_input('Please enter the password again for verification: \n')
        tries = 0
        while (nPassword != nPassword2 or bool(pTest.match(nPassword)) != True or isIterativePass(password, nPassword) == True) and tries < 3:
            tries += 1
            print 'Error - password does not match syntax. Please remember to include one lowercase and capital letter, one number and to not iterate passwords.'
            nPassword = raw_input('Please enter a new password: \n')
            nPassword2 = raw_input('Please enter the password again for verification: \n')
        userEntry.password = nPassword
        
        if tries >= 3:
            print 'You have reached the maximum amount of incorrect password attempts. Password change cancelled.'
        else:
            db.remove(userEntry)
            db.append(User(username, password))
            print 'Password set. User password changed.'
        

def main(): #rather than database that can modify specific entries, users are copies into program memory on the stack, uses more memory but saves on costly string ops, as no SQL
    db = openDB()
    username = raw_input('Please enter your username: \n')
    if(userExists(db, username)):
        changePassword(db, username)
    else:
        register(username, db)
    closeDB(db)

if __name__ == '__main__':
    main()