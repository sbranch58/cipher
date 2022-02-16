import random #for random.randrange() function 
import time
'''
Code
- reads a file and its pad to decrypt a message
- can encrypt a message with a pad 

'''
newfile = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

#ask the users if they want to encipher or decipher 
def ask():
    askCipher = input("Would you like to encrypt or decrypt? Type 0 for encrypt or 1 for decrypt ")
    if askCipher == '1':
        decipher() 
    elif askCipher == '0':
        encipher()
    else:
        print("Please input a 1 or a 0 ") 
        ask()
    

#makes string a list of letters/characters
def getChar(message):
    return [letter for letter in message]

#reads the file the user inputs
def readFile(filename):
    with open(filename, "r") as file:
        text = file.read() #reads file
        return text

#writes the message made in a file 
def writeMessage(message):
    with open("secret_" + newfile + ".txt", "a+") as file:
        file.write(message)
        file.close()

#writes pad into file (had to make two separate functions or else it wrote the pad and message all in one file)
def writePad(pad):
    with open("pad_" + newfile + ".txt", "a+") as file:
        file.write(pad)
        file.close()

#takes the lenof the message to make a pad of that length for the user to encrypt with
def generatePad(message):
    padNum = len(message)  
    pad = []
    while padNum != 0:
        num = random.randrange(65, 90, 1) #following capital letters for ascii code
        num = chr(num)
        pad.append(num)
        padNum -= 1

    letterPad = "".join(str(x) for x in pad) #turns the list into a string 
    print("The pad is: \n" + letterPad + "\n")
    writePad(letterPad)
    return letterPad




#deciphers the message by puttng the pad and message in a string, then list, and adding them together (had to have one to add the message differently if letters in message are uppercase or lowercase and same with the pad)
def decipher(): 
    message = input("Please input the message you would like to decipher: ")
    pad = input("Please input the pad: ")
    message = readFile(message)
    pad = readFile(pad)

    message = getChar(message)
    pad = getChar(pad)
    
    #print(message)
    for i in range(len(pad)): 
        pad[i] = ord(pad[i])
        #print(type(pad[i]))
    
    x = 0
    for i in range(len(message)): 
        message[i] = ord(message[i])
        #print(type(message[i]))

        if (message[i] >= 65) and (message[i] <= 90):
            if (pad[x] >= 65) and (pad[x] <= 90):
                message[i] = ((message[i] - 65) - (pad[x] - 65)) % 26 + 65 #need
                
            elif (pad[x] >= 97) and (pad[x] <= 122):
                message[i] = ((message[i] - 65) - (pad[x] - 97)) % 26 + 65
            
            x += 1

        elif (message[i] >= 97) and (message[i] <= 122):
            if (pad[x] >= 65) and (pad[x] <= 90):
                message[i] = ((message[i] - 97) - (pad[x] - 65)) % 26 + 97 #have to shift the pad and the message
                
            elif (pad[x] >= 97) and (pad[x] <= 122):
                message[i] = ((message[i] - 97) - (pad[x] - 97)) % 26 + 97

            x += 1 # increases pad by 1 separately from the message incase pad is longer than the message

        
    for a in range(len(message)): 
        message[a] = chr(message[a])
    #print(message)
    final_phrase = "".join(str(item) for item in message)
    print("The decrypted message is: \n" + final_phrase + "\n")
    writeMessage(final_phrase)

#encrypts the message by adding the ascii code pad woth the ascii code message
def encipher():
    message = input("Please input the file you would like to encode: ")
    message = readFile(message)
    askpad = input("Would you like to input a pad or make your own? Type 1 to make a pad or 0 to input your own ")
    if askpad == '1':
       newpad = generatePad(message)
    elif askpad == '0':
        newpad = input("Please input file path to pad: ")
        newpad = readFile(newpad)
    #print(message)
    #print(newpad)

    message = getChar(message)
    pad = getChar(newpad)
    
    #print(message)
    for i in range(len(pad)): 
        pad[i] = ord(pad[i])
        #print(type(pad[i]))
    
    x = 0
    for i in range(len(message)): 
        message[i] = ord(message[i])
        #print(type(message[i]))

        if (message[i] >= 65) and (message[i] <= 90):
            if (pad[x] >= 65) and (pad[x] <= 90):
                message[i] = ((message[i] - 65) + (pad[x] - 65)) % 26 + 65 #need
                
            elif (pad[x] >= 97) and (pad[x] <= 122):
                message[i] = ((message[i] - 65) + (pad[x] - 97)) % 26 + 65
            x += 1

        elif (message[i] >= 97) and (message[i] <= 122):
            if (pad[x] >= 65) and (pad[x] <= 90):
                message[i] = ((message[i] - 97) + (pad[x] - 65)) % 26 + 97 #the lowercase letters are off by 6
                #x += 1
            elif (pad[x] >= 97) and (pad[x] <= 122):
                message[i] = ((message[i] - 97) + (pad[x] - 97)) % 26 + 97
            x += 1

        
    for a in range(len(message)): 
        message[a] = chr(message[a])
    #print(message)
    final_phrase = "".join(str(item) for item in message)
    #writeMessage(final_phrase)
    print("The encrypted message is: \n" + final_phrase + "\n")
    writeMessage(final_phrase)
    #return final_phrase
    
#runs ask() function to run the rest of the programs/functions/prompt user
ask()



'''
Links/ Resources Used
list to string: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.
random.randrange() to get randome numbers: https://www.geeksforgeeks.org/random-numbers-in-python/
quotes inside quotes: https://cscircles.cemc.uwaterloo.ca/3-comments-literals/
string to list: https://pythonexamples.org/python-split-string-into-list-of-characters/ 
joining sentence together: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output
went to professor office hours to ask if input should be a file or string 
creating a new file to store message: https://stackoverflow.com/questions/31793549/new-file-name-each-time-python-run m
zip(): https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/ 


'''