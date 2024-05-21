import gooeypie as gp

def toggle_mask(event):
    checker_inp.toggle()

def password_check(event):
    
    if len(checker_inp.text) == 0:
        verify_lbl.text = 'Please enter your password!' 
    elif len(checker_inp.text) >= 5:
        verify_lbl.text = 'GREAT!' 
    elif len(checker_inp.text) <= 5:
        verify_lbl.text = 'Your password should be 5 characters long atleast' 
    
    checker_inp.update()



app = gp.GooeyPieApp('Locksmith')

app.set_size(250, 250) 

check = gp.Checkbox(app, 'Show secret')
check.add_event_listener('change', toggle_mask)

intro_lbl = gp.Label(app, 'Hello! Welcome to Locksmith!') # location, text
ask_lbl = gp.Label(app, 'Enter your password...')
verify_lbl = gp.Label(app, '')
checker_inp = gp.Secret(app)
checker_inp.justify = 'left'
checker_inp.width = 45
checker_btn = gp.Button(app, 'Check', password_check) # location, text, function



app.set_grid(50, 200) # Size of Tab

app.add(intro_lbl, 5, 25, align='left') # Text - Location: y, x (make sure it's within size of the Tab) - alignment



app.set_grid(50, 50)
app.add(ask_lbl, 7, 25, align='left')
app.add(checker_inp, 10, 25)
app.add(check, 11, 25, allign ='left') 
app.add(verify_lbl, 12, 25, align='left')
app.add(checker_btn, 13, 25, align='left')



app.run()