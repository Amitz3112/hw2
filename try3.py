MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }
text="hi i feel like i am going to die"
text=text.upper()
morse=text.translate(str.maketrans(MORSE_CODE))
separated_morse = morse.split()
separated_morse2="\n".join(separated_morse)
#     #Writing the morse code to the new file   
#print(separated_morse2)
#print(separated_morse2.count("\n"))
input_file = "lorem.txt"
with open(input_file, "r") as r:
        text_file = r.read()
separated=text_file.split()
#print(separated)
#print(len(separated))
separated2="\n".join(separated)
#print(separated2)
print(separated2.count("\n"))
#print(len(separated2))