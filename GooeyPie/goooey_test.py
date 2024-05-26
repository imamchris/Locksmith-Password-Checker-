import gooeypie as gp

# def say_hello(event): # triggers an event
#     hello_lbl.text = 'Hello Gooey Pie!'


# app = gp.GooeyPieApp('Hello!')
# app.width = 250

# hello_btn = gp.Button(app, 'Say Hello', say_hello) # ___ - Text - Event
# hello_lbl = gp.Label(app, '')

# app.set_grid(10, 10) # Size of Tab
# # app.add(hello_btn, 1, 1, align='center')
# # app.add(hello_lbl, 2, 1, align='center') # Text - Location: y, x (make sure it's within size of the Tab) - alignment


# app.add(hello_btn, 5, 5, align= 'center', fill = True)

# app = gp.GooeyPieApp('TabContainer Demo')

# Create tab container
# tabs_cont = gp.TabContainer(app)

# # Create tabs
# tab1_tab = gp.Tab(tabs_cont, 'Tab 1')
# tab2_tab = gp.Tab(tabs_cont, 'Tab 2')

# # Create widgets for each tab
# some_lbl = gp.Label(tab1_tab, 'A label in Tab 1')
# some_btn = gp.Button(tab2_tab, 'A button in Tab 2', None)

# # Add widgets to each tab
# tab1_tab.set_grid(1, 1)
# tab1_tab.add(some_lbl, 1, 1, align='center', valign='middle')
# tab2_tab.set_grid(1, 1)
# tab2_tab.add(some_btn, 1, 1, align='center', valign='middle')

# # Add tabs to TabContainer
# tabs_cont.add(tab1_tab)
# tabs_cont.add(tab2_tab)

# # Add TabContainer to main window
# app.set_grid(1, 1)
# app.add(tabs_cont, 1, 1, fill=True, stretch=True)

# def toggle_mask(event):
#     secret.toggle()

# app = gp.GooeyPieApp('Secret')

# question = gp.Label(app, "What's your secret?")

# secret = gp.Secret(app)
# secret.width = 50

# check = gp.Checkbox(app, 'Show secret')
# check.add_event_listener('change', toggle_mask)

# app.set_grid(3, 1)
# app.add(question, 1, 1)
# app.add(secret, 2, 1)
# app.add(check, 3, 1)

# app.run()

# with open("100000-most-common-passwords.txt", "r") as file:
#     password_list = file.read().splitlines()

#     target_word = password

# if target_word in password_list:
#     print(f"'{target_word}' is in the list of common passwords.")
# else:
#     print(f"'{target_word}' is not in the list.")


