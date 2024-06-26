import gooeypie as gp
import time

# Opening the App

def open_function(event): # destroys the startup page and adds the password checker
    
    app.refresh() # begins to show the loading bar
    app.add(loading_txt, 29, 1)
    app.add(loading_pb, 30, 1, column_span=30, fill=True) # adds the loading bar

    loading_pb.value = 0 
    step = 0
    for i in range(20): # Loading Process
        text, step = loading_text("Loading...", step)
        loading_pb.value += 5
        
        loading_txt.text = text
        loading_txt.update()
        
        app.refresh()

        time.sleep(0.02)
    
    # Destroy startup widgets

    loading_pb.destroy() # removes loading bar once finished
    loading_txt.destroy() # removes the loading text
    startup_top_txt.destroy()
    startup_mid_txt.destroy()
    startup_bottom_txt.destroy()
    startup_btn.destroy()
    lock_img.destroy()
    app.refresh()

    app.height = 100

    # Add new widgets
    app.add(ask_lbl, 6, 1)
    
    app.add(checker_inp, 8, 1, margins=[5, 0, 5, 15], valign = 'middle')
    app.add(checker_btn, 8, 2, margins=[5, 0, 5, 0], valign = 'middle')
    app.add(check, 9, 1)
    app.add(assist_btn, 8, 3, margins=[5, 0, 5, 0], valign = 'middle')
    app.add(copy_btn, 8, 4, margins=[5, 0, 5, 0], valign = 'middle')
    
    app.add(sep_1, 10, 1)
    
    app.add(rating_lbl, 11, 1)
    app.add(status_lbl, 12, 1)

    app.add(sep_2, 13, 1)

    app.add(details_info_btn, 14, 1)


def loading_text(text, step): # NOTE: Use of ChatGPT, Changes the amount of dots in the loading text
    if step >= 3: # Adjust the step and reset if it's greater than 3
        step = 0
    else:
        step += 1

    text = text.replace('.', '') # Remove all dots from the text
    result = text + ('.' * step) # Adds new ones to the end of the text based on the step

    return result, step

# Help Window

def open_help_window(event): # opens the help window
    help_window.show_on_top()

def close_help_window(event): # closes the help window
    help_window.hide()

# Detail Window

def open_details_window(event): # opens the help window
    details_window.show_on_top()

def close_details_window(event): # closes the help window
    details_window.hide()

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


def get_rating(count, thresholds): # NOTE: Use of ChatGPT, Gets rating of individual statistics
    if count >= thresholds['Very Good']:
        return 'Very Good'
    elif count >= thresholds['Good']:
        return 'Good'
    elif count >= thresholds['Ok']:
        return 'Ok'
    elif count >= thresholds['Poor']:
        return 'Poor'
    else:
        return 'Very Poor'

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
            length_of_password.txt = f'{len(password)} (Very Poor)'
        else:
            
            # further checks the length of password
            if len(password) >= 15:
                password_rating += 2
                
            elif len(password) >= 10:
                password_rating += 1
                feedback.append("The length is good but can be increased")
                
            elif len(password) >= 5:
                password_rating -= 2
                feedback.append("Try to make the password longer")
            
            else:
                password_rating -= 5
                feedback.append("Please make the password longer")

            letters = get_letters(password) # checks for how many letters are in the password

            if letters > 3: # amount of letters is acceptable
                password_rating += 1

                uppers = get_upper(password) # finds how many captials are in the password


                if uppers > 2: # amount of captials is acceptable
                    password_rating += 2
                
                elif uppers == 0: # if there are no captials
                    password_rating -= 2
                    feedback.append("Please include capital letters")

                elif uppers < 3: # amount of captials can be improved on
                    password_rating += 1
                    feedback.append("Try to include more capital letters")

                lowers = get_lower(password) # finds how many lowercases are in the password
                
                if lowers > 2: # amount of lowercases is acceptable
                    password_rating += 2

                elif lowers == 0: # if there are no lowercases
                    password_rating -= 2
                    feedback.append("Please include lowercase letters")
                
                elif lowers < 3: # amount of lowercases can be improved on
                    password_rating += 1
                    feedback.append("Try to include more lowercase letters")
            
            elif letters == 0: # if there are no letters
                password_rating -= 1
                feedback.append("Please add letters to the password")

            elif letters <= 3: # amount of letters can be improved on
                password_rating += 0.5
                feedback.append("Try having more letters")

                uppers = get_upper(password) # finds how many captials are in the password
                
                if uppers > 2: # amount of captials is acceptable
                    password_rating += 2
                
                elif uppers == 0: # if there are no captials
                    password_rating -= 2
                    feedback.append("Please include capital letters")

                elif uppers < 3: # amount of captials can be improved on
                    password_rating += 1
                    feedback.append("Try to include more capital letters")
                
                lowers = get_lower(password) # finds how many lowercases are in the password
                
                if lowers > 2: # amount of lowercases is acceptable
                    password_rating += 2

                elif lowers == 0: # if there are no lowercases
                    password_rating -= 1
                    feedback.append("Please include lowercase letters")

                elif lowers < 3: # amount of lowercases can be improved on
                    password_rating += 1
                    feedback.append("Try to include more lowercase letters")
            
            digits = get_digits(password) # checks for how many digits are in the password

            if digits > 3: # amount of digits is acceptable
                password_rating += 3
            
            elif digits == 0: # if there are not digits
                password_rating -= 2
                feedback.append("Please include numbers") 

            elif digits < 4: # amount of digits can be improved on
                password_rating += 1.5
                feedback.append("Try to include more numbers") 

            specialchars = get_special_char(password) # checks for how many digits ar in the password

            if specialchars > 3: # amount of special characters is acceptable
                password_rating += 2
            
            elif letters == 0: # if there are not special characters
                password_rating -= 1
                feedback.append("Please include special characters")

            elif specialchars <= 4: # amount of special characters can be improved on            
                password_rating += 1.5
                feedback.append("Try having more special characters")

    securness = min(100, max(0, round((password_rating / 20) * 100))) # NOTE: Use of ChatGPT, calculates the securness of the password

    # changes the colour of the text based on the score above
    if securness >= 100:
        rating_lbl.text = (f"Password security is: 100%")
        colour = 'DarkOliveGreen'
    elif securness == 0:
        rating_lbl.text = (f"Password security is: 0%")
        colour = 'Crimson'
    else:
        rating_lbl.text = (f"Password security is: {securness} %") # Calculates how secure the password is based on the rating 
        colour = 'DarkOrange'  
          
    status_lbl.text = f"Feedback-\n{'\n'.join(feedback)}" # adds in the feedback
    rating_lbl.colour = colour # changes the colour of the rating
    rating_lbl.update()

    # NOTE: Use of ChatGPT, Gets the individual rating for the stat details and updates them
    length_of_password.text = f'Length: {len(password)} ({get_rating(len(password), {"Very Good": 15, "Good": 10, "Ok": 5, "Poor": 1})})'
    letters_of_password.text = f'Letters: {get_letters(password)} ({get_rating(get_letters(password), {"Very Good": 10, "Good": 7, "Ok": 4, "Poor": 1})})'
    lowers_of_password.text = f'Lowercase Letters: {get_lower(password)} ({get_rating(get_lower(password), {"Very Good": 5, "Good": 3, "Ok": 2, "Poor": 1})})'
    uppers_of_password.text = f'Uppercase Letters: {get_upper(password)} ({get_rating(get_upper(password), {"Very Good": 5, "Good": 3, "Ok": 2, "Poor": 1})})'
    digits_of_password.text = f'Digits: {get_digits(password)} ({get_rating(get_digits(password), {"Very Good": 5, "Good": 3, "Ok": 2, "Poor": 1})})'
    specials_of_password.text = f'Special Characters: {get_special_char(password)} ({get_rating(get_special_char(password), {"Very Good": 5, "Good": 3, "Ok": 2, "Poor": 1})})'

    length_of_password.update()
    length_of_password.update()
    lowers_of_password.update()
    uppers_of_password.update()
    digits_of_password.update()
    specials_of_password.update()


# Other Features

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

checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 50

sep_1 = gp.Separator(app, 'horizontal')

rating_lbl = gp.StyleLabel(app, 'Password security is: ...')
rating_lbl.font_name = 'Eras Demi ITC'

status_lbl = gp.StyleLabel(app, '...')
status_lbl.font_name = 'Eras Demi ITC'

sep_2 = gp.Separator(app, 'horizontal')

details_info_btn = gp.Button(app, 'Details', open_details_window)



# Help Tab
help_window = gp.Window(app, 'Assistance')
help_window.set_grid(80, 80)  # Sets the grid

help1_txt = gp.StyleLabel(help_window, 'What is our intention?')
help1_txt.font_name = 'Eras Demi ITC'
help1_txt.font_weight = 'bold'
help1_txt.font_size = 15

help2_txt = gp.StyleLabel(help_window, 'Our intention to give our users the tools to check whether their passwords are secure or not')
help2_txt.font_name = 'Eras Demi ITC'

help3_txt = gp.StyleLabel(help_window, 'What do each of the buttons do?')
help3_txt.font_name = 'Eras Demi ITC'
help3_txt.font_weight = 'bold'
help3_txt.font_size = 15

help4_txt = gp.StyleLabel(help_window, 'Check - Intializes checking of your password in the box')
help4_txt.font_name = 'Eras Demi ITC'

help5_txt = gp.StyleLabel(help_window, '? - Provides a basic guide to the application and its details')
help5_txt.font_name = 'Eras Demi ITC'

help6_txt = gp.StyleLabel(help_window, '📋 - Copies whatever is in the text box')
help6_txt.font_name = 'Eras Demi ITC'

help7_txt = gp.StyleLabel(help_window, '❎ Show Password - Shows and hides your password which is inside the text box')
help7_txt.font_name = 'Eras Demi ITC'

help8_txt = gp.StyleLabel(help_window, 'Details - Shows stats of the checked password such as its length, amount of letters, etc...')
help8_txt.font_name = 'Eras Demi ITC'


help_btn = gp.Button(help_window, 'Ok!', close_help_window)


help_window.add(help1_txt, 1, 1)
help_window.add(help2_txt, 2, 1)
help_window.add(help3_txt, 3, 1)
help_window.add(help4_txt, 4, 1)
help_window.add(help5_txt, 5, 1)
help_window.add(help6_txt, 6, 1)
help_window.add(help7_txt, 7, 1)
help_window.add(help8_txt, 8, 1)
help_window.add(help_btn, 10, 1)



# Details
details_window = gp.Window(app, 'Password Details')
details_window.set_grid(80, 80)  # Sets the grid

detail_intro = gp.StyleLabel(details_window, 'Password Details -')
detail_intro.font_name = 'Eras Demi ITC'
detail_intro.font_weight = 'bold'
detail_intro.font_size = 15

detail_intro2 = gp.StyleLabel(details_window, 'NOTE: Please make sure you pressed check for your given password \n            or else stats of previous passwords may be shown!')
detail_intro2.font_name = 'Eras Demi ITC'
detail_intro2.font_weight = 'bold'
detail_intro2.font_size = 10

length_of_password = gp.StyleLabel(details_window, 'Password Length: ...')
length_of_password.font_name = 'Eras Demi ITC'

letters_of_password = gp.StyleLabel(details_window, 'Letters in Password: ...')
letters_of_password.font_name = 'Eras Demi ITC'

lowers_of_password = gp.StyleLabel(details_window, 'Lowercases in Password: ...')
lowers_of_password.font_name = 'Eras Demi ITC'

uppers_of_password = gp.StyleLabel(details_window, 'Capitals in Passworrd: ...')
uppers_of_password.font_name = 'Eras Demi ITC'

digits_of_password = gp.StyleLabel(details_window, 'Numbers in Password: ...')
digits_of_password.font_name = 'Eras Demi ITC'

specials_of_password = gp.StyleLabel(details_window, 'Special Characters in Password: ...')
specials_of_password.font_name = 'Eras Demi ITC'

detail_btn = gp.Button(details_window, 'Ok!', close_details_window)


details_window.add(detail_intro, 1, 1)
details_window.add(detail_intro2, 2, 1)
details_window.add(length_of_password, 3, 1)
details_window.add(letters_of_password, 4, 1)
details_window.add(lowers_of_password, 5, 1)
details_window.add(uppers_of_password, 6, 1)
details_window.add(specials_of_password, 7, 1)

details_window.add(detail_btn, 10, 1)

details_window.width = 400

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

loading_txt = gp.StyleLabel(app, "Loading...")
loading_txt.font_name = 'Eras Demi ITC'
loading_txt.font_weight = 'bold'

app.add(startup_top_txt, 1, 1)
app.add(startup_mid_txt, 2, 1)
app.add(startup_bottom_txt, 3, 1)
app.add(startup_btn, 5, 1)
app.add(lock_img, 5, 5)



app.set_resizable(True)

app.height = 550
app.width = 600

app._root.protocol("WM_DELETE_WINDOW", on_close)
app.set_icon('Logo.png')

app.run()