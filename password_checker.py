import gooeypie as gp
import time


def open_function(event): # destroys the startup page and adds the password checker
    # Destroy startup widgets
    startup_top_txt.destroy()
    startup_mid_txt.destroy()
    startup_bottom_txt.destroy()
    startup_btn.destroy()
    lock_img.destroy()

    app.refresh()
    app.add(loading_pb, 50, 2, column_span=30, fill=True)

    loading_pb.value = 0
    for i in range(20):
        loading_pb.value += 5
        app.refresh()
        time.sleep(0.05)
    
    loading_pb.destroy()
    app.refresh()

    # Add new widgets
    app.add(ask_lbl, 6, 1)
    app.add(checker_inp, 8, 1, margins=[5, 0, 5, 15], valign = 'middle')
    app.add(checker_btn, 8, 2, margins=[5, 0, 5, 0], valign = 'middle')
    app.add(check, 9, 1)
    app.add(rating_lbl, 10, 1)
    app.add(status_lbl, 11, 1)
    app.add(assist_btn, 8, 3, margins=[5, 0, 5, 0], valign = 'middle')
    app.add(copy_btn, 8, 4, margins=[5, 0, 5, 0], valign = 'middle')


def open_help_window(event): # opens the help window
    help_window.show_on_top()

def close_help_window(event): # closes the help window
    help_window.hide()


# Password Checking Functions

def get_letters(password): # checks for letters in the password
    letters = []
    for i in password:
        if i.isalpha():
            letters.append(i) 
    return len(letters)

def get_lower(password): # checks for lowercase letters in the password
    lowers = []
    for i in password:
        if i.islower():
            lowers.append(i) 
    return len(lowers)

def get_upper(password): # checks for uppercase letters in the password
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
    types = list(types_str)
    specials = []
    for i in password:
        if i in types:
            specials.append(i) 
    return len(specials)


def password_check(event): # runs the overall checks on the password 
    with open("100000-most-common-passwords.txt", "r") as file: # Opens the .txt file and puts it into a list
        password_list = file.read().splitlines()
    
    rating_lbl.text = '' # Text for password rating
    feedback = [] # Password feedback
    password = checker_inp.text
    password_rating = len(password)

    if password in password_list: # checks to see if the password is common
        password_rating -= 5
        feedback.append('This password has a high risk \nof being breached please change your password!')
    else:
        if len(password) <= 0: # checks if there's nothing in the input
            feedback.append("Please enter a password")    
        else:
            
            # further checks the length of password
            if len(password) >= 15:
                password_rating += 2
            elif len(password) >= 10:
                password_rating += 1
            elif len(password) >= 5:
                password_rating -= 2
            else:
                password_rating -= 5


            letters = get_letters(password) # checks for how many letters are in the password

            if letters > 3: # amount of letters is acceptable
                password_rating += 1

                uppers = get_upper(password) # finds how many captials are in the password

                if uppers > 2: # amount of captials is acceptable
                    password_rating += 2
                
                elif uppers == 0: # if there are no captials
                    password_rating -= 2
                    feedback.append("Try to include capital letters")

                elif uppers < 3: # amount of captials can be improved on
                    password_rating += 1
                    feedback.append("Try to include more capital letters")

                lowers = get_lower(password) # finds how many lowercases are in the password
                
                if lowers > 2: # amount of lowercases is acceptable
                    password_rating += 2

                elif lowers == 0: # if there are no lowercases
                    password_rating -= 2
                    feedback.append("Try to include lowercase letters")
                
                elif lowers < 3: # amount of lowercases can be improved on
                    password_rating += 1
                    feedback.append("Try to include more lowercase letters")
            
            elif letters == 0: # if there are no letters
                password_rating -= 1
                feedback.append("Try add letters")

            elif letters <= 3: # amount of letters can be improved on
                password_rating += 0.5
                feedback.append("Try having more letters")

                uppers = get_upper(password) # finds how many captials are in the password
                
                if uppers > 2: # amount of captials is acceptable
                    password_rating += 2
                
                elif uppers == 0: # if there are no captials
                    password_rating -= 2
                    feedback.append("Try to include capital letters")

                elif uppers < 3: # amount of captials can be improved on
                    password_rating += 1
                    feedback.append("Try to include more capital letters")
                
                lowers = get_lower(password) # finds how many lowercases are in the password
                
                if lowers > 2: # amount of lowercases is acceptable
                    password_rating += 2

                elif uppers == 0: # if there are no lowercases
                    password_rating -= 1
                    feedback.append("Try to include lowercase letters")

                elif lowers < 3: # amount of lowercases can be improved on
                    password_rating += 1
                    feedback.append("Try to include more lowercase letters")
            
            digits = get_digits(password) # checks for how many digits are in the password

            if digits > 3: # amount of digits is acceptable
                password_rating += 3
            
            elif digits == 0: # if there are not digits
                password_rating -= 2
                feedback.append("Try to include numbers") 

            elif digits < 4: # amount of digits can be improved on
                password_rating += 1.5
                feedback.append("Try to more include numbers") 

            specialchars = get_special_char(password) # checks for how many digits ar in the password

            if specialchars > 3: # amount of special characters is acceptable
                password_rating += 2
            
            elif letters == 0: # if there are not special characters
                password_rating -= 1
                feedback.append("Try having special characters")

            elif specialchars <= 4: # amount of special characters can be improved on            
                password_rating += 1.5
                feedback.append("Try having more special characters")


    securness = min(100, max(0, round((password_rating / 20) * 100))) # NOTE: Use of ChatGPT

    if securness >= 100:
        rating_lbl.text = (f"Password security is: 100%")
    elif securness == 0:
        rating_lbl.text = (f"Password security is: 0%")
    else:
        rating_lbl.text = (f"Password security is: {securness} %") # Calculates how secure the password is based on the rating 
          
          
    status_lbl.text = f"Feedback-\n{'\n'.join(feedback)}"
    rating_lbl.update()



def toggle_mask(event): # hides and shows the password
    checker_inp.toggle()

def copy_password(event):
    print("COPIED!!!")
    app.copy_to_clipboard(checker_inp.text)
    status_lbl.text = "Password copied"

def on_close():  
    result =  app.confirm_yesno('Exit', 'Are you sure your finished using the app?', 'warning') # warning, question  
    # If the user clicks 'Yes', close the app
    if result:
        app.quit()



# Main app window
app = gp.GooeyPieApp('Locksmith')
app.set_grid(50, 50)  # Sets the grid

# Main Tab
ask_lbl = gp.StyleLabel(app, 'Enter your password...')
ask_lbl.font_name = 'Eras Demi ITC'
ask_lbl.font_weight = 'bold'

rating_lbl = gp.StyleLabel(app, '')
rating_lbl.font_name = 'Eras Demi ITC'

status_lbl = gp.StyleLabel(app, '')
status_lbl.font_name = 'Eras Demi ITC'

checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 50

check = gp.Checkbox(app, 'Show Password')
check.add_event_listener('change', toggle_mask)

checker_btn = gp.Button(app, 'Check', password_check)

assist_btn = gp.Button(app, '?', open_help_window)
assist_btn.width = 3

copy_btn = gp.ImageButton(app, 'clipboard.png', copy_password, '')
copy_btn.width = 5

# Help Tab
help_window = gp.Window(app, 'Assistance')
help_window.set_grid(80, 80)  # Sets the grid

help1_txt = gp.StyleLabel(help_window, 'What is our intention?')
help1_txt.font_name = 'Eras Demi ITC'
help1_txt.font_weight = 'bold'

help2_txt = gp.StyleLabel(help_window, 'Our intention to give our users the tools to check whether their passwords are secure or not')
help2_txt.font_name = 'Eras Demi ITC'

help3_txt = gp.StyleLabel(help_window, 'What do each of the buttons do?')
help3_txt.font_name = 'Eras Demi ITC'
help3_txt.font_weight = 'bold'

help4_txt = gp.StyleLabel(help_window, 'Check - Intializes checking of your password in the box')
help4_txt.font_name = 'Eras Demi ITC'

help5_txt = gp.StyleLabel(help_window, '? - Provides a basic guide to the application and its details')
help5_txt.font_name = 'Eras Demi ITC'

help6_txt = gp.StyleLabel(help_window, '📋 - Copies whatever is in the text box')
help6_txt.font_name = 'Eras Demi ITC'

help7_txt = gp.StyleLabel(help_window, '❎ Show Password - Shows and hides your password which is inside the text box')
help7_txt.font_name = 'Eras Demi ITC'


help_btn = gp.Button(help_window, 'Ok!', close_help_window)


help_window.add(help1_txt, 1, 1)
help_window.add(help2_txt, 2, 1)
help_window.add(help3_txt, 3, 1)
help_window.add(help4_txt, 4, 1)
help_window.add(help5_txt, 5, 1)
help_window.add(help6_txt, 6, 1)
help_window.add(help7_txt, 7, 1)
help_window.add(help_btn, 10, 1)

# Startup Tab
startup_top_txt = gp.StyleLabel(app, 'Hello, \nWelcome to Locksmith!')
startup_top_txt.font_name = 'Eras Demi ITC'
startup_top_txt.font_size = 25

startup_mid_txt = gp.StyleLabel(app, 'We are here to help you create the most secure password as possible')
startup_mid_txt.font_name = 'Eras Demi ITC'


startup_bottom_txt = gp.StyleLabel(app, 'Please Press Start to begin...')
startup_bottom_txt.font_name = 'Eras Demi ITC'
startup_btn = gp.Button(app, 'Start', open_function)


lock_img = gp.Image(app, 'Logo.png')

loading_pb = gp.Progressbar(app)

app.add(startup_top_txt, 1, 1)
app.add(startup_mid_txt, 2, 1)
app.add(startup_bottom_txt, 3, 1)
app.add(startup_btn, 5, 1)
app.add(lock_img, 5, 5)

app.width = 500

app._root.protocol("WM_DELETE_WINDOW", on_close)
app.set_icon('Logo.png')

app.run()