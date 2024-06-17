import gooeypie as gp

# def open_on_top_window(event):
#     help_window.show_on_top()

# def close_on_top_window(event):
#     help_window.hide()

# # Create main window
# app = gp.GooeyPieApp('Other windows')
# app.width = 250
# assist_btn = gp.Button(app, 'Open on top', open_on_top_window)
# app.set_grid(1, 2)
# app.add(assist_btn, 1, 1)

# # Create other windows
# help_window = gp.Window(app, 'On top window')
# help_window.width = 300
# help_txt = gp.Label(help_window, 'This is what you do...')
# help_btn = gp.Button(help_window, 'Ok!', close_on_top_window)
# help_window.set_grid(5, 5)
# help_window.add(help_txt, 1, 1)
# help_window.add(help_btn, 3, 1)

# app.run()

# def get_digits(password):
#     digits = []

#     for i in password:
#         if i.isdigit():
#             digits.append(i) 
#     return digits

# def get_alpha(password):
#     letters = []

#     for i in password:
#         if i.isalpha():
#             letters.append(i) 
#     return letters

# print(get_alpha(""))


# def get_special_characters(password):    
#     types_str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#     types = list(types_str)

#     specials = []

#     for i in password:
#         if i in types:
#             specials.append(i) 
#     return len(specials)


# print(get_special_characters(""))

