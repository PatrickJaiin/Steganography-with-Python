from PIL import Image
import hashlib
def ceasarcipher(text,flag):
    print("Enter the key2 (numeric): ")
    key = int(input())
    if flag == 1:
        key = -key
    result = ''
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        elif (char.isnumeric()):
            result += chr((ord(char) + key-48) % 10 + 48)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def ceasardecode(text):
    return ceasarcipher(text,1)

def vignerecipher(text,key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def vignerecipherdecode(text,key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) -
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipher(text):
    print(text)
    text=ceasarcipher(text,0)
    key = input("Enter the key1 (string): ")
    print("key1 is: ",key)
    key=generateKey(text,key)
    print("key1 is: ",key)
    text=vignerecipher(text,key)
    return text

def cipherdecode():
    text=decode()
    print(text)
    key = input("Enter the key1 (string): ")
    key=generateKey(text,key)
    print("key1 is: ",key)
    text=vignerecipherdecode(text,key)
    text=ceasardecode(text)
    return text
# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
 
        # list of binary codes
        # of given data
        newd = []
 
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd
 
# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
 
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1
 
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
 
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
# Encode data into image
def encode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
 
    data1 = input("Enter data to be encoded : ")
    data1=data1.upper()
    data=cipher(data1)
    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    newimg = image.copy()
    encode_enc(newimg, data)
 
    new_img_name = input("Enter the name of new image(with extension) : ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
 
# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
while(True):
# Main Function
    hashes=['d55c6310ac3ee125e40c674b5482c5cf88b9b3a6960aea31b53e9186d19b83c9','ecb4f54ba57ea81da68039fcce3e5d9a884aba18099724ddded9e431a141c16e']
    print("Hi, please login to continue:")
    print("Enter username:")
    username=input()
    if username=="admin":
        print("Enter password:")
        password=input()
        hashed_text=hashlib.sha256(password.encode('utf-8')).hexdigest()
        print("Hashed password is:",hashed_text)
        if hashed_text in hashes:
            a = int(input(":: Welcome to Steganography ::\n"
                                    "1. Encode\n2. Decode\n3. Exit\n"))
            if (a == 1):
                encode()
            
            elif (a == 2):
                final=cipherdecode()
                print("Decoded Word :  " + final)
            elif (a==0):
                break
            else:
                raise Exception("Enter correct input")
