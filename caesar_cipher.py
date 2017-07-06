from sys import exit
import string
import pickle

def encode():
    #initialize lower and upper list
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxz'
    lower_list = list(string.ascii_lowercase)

    #take a string and a number to shift by
    plain_text = raw_input('Enter a string of alphabetical letters to encode:\n> ').lower()
    shift = int(raw_input('Enter a number to shift your message:\n> ')) % 26
    plain_list = list(plain_text)

    #encode using shift
    cipher_list = []
    for x in plain_text:
        if x == ' ':
            cipher_list.append(' ')
        elif (ord(x) + shift) <= 122:
            cipher_list.append(chr(ord(x) + shift))
        elif (ord(x) + shift) > 122:
            cipher_list.append(chr(ord(x) + shift - 26))
    
    #output to pickle file
    pickle_file = raw_input("Enter a name for your encoded file, it will automatically have a .pickle extension:\n> ") + ".pickle"
    with open(pickle_file, 'wb') as f:
        pickle.dump(cipher_list,f)
    print "Your message has been encoded and stored in %s" % pickle_file
def decode():
    #take pickle file name as input
    pickle_file = raw_input("Enter the name of the *.pickle file you want to decode:\n> ") + ".pickle"
    with open(pickle_file, 'rb') as f:
        cipher_list = pickle.load(f)
    print "%s successfully loaded." % pickle_file

    #bruteforce the cipher
    print "Preparing to brute-force ..."

    for x in range(1,26):
        temp_list = []
        for char in cipher_list:
            if char == ' ':
                temp_list.append(' ')
            elif(ord(char) + x) <= 122:
                temp_list.append(chr(ord(char) + x))
            elif(ord(char) + x) > 122:
                temp_list.append(chr(ord(char) + x - 26))
        print ''.join(temp_list)

if __name__ == "__main__":
    
    choice = raw_input("Are you looking to 'encode' or 'decode' a message?\n> ")

    if choice == 'encode':
        encode()
        exit(1)
    elif choice == 'decode':
        decode()
        exit(1)
    else:
        print "Not sure what you said, exiting ..."
        exit(1)
