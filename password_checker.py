import gooeypie as gp
import re

def open_function(event): # destroys the startup page and adds the password checker
    startup_txt.destroy()
    startup_btn.destroy()
    
    app.height = 250

    app.add(intro_lbl, 5, 25, align='left')
    app.add(ask_lbl, 7, 25, align='left')
    app.add(checker_inp, 10, 25)
    app.add(check, 11, 25, align='left')  # Typo fixed: allign -> align
    app.add(rating_lbl, 12, 25, align='left')
    app.add(checker_btn, 13, 25, align='left')
    app.add(assist_btn, 13, 26)

def open_on_top_window(event): # opens the hekp window
    help_window.show_on_top()

def close_on_top_window(event): # closes the help window
    help_window.hide()


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
    
    rating_lbl.text = '' # Text for password feedback
    password = checker_inp.text
    password_rating = len(password)

    print(password_rating)

    if password in password_list: # checks to see if the password is common
        password_rating = 'This password has a high risk of being breached'
    
    else:
        
        if len(password) <= 0: # checks if there's nothing in the input
            password_rating = 'Please enter a password'
            print(password_rating)      
        
        else:
            if get_letters(password) > 3:
                password_rating += 1
                if get_upper(password) > 2:
                    password_rating += 2
                elif get_lower(password) > 2:
                    password_rating += 2

            if get_digits(password) > 3:
                password_rating += 3 

            if get_special_char(password) > 3:
                password_rating += 2

            rating_lbl.text = (f"Password security is: {password_rating / (len(password) + 6) * 100}%") # Calculates how secure the password is base on the rating 
    
    rating_lbl.update()

def toggle_mask(event): # hides and shows the password
    checker_inp.toggle()



# Main app window
app = gp.GooeyPieApp('Locksmith')
app.set_grid(100, 100)  # Sets the grid


# Main Tab
intro_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!')
ask_lbl = gp.Label(app, 'Enter your password...')
rating_lbl = gp.Label(app, '')
checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 45
check = gp.Checkbox(app, 'Show Password')
check.add_event_listener('change', toggle_mask)
checker_btn = gp.Button(app, 'Check', password_check)
assist_btn = gp.Button(app, '?', open_on_top_window)

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
app.width = 250

app.run()