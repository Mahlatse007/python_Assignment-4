#Create a program that reads a file and writes a modified version to a new file.
try:
    with open('ResearchTopics.txt', 'w') as file:
        file.write("The beginning of new IT concepts during Covid-19")

except FileNotFoundError:
    print("File Not Found")
finally:
    file.close()

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename = input("Please enter the file name : ")
try:
    with open(f'{filename}.txt', 'r') as file:
        print(file.read())

except FileNotFoundError:
    print("File Not Found")

finally:
    file.close()
