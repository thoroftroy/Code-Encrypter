#this will attempt to translate english into code

def choose():
    crypt = input('Encrypt(0) or Decrypt(1) ')
    if(crypt == '0'):
        print('Encrypting')
        encrypt()
    elif(crypt == '1'):
        print('Decrypting')
        decrypt()
    else:
        print('No comprendo')
        choose()

def encrypt():
    string_name = input('Type message here:')
    cyfer = int(input('Cyfer Num:'))
    for element in range(0, len(string_name)):
        if(string_name[element] == ' '):
            print(0+cyfer)
        elif(string_name[element] == 'a') or (string_name[element] == 'A'):
            print(1+cyfer)
        elif(string_name[element] == 'b') or (string_name[element] == 'B'):
            print(2+cyfer)
        elif(string_name[element] == 'c') or (string_name[element] == 'C'):
            print(3+cyfer)
        elif(string_name[element] == 'd') or (string_name[element] == 'D'):
            print(4+cyfer)
        elif(string_name[element] == 'e') or (string_name[element] == 'E'):
            print(5+cyfer)
        elif(string_name[element] == 'f') or (string_name[element] == 'F'):
            print(6+cyfer)
        elif(string_name[element] == 'g') or (string_name[element] == 'G'):
            print(7+cyfer)
        elif(string_name[element] == 'h') or (string_name[element] == 'H'):
            print(8+cyfer)
        elif(string_name[element] == 'i') or (string_name[element] == 'I'):
            print(9+cyfer)
        elif(string_name[element] == 'j') or (string_name[element] == 'J'):
            print(10+cyfer)
        elif(string_name[element] == 'k') or (string_name[element] == 'K'):
            print(11+cyfer)
        elif(string_name[element] == 'l') or (string_name[element] == 'L'):
            print(12+cyfer)
        elif(string_name[element] == 'm') or (string_name[element] == 'M'):
            print(13+cyfer)
        elif(string_name[element] == 'n') or (string_name[element] == 'N'):
            print(14+cyfer)
        elif(string_name[element] == 'o') or (string_name[element] == 'O'):
            print(15+cyfer)
        elif(string_name[element] == 'p') or (string_name[element] == 'P'):
            print(16+cyfer)
        elif(string_name[element] == 'q') or (string_name[element] == 'Q'):
            print(17+cyfer)
        elif(string_name[element] == 'r') or (string_name[element] == 'R'):
            print(18+cyfer)
        elif(string_name[element] == 's') or (string_name[element] == 'S'):
            print(19+cyfer)
        elif(string_name[element] == 't') or (string_name[element] == 'T'):
            print(20+cyfer)
        elif(string_name[element] == 'u') or (string_name[element] == 'U'):
            print(21+cyfer)
        elif(string_name[element] == 'v') or (string_name[element] == 'V'):
            print(22+cyfer)
        elif(string_name[element] == 'w') or (string_name[element] == 'W'):
            print(23+cyfer)
        elif(string_name[element] == 'x') or (string_name[element] == 'X'):
            print(24+cyfer)
        elif(string_name[element] == 'y') or (string_name[element] == 'Y'):
            print(25+cyfer)
        elif(string_name[element] == 'z') or (string_name[element] == 'Z'):
            print(26+cyfer)
        elif(string_name[element] == '1'):
            print(27+cyfer)
        elif(string_name[element] == '2'):
            print(28+cyfer)
        elif(string_name[element] == '3'):
            print(29+cyfer)
        elif(string_name[element] == '4'):
            print(30+cyfer)
        elif(string_name[element] == '5'):
            print(31+cyfer)
        elif(string_name[element] == '6'):
            print(32+cyfer)
        elif(string_name[element] == '7'):
            print(33+cyfer)
        elif(string_name[element] == '8'):
            print(34+cyfer)
        elif(string_name[element] == '9'):
            print(35+cyfer)
        elif(string_name[element] == '10'):
            print(36+cyfer)
            
def listThing(message):
    messageA = input('First Num:')
    append(messagA,message)
def decrypt():
    cyfer = int(input('Cyfer Num:'))
    i = 0
    for i in list:
        if(message[i]-cyfer == '0'):
            print(A)
        elif(message[i]-cyfer == '1'):
            print(B)
        
choose()
