# import gooeypie as gp

# def get_upper(password):
#     uppers = []

#     for i in password:
#         if i.isupper():
#             uppers.append(i) 
#     return len(uppers)

# print(get_upper("Hs"))

import re

# Original string
original_string = "This is a [sample] string with (brackets) and {curly braces}."

# Regular expression pattern for characters to remove
remove_from_feedback = r"[\[\](){}]"

# Remove characters using re.sub()
cleaned_string = re.sub(remove_from_feedback, "", original_string)

print(cleaned_string)
