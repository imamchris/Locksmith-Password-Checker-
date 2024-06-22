import gooeypie as gp

def on_close():
    # Show a confirmation dialog using tkinter
    result =  app.confirm_yesno('Warning', 'Are you sure you want to leave?', 'warning') #warning, question
    # If the user clicks 'Yes', close the app
    if result:
        app.quit()

# Create the app window
app = gp.GooeyPieApp('Confirmation on Close')
app.set_size(400, 300)

# Use the built-in tkinter method to intercept the close event
app._root.protocol("WM_DELETE_WINDOW", on_close)

app.run()
