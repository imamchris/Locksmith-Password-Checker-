import gooeypie as gp

def password_check(event):
    
    if len(checker_inp.text) == 5:
        verify_lbl.text = 'GREAT!' 
    else:
        verify_lbl.text = 'Could be better...'
    
    checker_inp.update()

app = gp.GooeyPieApp('Locksmith')
# tabs_cont = gp.TabContainer(app)

# intro = gp.Tab(tabs_cont, 'Tab 1')
# checker = gp.Tab(tabs_cont, 'Tab 2')

app.set_size(250, 250) 

intro_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!') # location, text
ask_lbl = gp.Label(app, 'Enter your password...')
verify_lbl = gp.Label(app, 'NAN')
checker_inp = gp.Input(app)
checker_inp.justify = 'center'
checker_inp.width = 30
checker_btn = gp.Button(app, 'Check', password_check) # location, text, function

# intro_tab.set_grid(1, 1)
# checker_tab.add(some_lbl, 1, 1, align='center', valign='middle')

app.set_grid(50, 50) # Size of Tab
# intro.set_grid(50, 50)

app.add(intro_lbl, 5, 25, align='center') # Text - Location: y, x (make sure it's within size of the Tab) - alignment

app.set_grid(50, 50)
app.add(ask_lbl, 7, 25, align='center')
app.add(checker_inp, 10, 25)
app.add(verify_lbl, 12, 25, align='center')
app.add(checker_btn, 17, 25, align='center')

# tabs_cont.add(intro)
# tabs_cont.add(checker)

# app.add(tabs_cont, 1, 1, fill=True, stretch=True)


app.run()