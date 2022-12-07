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
    input_text = str(sys.argv[1])
    add_char = str(sys.argv[2])
    location = int(sys.argv[3])
    if len(sys.argv) == 5:
        fill = str(sys.argv[4])
    else:
        fill = 'f'
    
    temp = list(input_text)
    if fill[0].capitalize() == 'T':
        for i in range(len(temp) + location + 1):
            if i % location == 0:
                temp.insert(i, add_char)
        del temp[0]
        temp = ''.join(temp)

    else:
        temp.insert(location, add_char)
        temp = ''.join(temp)
    
    pyperclip.copy(temp)
    print(f'New Text: {temp}')

if __name__ == '__main__':
    
    add_text()