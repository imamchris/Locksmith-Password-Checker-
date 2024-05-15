password = input() # input

print(len(password)) # length of password



# check if string contains specific character
def check_for_exclamation(password):
    for character in password:
        if character == "!":
            return True

# isalpha() - check for letters
# isupper() - checks for upper case

