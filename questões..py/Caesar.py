alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #25 (não conta com 0)
      
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
def caesar(text, shift, direction):
    end_text = ""
    for letter in range(len(text)):
        if direction == "encode":
            if (alphabet.index(text[letter]) + shift) > 25:
                diferrence = ((alphabet.index(text[letter]) + shift) - 25)
                end_text += alphabet[diferrence]                                   
            else:
                aux = alphabet[(alphabet.index(text[letter])) + shift]
                end_text += aux
                    
        elif direction == "decode":
               aux = alphabet[(alphabet.index(text[letter]) - shift)]
               end_text += aux          
            
    print(f"The {direction}  text is {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# shift = shift % 26
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
while True:
    caesar(text, shift, direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again == "no":
        break

    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        