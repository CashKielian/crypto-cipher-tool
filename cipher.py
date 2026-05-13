# Asks the user for a message an a shift number
message = input("Enter a message to encrypt: ")
shift = input("Enter a secret shift number(1-10): ")

encrypted_messgae = ""

print("\n--- Running Cryptographic Encryption ---")

# Loop through every letter in the entered message by the user
for letter in message:
  # Checks if the character is an actual letter
  if letter.isalpha():
    # Shift the letter forward in the alphabet using its ASCII number value 
    # ord() converts a letter to a number, chr() converts it back 
    ascii_offset = 65 if letter.isupper() else 97
    shifted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
    encrypted_message += shifted_letter
  else:
    # If it's punctuation or a space, don't change it 
    encrypted_message += letter

print(f"🔒 Encrypted Secure Text: {encrypted_message}")

# --- Decryption Process ---
# Reverse - subtract backwards by subtracting the secret number
decrypted_message = ""

for letter in encrypted_message:
  if letter.isalpha():
    ascii_offset = 65 if letter.isupper() else 97
    unshifted_letter = chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
    decrypted_message += unshifted_letter
  else:
    decrypted_message += letter

print(f"🔓 Decrypted Original Text: {decrypted_message}")
