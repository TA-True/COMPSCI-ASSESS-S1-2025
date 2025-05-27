def rollindecypher(cypher, startshift, encodedmessage):
    currentshift = cypher.index(startshift)
    cypherlen = len(cypher)
    msglen = len(encodedmessage)
    i = 0
    code = ""
    while i < msglen:#trickery to make sure it does not try to split a list
        code += encodedmessage[i]
        i += 1
    encodedmessage = code
    encodedmessage.split
    fibbogen = [1, 1]
    encoded = []
    i = 0
    while i < msglen:
        message = cypher.index(encodedmessage[i])
        fibbopend1 = message#storing the resultant value to insert into fibbogen
        gen1n = currentshift
        genlen = len(fibbogen)
        while gen1n > genlen:
            gen1n-= genlen
        gen1n -= 1
        gen1n = fibbogen[gen1n]
        message -= gen1n
        message += 1
        while message < (-1):
            message = cypherlen - message
        fibbopend2 = message#ALSO STORING
        fibbogen.append(fibbopend2)
        fibbogen.append(fibbopend1)
        currentshift = message
        while message >= cypherlen:
            message-= cypherlen
        message = cypher[message]
        encoded.append(message)
        i+= 1
        print(str())
    return encoded
def rollincypher(cypher, startshift, message):
    currentshift = cypher.index(startshift)
    cypherlen = len(cypher)
    message.split
    fibbogen = [1, 1]
    encoded = []
    msglen = len(message)
    nextshift = 0
    i = 0
    while i < msglen:
        numberfied = cypher.index(message[i]) 
        gen1n = currentshift
        genlen = len(fibbogen)
        while gen1n > genlen:
            gen1n-= genlen
        gen1n -= 1
        gen1n = fibbogen[gen1n]
        fibbogen.append(numberfied)
        nextshift = numberfied
        numberfied += gen1n
        while cypherlen < numberfied:
            numberfied -= cypherlen
        numberfied -= 1
        result = cypher[numberfied]
        encoded.append(result)
        fibbogen.append(numberfied)
        currentshift = nextshift
        i += 1
    return encoded
def scramblecypher(message, shift):
    msglen = len(message)
    msglen -= 1
    startingshiftee = msglen-shift
    message.split
    encoded = ["Encoded:"]
    if startingshiftee < 0:
        startingshiftee = msglen-startingshiftee
    lastshiftee = startingshiftee-1
    if lastshiftee < 0:
        lastshiftee = msglen
    while startingshiftee <= msglen:
        encoded.append(message[lastshiftee])
        startingshiftee += 1
    if startingshiftee != lastshiftee:
        startingshiftee = 0
        while startingshiftee <= lastshiftee:
            encoded.append(message[lastshiftee])
            startingshiftee += 1
    return encoded
cypheraddition = "Null"
cypher = []
while cypheraddition != "COMPLETED":
    if cypheraddition != "Null":
        if cypheraddition not in cypher:
            cypher.append(cypheraddition)
        else:
            print("Numbers cannot appear twice in the cypher!")
    print('To stop the cypher creation process submit "COMPLETED" inn all caps to the input question.')
    cypheraddition = input("What is the next letter/symbol you want to put into the cypher: ")
message = input("What is the desired message to be encoded: ")
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
print(encodedmsg)
print(decodedmsg)