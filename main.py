from morse_alphabeth import MORSE_CODE_DICT

message = input("Write a message you want to convert to morse code. ").upper()

# Converts text input to morse code.
split_message = list(message)
morse_code = ""
for char in split_message:
    morse = MORSE_CODE_DICT[char]
    morse_code += morse

# Print morse code
print(f"Your message in morse code:\n{morse_code}")
