import gooeypie as gp
import re


def open_function(event): # destroys the startup page and adds the password checker
    startup_txt.destroy()
    startup_btn.destroy()
    
    app.height = 400

    # margins=[5, 1, 5, 0], valign = 'middle'
    
    app.add(intro_lbl, 5, 1)
    app.add(ask_lbl, 6, 1)
    app.add(checker_inp, 8, 1, margins=[5, 0, 5, 15], valign = 'middle')
    app.add(checker_btn, 8, 2, margins=[5, 0, 5, 0], valign = 'middle')
    app.add(check, 9, 1)
    app.add(rating_lbl, 10, 1)
    app.add(status_lbl, 11, 1)
    app.add(assist_btn, 8, 3, margins=[5, 0, 5, 0], valign = 'middle') # margins[top, right, botton, left]
    app.add(copy_btn, 8, 4, margins=[5, 0, 5, 0], valign = 'middle')


def open_on_top_window(event): # opens the hekp window
    help_window.show_on_top()

def close_on_top_window(event): # closes the help window
    help_window.hide()


# Password Checking Functions

def get_letters(password): # checks for letters in the password
    letters = []

    for i in password:
        if i.isalpha():
            letters.append(i) 
    return len(letters)

def get_lower(password):
    lowers = []

    for i in password:
        if i.islower():
            lowers.append(i) 
    return len(lowers)

def get_upper(password):
    uppers = []

    for i in password:
        if i.isupper():
            uppers.append(i) 
    return len(uppers)


def get_digits(password): # checks for numbers in the password
    digits = []

    for i in password:
        if i.isdigit():
            digits.append(i) 
    return len(digits)


def get_special_char(password): # checks for any special characters
    types_str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    types = list(types_str) # NOTE: Use of ChatGPT 

    specials = []

    for i in password:
        if i in types:
            specials.append(i) 
    return len(specials)



def password_check(event):
    with open("100000-most-common-passwords.txt", "r") as file: # Opens the .txt file and puts it into a list
        password_list = file.read().splitlines()
    
    rating_lbl.text = '' # Text for password rating
    feedback = [] # Password feedback
    password = checker_inp.text
    password_rating = len(password)


    if password in password_list: # checks to see if the password is common
        rating_lbl.text = '0'
        feedback.append('This password has a high risk of being breached please change your password!')
    else:
        
        if len(password) <= 0: # checks if there's nothing in the input
            feedback.append("Please enter a password")    
        
        else:
            if get_letters(password) > 3:
                password_rating += 1

                if get_upper(password) > 2:
                    password_rating += 2
                else:
                    feedback.append("Try to include more captial letters")

                if get_lower(password) > 2:
                    password_rating += 2
                else:
                    feedback.append("Try to include more lowercase letters ")
            
            else:
                feedback.append("Try having more letters")

            if get_digits(password) > 3:
                password_rating += 3
            else:
                feedback.append("Try to include numbers ") 

            if get_special_char(password) > 3:
                password_rating += 2
            else:
                feedback.append("Try having more special characters ")

    if rating_lbl.text == '0':
        rating_lbl.text = ("Password security is: 0%")
    else:    
        rating_lbl.text = (f"Password security is: {round(password_rating / (len(password) + 6) * 100)}%") # Calculates how secure the password is base on the rating 
    
    status_lbl.text = (f"Feedback-\n{'\n'.join(feedback)}")

    rating_lbl.update()



def toggle_mask(event): # hides and shows the password
    checker_inp.toggle()



def copy_password(event):
    print("COPIED!!!")
    app.copy_to_clipboard(checker_inp.text)
    status_lbl.text = "Password copied"
    

# Main app window
app = gp.GooeyPieApp('Locksmith')
app.set_grid(50, 50)  # Sets the grid


# Main Tab
intro_lbl = gp.Label(app, 'Locksmith!')
ask_lbl = gp.Label(app, 'Enter your password...')
rating_lbl = gp.Label(app, '')
status_lbl = gp.Label(app, '')

checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 50

check = gp.Checkbox(app, 'Show Password')
check.add_event_listener('change', toggle_mask)

checker_btn = gp.Button(app, 'Check', password_check)


assist_btn = gp.Button(app, '?', open_on_top_window)
assist_btn.width = 3

copy_btn = gp.ImageButton(app, 'clipboard.png', copy_password, '')
copy_btn.width = 5


# Help Tab
help_window = gp.Window(app, 'On top window')
help_window.set_grid(50, 50)  # Sets the grid

help_txt = gp.Label(help_window, 'This is what you do...')
help_btn = gp.Button(help_window, 'Ok!', close_on_top_window)

help_window.add(help_txt, 1, 1)
help_window.add(help_btn, 3, 1)


# Startup Tab
startup_txt = gp.Label(app, 'Hello, Welcome to Locksmith... \nWe are here to help you create the most secure password as possible\nPlease Press Start to begin.')
startup_btn = gp.Button(app, 'Start', open_function)

app.add(startup_txt, 1, 1)
app.add(startup_btn, 3, 1)
app.width = 500

app.run()