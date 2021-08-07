
def ceaser(text,key):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        elif(char.isdigit()):
            result += str(int(char) + key)
        elif(char == '-'):
            result += '-'
        elif (char.isspace()):
            result += " "
    return result
#check the above function
text = input("Enter your plain text:")
key = int(input("Enter the key:"))
print(ceaser(text,key))

    