import random, pyperclip, string

# Initializes variables for different password requirements
pw_length = 12
special_min = 1
upper_min = 1
lower_min = 1
number_min = 1

# Sets up the dictionary of characters and associates their minimum amounts
comp = {
    'special':[special_min,'!@#$%&'],
    'upper':[upper_min, string.ascii_uppercase],
    'lower':[lower_min, string.ascii_lowercase],
    'number':[number_min, string.digits]
}

# Creates an empty list the size of the final password
password = ['' for i in range(pw_length)]

# Adds mandatory characters to the password list
for i in comp:
    for j in range(comp[i][0]):
        while True:
            rando = random.randint(0, pw_length-1)
            if password[rando] == '':
                password[rando] = random.choice(comp[i][1])
                break

# Fills in the remaining character slots with randomly selected characters
for space in range(len(password)):
    if password[space] == '':
        password[space] = random.choice(comp[random.choice(list(comp.keys()))][1])

# Converts the password list into a usable string
password = ''.join(password)

# Copies the password to the clipboard and outputs to console
pyperclip.copy(password)
print(f'Password created: {password}')
