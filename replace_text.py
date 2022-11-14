import pyperclip

# Inputs for the program
input_text = str(input('Input Text: '))
remove_char = str(input('Characters to Remove: '))
replace_char = str(input('Replacement Characters: '))

# Creates the output text using the replace function
output_text = input_text.replace(remove_char, replace_char)

# Outputs the new text string directly to the clipboard
pyperclip.copy(output_text)

# Outputs the text string to console
print(f'New text: {output_text}')