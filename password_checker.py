import gooeypie as gp

def say_hello(event): # triggers an event
    greeting_lbl.text = 'Hello Gooey Pie!'

app = gp.GooeyPieApp('Locksmith')

app.width = 250

hello_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!')
start_lbl = gp.Label(app, 'Please press the button to begin')
greeting_btn = gp.Button(app, 'Begin', say_hello)
greeting_lbl = gp.Label(app, '')

app.set_grid(10, 10) # Size of Tab
app.add(hello_lbl, 5, 5, align='center') # Text - Location: y, x (make sure it's within size of the Tab) - alignment
app.add(start_lbl, 7, 5, align='center')
app.add(greeting_btn, 9, 5, align='center')
app.add(greeting_lbl, 10, 5, align='center')

app.run()