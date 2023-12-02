file = open("filename.txt","r") #read text if the file exsict
file = open("filename.txt","w") # write in text
file = open("filename.txt","r+")#read and writebut file need to exist
file = open("filename.txt","w+")#read and writebut file need to exist
file = open("filename.txt","a")# append on file
file = open("filename.txt","a+")# append on file and read


#same thing but on binary

file = open("filename.txt","rb") #read binary text if the file exsict
file = open("filename.txt","wb") # write binRY in text
file = open("filename.txt","rb+")#read and write binarybut file need to exist
file = open("filename.txt","wb+")#read  and write binarybut file need to exist
file = open("filename.txt","ab")# append binary on file
file = open("filename.txt","ab+")# append on file and read binary