# Program Name: p56.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/22/2025
# Description: Deciphering "Caesar Cipher"
alphabet = ''
for i in range (65,91,1):
    alphabet += chr(i)
print('alphabet =', alphabet)
shift = 13 #cesear cipher = shift by 3
print('shift =', shift, 'letters')
encrypted = ''
for i in range (65,91,1):
    if i + shift < 91:
        encrypted += chr(i+shift)
    if i + shift >= 91:
        encrypted += chr(65 + (i+shift-91))
print('encrypted =', encrypted)

encrypt = { }
decypher = { }
encrypt  [ ' ' ] = ' '
decypher [ ' ' ] = ' '

for i in range (0, len(alphabet), 1):
    encrypt [ alphabet[i]  ] = encrypted[i]
    decypher[ encrypted[i] ] = alphabet [i]
original_message = input("Please type a message(ALL UPPER CASE): ")
encrypted_message = ''
for i in range(0, len(original_message),1):
    if original_message == ' ':
        encrypted_message += ' '
    else:
        encrypted_message += encrypt [ original_message [i] ]
print('Original Message: ', original_message)
print('Encrypt Message: ', encrypted_message)
print('...decyphered: ', end='')
for i in range (0, len(encrypted_message), 1):
    print(decypher [encrypted_message[i] ], end='')
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5b/p56.py
alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ
shift = 13 letters
encrypted = NOPQRSTUVWXYZABCDEFGHIJKLM
Please type a message(ALL UPPER CASE): CLGUBA VF TERNG
Original Message:  CLGUBA VF TERNG
Encrypt Message:  PYTHON IS GREAT
...decyphered: CLGUBA VF TERNG
'''
