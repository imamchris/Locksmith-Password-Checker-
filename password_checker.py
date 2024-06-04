import gooeypie as gp
from random import choice
import re

# colours = ['',]
# fonts = ['',]
# styles = ['',]
   

def open_function(event): 
    start_btn.destroy()
    
    app.add(intro_lbl, 5, 25, align='left') # Text - Location: y, x (make sure it's within size of the Tab) - alignment

    app.set_grid(50, 50)
    app.add(ask_lbl, 7, 25, align='left')
    app.add(checker_inp, 10, 25)
    app.add(check, 11, 25, allign ='left') 
    app.add(verify_lbl, 12, 25, align='left')
    app.add(checker_btn, 13, 25, align='left')
    app.add(assist_btn, 1, 1)

def open_on_top_window(event):
    help_window.show_on_top()

def close_on_top_window(event):
    help_window.hide()

def has_special_characters(input_string): # NOTE Use of ChatGPT
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]') # Define the regex pattern for special characters
    return bool(pattern.search(input_string)) # Search for the pattern in the input string

def password_check(event):
    with open("100000-most-common-passwords.txt", "r") as file: # opens .txt file as a python list 
        # - NOTE May contain inappropiate words!
        password_list = file.read().splitlines()
    
    verify_lbl.text = ''
    password = checker_inp.text

    if password in password_list:
        verify_lbl.text = 'This password has a high risk of being breached'
    else:
        if len(password) <= 0: # password length
            verify_lbl.text = 'Please enter a password'
        elif len(password) >= 0 and len(password) <= 4:
            verify_lbl.text = 'Please make the password at least 5 characters long'
        elif password.isdigit() == True: # just digits
            verify_lbl.text = 'Try having more letters'
        elif password.isalpha() == True: # just letters
            verify_lbl.text = 'Try having more numbers'
        elif not has_special_characters(password): # no special characters
            verify_lbl.text = 'Try including a special character'
        else:
            verify_lbl.text = 'PERFECT'
    
    verify_lbl.update()


def toggle_mask(event):
    checker_inp.toggle()


app = gp.GooeyPieApp('Locksmith')

app.set_size(250, 250) 

# Main Tab

intro_lbl = gp.Label (app, 'Hello! Welcome to Locksmith!') # location, text
ask_lbl = gp.Label(app, 'Enter your password...')
verify_lbl = gp.Label(app, '')
checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 45
check = gp.Checkbox(app, 'Show Password')
check.add_event_listener('change', toggle_mask)
checker_btn = gp.Button(app, 'Check', password_check) # location, text, function
app = gp.GooeyPieApp('Other windows')
assist_btn = gp.Button(app, '?', open_on_top_window)


# Create other windows
help_window = gp.Window(app, 'On top window')
help_window.width = 300
help_txt = gp.Label(help_window, 'This is what you do...')
help_btn = gp.Button(help_window, 'Ok!', close_on_top_window)
help_window.set_grid(5, 5)
help_window.add(help_txt, 1, 1)
help_window.add(help_btn, 3, 1)

# Startup screen

start_btn = gp.Button(app, 'Ok!', open_function)

app.set_grid(50, 200) # Size of Tab

app.add(start_btn, 1, 1, align='left')

app.run()
