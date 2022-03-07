from art import  logo;
import replit

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    new_text=""
    if(direction=="encode")or(direction=="decode"):
        for char in text:
            if char in alphabet:
                position=alphabet.index(char) 
                if(direction=="encode"):
                    encrypted_position=position+shift
                    if(encrypted_position>(len(alphabet)-1)):
                        encrypted_position= encrypted_position-(len(alphabet))
                        
                    letter_encrypted=alphabet[encrypted_position]  
                    new_text+=letter_encrypted
                elif(direction=="decode"):
                    descrypted_position=position - shift
                    
                    if(descrypted_position<0):
                        descrypted_position= len(alphabet) - (-1*descrypted_position)
                        
                    new_text+=alphabet[descrypted_position]
            else:
                new_text+=char
    
        print(f"The {direction}d text is {new_text}")
    else:
        print("Invalid Comand")

    awnser=input("Type 'yes' if you want to go again.Otherwise type 'no'\n")

    if(awnser=="yes"):
        replit.clear()
        caesar()
    else:
        print("Goodbye!")

caesar()
        
    
