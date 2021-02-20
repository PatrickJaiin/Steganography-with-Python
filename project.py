#made by The Collective
import numpy as np
from PIL import Image,UnidentifiedImageError

def cipher(data,key):
    result=""
    for i in range(len(data)):
        char=data[i]
        if (char.isupper()): 
            result += chr((ord(char) + key-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + key - 97) % 26 + 97) 
  
    return result 
    
def convert(ASCII):
    binary=[]
    for i in ASCII:
        x=ord(i)
        y='0'+bin(x)[2:]
        binary.append(y)
    return binary   
    
def modifier(pixel,asci):
    data=convert(asci)
    l=len(data)
    im=iter(pixel)
    for i in range(l):
        pixel = [value for value in im.__next__()[:3] +im.__next__()[:3] +im.__next__()[:3]]
        for j in range(0, 8):
            if (data[i][j] == '0' and pixel[j]% 2 != 0):
                pixel[j]=pixel[j]-1
 
            elif (data[i][j] == '1' and pixel[j] % 2 == 0):
                if(pixel[j] != 0):
                    pixel[j]=pixel[j]-1
                else:
                    pixel[j]=pixel[j]-1

        if (i == l - 1):
            if (pixel[-1] % 2 == 0):
                if(pixel[-1] != 0):
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
 
        else:
            if (pixel[-1] % 2 != 0):
                pixel[-1] -= 1
 
        pixel = tuple(pixel)
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]


def encode():
    img = input("Enter file name in format 'image.extension' : ")
    image = Image.open(img, 'r')
    k=int(input("Enter a numeric key"))
    dataold = input("Enter data to be hidden : ")
    data=cipher(dataold,k)
    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    newimg = image.copy()
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modifier(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
    new_img_name = "enc"+img
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def decode():

    name = input("Enter image name: ")

    try:
        img = Image.open(name, 'r')
    except FileNotFoundError:
        print("File doesn't exist")
    except UnidentifiedImageError:
        print("File is not an image")
    else:
        data = list(img.getdata())
        info = ""

        for idx in range(0, len(data), 3):
            l = data[idx] + data[idx+1] + data[idx+2]
            code = '0b'

            for i in range(8):
                if l[i] % 2 == 0:
                    code += '0'
                else:
                    code += '1'

            lettercode = int(code, 2)
            letter = chr(lettercode)
            info += letter

            if l[8] % 2 == 1:
                break

        return info
try:
    a = int(input("Enter your Choice:\n1. Encode\n2. Decode\n"))
    while (a!=0):
        try:
            if (a == 1):
                encode()

            elif (a == 2):
                x=decode()
                k=int(input("Enter the key: "))
                print("Decoded Word :  " + cipher(x,26-k))
            else:
                raise Exception("Enter correct input")
            a = int(input("Please make a choice:\n""1. Encode\n2. Decode\n"))    
        except:
            print("error plz try again")
            continue
except:
    print("error plz try again")   
         
