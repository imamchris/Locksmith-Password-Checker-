import time

def loading_text(text, step):
    # Adjust the step and reset if it exceeds 3
    if step >= 3:
        step = 0
    else:
        step += 1

    # Remove all periods from the text
    text = text.replace('.', '')
    
    # Add the periods to the end of the text based on the step
    result = text + ('.' * step)

    return result, step

# Test the function
step = 0
for i in range(10):
    text, step = loading_text("loading...", step)
    loading_txt.text = text
    loading_txt.update()
    time.sleep(1)
