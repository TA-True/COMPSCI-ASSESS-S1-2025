def rollindecypher(cypher, startshift, encodedmessage):
    currentshift = cypher.index(startshift)
    currentshift = cypher.index(startshift)#Index to convert letter to number
    cypherlen = len(cypher)
    msglen = len(encodedmessage)
    i = 0#ticking through the problems
    code = ""
    while i < msglen:#trickery to make sure it does not try to split a list
        code += encodedmessage[i]
        i += 1
    encodedmessage = code
    encodedmessage.split
    fibbogen = [1, 2, 3]#the starting numbers for the gen
    decoded = []
    i = 0
    while i < msglen:
        message = cypher.index(encodedmessage[i])
        fibbopend1 = message#storing the resultant value to insert into fibbogen
        gen1n = currentshift#the fibbogen is using the previous term and one other term in it's generator
        genlen = len(fibbogen)
        while gen1n > genlen:
            gen1n-= genlen
        gen1n -= 1
        gen1n = fibbogen[gen1n]
        message -= gen1n
        message += 1
        while message < (-1):
        while message < 0:#Not underflow
            message = cypherlen + message
        fibbopend2 = message#ALSO STORING
        fibbogen.append(fibbopend2)#updating the gen
        fibbogen.append(fibbopend1)
        currentshift = message
        if message > cypherlen:#Not overflow
            message -= cypherlen
        message = cypher[message]
        decoded.append(message)#adding result to decoded
        i+= 1
    #print("This is the generator history") This was bugtesting material
    #print(fibbogen) Used to figure out where the mirroring failed
    return decoded
def rollincypher(cypher, startshift, message):
    currentshift = cypher.index(startshift)
    cypherlen = len(cypher)
    message.split
    fibbogen = [1, 2, 3]
    encoded = []
    msglen = len(message)
    nextshift = 0
    i = 0
    while i < msglen:
        numberfied = cypher.index(message[i]) 
        gen1n = currentshift
        gen1n = currentshift#similar fibbonacci trickery
        genlen = len(fibbogen)
        while gen1n > genlen:
            gen1n-= genlen
        gen1n -= 1#genlen = fibbogen tags + 1 so removing the 1
        gen1n = fibbogen[gen1n]
        fibbogen.append(numberfied)#updating
        nextshift = numberfied
        numberfied += gen1n
        numberfied += gen1n#shifting the number
        while cypherlen < numberfied:
            numberfied -= cypherlen
        numberfied -= 1#len(cypher) does not align with the cypher[x] so this is realigning
        while numberfied < 0:
            numberfied = cypherlen+numberfied#no underflow
        result = cypher[numberfied]
        encoded.append(result)
        fibbogen.append(numberfied)
        currentshift = nextshift
        i += 1
    #print("This is the generator history")
    #print(fibbogen)
    return encoded
def scramblecypher(message, shift):
    msglen = len(message)
    msglen -= 1
    startingshiftee = msglen-shift
    message.split
    encoded = ["Encoded:"]
    if startingshiftee < 0:#deciding where to start
        startingshiftee = msglen-startingshiftee
    lastshiftee = startingshiftee-1#deciding when the last charactter to be shifted
    if lastshiftee < 0:#implementing intentional underflow
        lastshiftee = msglen
    while startingshiftee <= msglen:#going down from the starting shiftee to create the message
        encoded.append(message[lastshiftee])
        startingshiftee += 1
    if startingshiftee != lastshiftee:#if it is past the lastt number in the original message but not the shift,
        startingshiftee = 0
        while startingshiftee <= lastshiftee:
            encoded.append(message[lastshiftee])
            startingshiftee += 1
    return encoded
cypheraddition = "Null"#cypher creation process, makes loop work
cypher = []
possicypher = False
nontedious_cyper=  input("Do you want to have type the cypher in one go? Put 'Yes' if true: ")
if nontedious_cyper != "Yes":
    while cypheraddition != "COMPLETED":
        if len(cypheraddition) > 2 and cypheraddition != "Null":#explaining why things don't get entered
            print("The cypher can only take in single characters")
        elif cypheraddition == " " or cypheraddition == "":#suggesting alternative
            print("The cypher breaks when spaces are used, it is recommended that you use '_' instead.")
        elif cypheraddition != "Null":#used to skip this step first time through
            if cypheraddition not in cypher:
                cypher.append(cypheraddition)
            else:
                print("Characters cannot appear twice in the cypher!")
    print('To stop the cypher creation process submit "COMPLETED" in all caps to the input question.')
    cypheraddition = input("What is the next letter/symbol you want to put into the cypher: ")
else:
    while possicypher == False:
        print("The cypher can only take in single characters")
        print("The cypher breaks when spaces are used, it is recommended that you use '_' instead.")
    print('To stop the cypher creation process submit "COMPLETED" inn all caps to the input question.')
    cypheraddition = input("What is the next letter/symbol you want to put into the cypher: ")
messagework = False
while messagework == False:
    message = input("What is the desired message to be encoded: ")
    messagework = True
    i = 0
    while i < len(message):
        if message[i] not in cypher:
            messagework = False
            print("Your message may only contain characters from the cypher.")
            print("The Cypher is made up of these characters: " + cypher)
        i += 1
startshift = "Null"
while startshift not in cypher:
    startshift = input("What would you like to have the rolling cypher start off with as a shift (choose a part of the cypher): ")
scrambled = input('Would you like to put the encoded message through a horizontal shift put "Yes" if you do: ')
encodedmsg = rollincypher(cypher, startshift, message)
print(encodedmsg)
print(cypher)
if scrambled == "Yes":
    horizshift = int(input("What number will you be shifting the message by? "))
    encodedmsg = scramblecypher(encodedmsg, horizshift)
decodedmsg = rollindecypher(cypher, startshift, encodedmsg)
i = 0
encodedstring = ""
while i < len(encodedmsg):
    encodedstring += encodedmsg[i]
    i += 1
print(encodedmsg)
decodedstring = ""
    scrambled = input('Would you like to put the encoded message through a horizontal shift put "Yes" if you do: ')
        message = encodedmsg
    known_start = input("Do you know the starting shift? Put the respective letter if yes: ")#to use if startshift is known
    if known_start in cypher:#uses startshift
        startshift = known_start
        decodedmsg = rollindecypher(cypher, startshift, message)
    else:#otherwise, brute force it
        print("The decoder will now try every single shift.")
        i = 0    
        while i < len(cypher):#go through each potential shift
            l = cypher[i]
            print(l)
            decodedmsg = rollindecypher(cypher, l, message)
            decodedstring = ""
            a = 0
            i +=  1
            while a < len(decodedmsg):
                decodedstring += decodedmsg[a]
                a += 1
            print(decodedstring)
            print("This was done with a shift of " + l +".")
if encoded == True:##increasing readability by converting list to string
    i = 0
    encodedstring = ""
    while i < len(encodedmsg):
        encodedstring += encodedmsg[i]
        i += 1
    print(encodedstring)
if decoded == True:#increasing readability by converting list to string
    decodedstring = ""
    i = 0
    while i < len(decodedmsg):
        decodedstring += decodedmsg[i]
        i += 1
    print(decodedstring)
i = 0
cypherstring = ""
while i < len(cypher):#increasing readability by converting list to string
    cypherstring += cypher[i]
    i += 1
print(cypherstring)