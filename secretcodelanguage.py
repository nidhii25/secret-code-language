import random
import string

def secretCode():
    preference= input(" Type C for Coding and D for Decoding: ").strip().upper()

    if preference=='C' :
        #encoding starts
        message= input("Enter Message to Code:")
        dob= input("Enter your Date of Birth (format:DD)")
        words= message.split()

        encoded_msg= []
        for word in words:
            reverse= word[::-1]
        
            if len(word)>3:
                random_char= ''.join(random.choices(string.ascii_letters, k=3))
                new_word= dob+reverse+random_char
                encoded_msg.append(new_word)

            else:
                new_word= reverse
                encoded_msg.append(new_word)

        print(f"Your encoded message is:{" ".join(encoded_msg)}")
            

    elif preference== 'D':
        #decoding starts
        print("Format of message should be as follows for every word:\n1. For word length > 3: [DOB(DD)(message in reverse)(3 random characters)]\n 2. For word length <= 3: (reverse the word)")
        encoded_msg= input("Enter Message to Decode:")
        words= encoded_msg.split()

        decoded_msg= []
        for word in words:
            if len(word)>3:
                reverse_word= word[2:len(word)-3]
                    
                original_word= reverse_word[::-1]
                decoded_msg.append(original_word)
            else:
                original_word = word[::-1]
                decoded_msg.append(original_word)
        final_msg=" ".join(decoded_msg)
        print(f"your decoded msg is:{final_msg}")

    else:
        print("Invalid Input! Please restart and enter a valid input.")

    restart= input("Enter Yes if You want to resart the program.")
    if restart.lower()== "yes":
        secretCode()
    else:
        print("Goodbye!")

if __name__=="__main__":
    secretCode()

