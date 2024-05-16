import gooeypie as gp

def say_hello(event): # triggers an event
    #startup_lbl.text = ''
    # app.add(name_lbl, 11, 5, align='center')
    # app.add(name_inp, 12, 5)
    # app.add(hello_btn, 13, 5, align='center')
    # app.add(hello_lbl, 14, 5, align='center')



def password_input(event):
    print("eh")

app = gp.GooeyPieApp('Locksmith')

app.width = 250

hello_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!')
start_lbl = gp.Label(app, 'Please press the button to begin')
startup_btn = gp.Button(app, 'Begin', say_hello)
startup_lbl = gp.Label(app, '')

name_lbl = gp.Label(app, 'What is the password?')
name_inp = gp.Input(app)
name_inp.justify = 'center'
name_inp.width = 30
hello_btn = gp.Button(app, 'Begin', password_input)
hello_lbl = gp.Label(app, '')

app.set_grid(30, 30) # Size of Tab
app.add(hello_lbl, 5, 5, align='center') # Text - Location: y, x (make sure it's within size of the Tab) - alignment
app.add(start_lbl, 7, 5, align='center')
app.add(startup_btn, 9, 5, align='center')
app.add(startup_lbl, 10, 5, align='left')

app.add(name_lbl, 11, 5, align='center')
app.add(name_inp, 12, 5)
app.add(hello_btn, 13, 5, align='center')
app.add(hello_lbl, 14, 5, align='center')


app.run()