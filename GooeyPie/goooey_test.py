import gooeypie as gp

def say_hello(event): # triggers an event
    hello_lbl.text = 'Hello Gooey Pie!'


app = gp.GooeyPieApp('Hello!')
app.width = 250

hello_btn = gp.Button(app, 'Say Hello', say_hello) # ___ - Text - Event
hello_lbl = gp.Label(app, '')

app.set_grid(10, 10) # Size of Tab
app.add(hello_btn, 1, 1, align='center')
app.add(hello_lbl, 2, 1, align='center') # Text - Location: y, x (make sure it's within size of the Tab) - alignment


app.run()

