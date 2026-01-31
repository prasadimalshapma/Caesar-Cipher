# Coursework Assessment 1
# Name:Prasadi Malsha Abeysekara
# Student No:2502330

# A Caesar Cipher Program
import os.path

def welcome():
    # add your code here
    print("Welcome to the Caesar Cipher.\n This program encrypts and descrypts text using Caesar Cipher.")
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    # add your code here
    myarray=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mode=''
    
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d):").lower()
        if mode in ('e','d'):
            break
        
        print("Invalid input. Please enter 'e' or 'd'.")
        
    message=input("What message would you like to encrypt/decrypt:").upper()
    while True:
        try:
             shift=int(input("What is the shift number:"))
             break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
   
    return (mode, message, shift)


def encrypt(message,shift):
    # add your code here
    myarray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_word = ""
    for letter in message:
        if letter in myarray:
            shift_value=ord(letter)+shift
            if shift_value> ord('Z'):
                 shift_value= shift_value-26
            new_word=new_word +chr( shift_value)
        else:
            new_word=new_word+letter
    return new_word


def decrypt(message,shift):
    
    # add your code here
    myarray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_word = ""
    
    for letter in message:
        if letter in myarray:
            shift_value=ord(letter)-shift
            if shift_value<ord('A'):
                 shift_value= shift_value+26
            new_word=new_word +chr( shift_value)
        else:
            new_word=new_word+letter
    return new_word

        

def process_file(filename, mode,shift):
    list_messages = []
    # add your code here
    with open(filename,"r") as input_file:
        for line in  input_file:
            line=line.strip().upper()
            if mode=='e':
                list_messages.append(encrypt(line, shift))
            elif mode=='d':
                 list_messages.append(decrypt(line, shift))
                
              
    return list_messages


def write_messages(lines):
    # add your code here
    with open("results.txt","w") as output_file:
        for line in lines:
            output_file.write(line+"\n")
            
    print("Processed messages saved to 'results.txt'.")

    


def is_file(filename):
    import os
    return os.path.isfile(filename)


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    # add your code here
    while True:
        mode = input("Would you like to read from a file (f) or the console (c)?").lower()
        if mode in ('f','c'):
            break
        print("Invalid input. Please enter 'f' or 'c'.")
         

    if mode=='c':
         mode, message, shift = enter_message()
         
    elif mode=='f':
        while True:
              filename = input("Enter the filename to process: ")
              if is_file(filename):
                  break
              else:
                  print("Invalid Filename. Please enter a valid file name.")
                     
                  
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        shift = int(input("Enter your shift number: "))
         
         
         
    return (mode, message, filename, shift)
    
"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    # add your code here
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename is None:
            if mode=='e':
                 result = encrypt(message, shift)
            elif mode=='d':
                 result = decrypt(message, shift)

            print(f"Original message: {message}")
            print(f"Processed message: {result}")

        else:
            if mode in ('e','d'):
                lines=process_file(filename,mode,shift)
                write_messages(lines)

        while True:
             again=input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
             if again in ('y','n'):
                 break
             print("Invalid input. Please enter 'y' or 'n'.")
        if again == 'n':
            print("Thank you for using the program. Good bye!")
            break
            

       
        
       

        
                
# Program execution begins here
if __name__ == '__main__':
    main()
