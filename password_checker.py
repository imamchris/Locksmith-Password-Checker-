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
    app.add(verify_lbl, 12, 25, align='left')
    app.add(checker_btn, 13, 25, align='left')
    app.add(assist_btn, 13, 26)

def open_on_top_window(event): # opens the hekp window
    help_window.show_on_top()

def close_on_top_window(event): # closes the help window
    help_window.hide()


def has_special_characters(input_string): 
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    return bool(pattern.search(input_string))

def password_check(event):
    with open("100000-most-common-passwords.txt", "r") as file: # Opens the .txt file and puts it into a list
        password_list = file.read().splitlines()
    
    verify_lbl.text = '' # Text for password feedback
    password = checker_inp.text

    if password in password_list: # checks to see if the password is common
        verify_lbl.text = 'This password has a high risk of being breached'
    else:
        if len(password) <= 0: # checks if there's nothing in the input
            verify_lbl.text = 'Please enter a password'
        elif len(password) >= 0 and len(password) <= 4: # checks if the password is too short
            verify_lbl.text = 'Please make the password at least 5 characters long'
        elif password.isdigit(): # checks for digits
            verify_lbl.text = 'Try having more letters'
        elif password.isalpha(): # checks for letter
            verify_lbl.text = 'Try having more numbers'
        elif not has_special_characters(password): # checks for special characters
            verify_lbl.text = 'Try including a special character'
        else:
            verify_lbl.text = 'PERFECT'
    
    verify_lbl.update()

def toggle_mask(event): # hides and shows the password
    checker_inp.toggle()



# Main app window
app = gp.GooeyPieApp('Locksmith')
# app.set_size(250, 250)
app.set_grid(100, 100)  # Sets the grid


# Main Tab
intro_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!')
ask_lbl = gp.Label(app, 'Enter your password...')
verify_lbl = gp.Label(app, '')
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