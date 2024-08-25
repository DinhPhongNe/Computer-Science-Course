with open("name.txt", "a") as file:
    file.write("10")
    
try:
    file.open("grade.txt", "r")
    content = file.read
except FileNotFoundError:
    print("The file does not exist.")
finally:
    file.close()