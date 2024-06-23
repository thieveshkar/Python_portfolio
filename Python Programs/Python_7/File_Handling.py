#Author: Thieveshkar
#Task :File_Handling Program

def read_file():
    while True:
        try:
            filename = input("Enter the File Name: ")
            File = open(filename, "r")
        except FileNotFoundError:
            print("The File doesn't exist so it will be created")
            File = open(filename, "w")
            File.close()
        else:
            File_Content = File.read()
            print(File_Content)
            File.close()
            return File_Content, filename

def write_to_file(File_Content, filename):
    while True:
        try:
            File = open(filename, "w")
        except FileNotFoundError:
            print("The File doesn't exist so it will be created")
            File = open(filename, "w")
        else:
            content = input("Enter what you want to enter into the file: ")
            File_Write = File.write(content)
            File.close()
            break

def read_lines():
    while True: 
        try:
            filename = input("Enter the File Name: ")
            File = open(filename, "r")
        except FileNotFoundError:
            print("File Not Found")
        else:
            File_Contents = File.readlines()
            print(File_Contents)
            File.close()
            break

File_Content, filename = read_file()
write_to_file(File_Content, filename)
read_lines()
