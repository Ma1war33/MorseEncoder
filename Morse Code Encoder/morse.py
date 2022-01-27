
#Function to turn text into morse code
def translate(x):
    #making all letters upper case
    x = x.upper()
    
    #creating dictionary
    global MORSE_CODE_DICT
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ',':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ':' ', #new 
                '@' : '.--.-.', "'" : '.----.', '"' : '.-..-.',
                '!' : '-.-.--', ':' : '---...', '&' : '.-...',
                '=' : '-...-', '%' : '------..-.-----', '+' : '.-.-.'}
    
    #replacing each letter with its morse code and adding a space between them
    msg = str()
    for i in x:
        msg = msg + MORSE_CODE_DICT[i]
        msg = msg + " "
            
    #returning the morse code
    return msg
        
#Function to turn morse code into text
def untranslate(x):

    #Creating dictionary
    MORSE_TO_TEXT = { '.-':'A', '-...':'B',
                '-.-.':'C', '-..':'D', '.':'E',
                '..-.':'F', '--.':'G', '....':'H',
                '..':'I', '.---':'J', '-.-':'K',
                '.-..':'L', '--':'M', '-.':'N',
                '---':'O', '.--.':'P', '--.-':'Q',
                '.-.':'R', '...':'S', '-':'T',
                '..-':'U', '...-':'V', '.--':'W',
                '-..-':'X', '-.--':'Y', '--..':'Z',
                '.----':'1', '..---':'2', '...--':'3',
                '....-':'4', '.....':'5', '-....':'6',
                '--...':'7', '---..':'8', '----.':'9',
                '-----':'0', '--..--':',', '.-.-.-':'.',
                '..--..':'?', '-..-.':'/', '-....-':'-',
                '-.--.':'(', '-.--.-':')', '  ':' ', ' ': '',
                '.--.-.' : '@', '.----.' : "'", '.-..-.' : '"',
                '-.-.--' : '!', '---...' : ':', '.-...' : '&',
                '-...-' : '=', '------..-.-----' : '%', '.-.-.' : '+'}

    #splitting sentance into words by splitting by a double space
    msg = str()
    x = x.split('  ')

    #repeat for the number of terms(words) in the list
    word = str()
    for i in range(len(x)):
        #splitting words into letters by splitting by a space
        p = x[i].split(' ')

        #removing empty terms in the list
        for j in p:
            if j == "":
                p.remove(j)

        #translating morse code into letters and putting them together into a word
        letters = str()
        for i in p:
            letters = letters + MORSE_TO_TEXT[i]

        #putting words into a sentance and adding a space between them
        word += letters + " "
        #makaing sentance all lowercase
        word.lower()
    
    #returning the sentance
    return word

