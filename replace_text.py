import pyperclip, sys

def replace_text():
    # Inputs for the program
    input_text = str(input('Input Text: '))
    remove_char = str(input('Characters to Remove: '))
    replace_char = str(input('Replacement Characters: '))

    # Creates the output text using the replace function
    output_text = input_text.replace(remove_char, replace_char)

    # Copies new text to clipboard and outputs to console
    pyperclip.copy(output_text)
    print(f'New text: {output_text}')

def add_text():
    # Uses system arguments to access the script from a command line
    input_text = str(sys.argv[1])
    add_char = str(sys.argv[2])
    location = int(sys.argv[3])

    # Checks if a boolean is given to fill in characters throughout the text
    if len(sys.argv) == 5:
        fill = str(sys.argv[4])
    else:
        fill = 'f'
    
    # Fills in the input text with the supplied character based on the location variable
    temp = list(input_text)
    if fill[0].capitalize() == 'T':
        for i in range(len(temp) + location + 1):
            if i % location == 0:
                temp.insert(i, add_char)
        del temp[0]
        temp = ''.join(temp)

    # Adds in the add_char to the input text at the location variable space
    else:
        temp.insert(location, add_char)
        temp = ''.join(temp)
    
    # Copies the new text to the clipboard and outputs to console
    pyperclip.copy(temp)
    print(f'New Text: {temp}')

if __name__ == '__main__':
    # TODO Add in a choice menu to access other functions of this script
    add_text()