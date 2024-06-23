import gooeypie as gp
import time


def ask(event):
    loading_pb.value = 0
    for i in range(20):
        loading_pb.value += 5
        app.refresh()
        time.sleep(0.02)
    
    ask_btn.destroy()
    loading_pb.destroy()
    


app = gp.GooeyPieApp('Magic 8 Ball')


ask_btn = gp.Button(app, 'Ask', ask)

loading_pb = gp.Progressbar(app)


app.set_grid(10, 10)
app.add(ask_btn, 1, 2, valign='middle')
app.add(loading_pb, 2, 1, column_span=10, fill=True)

app.width = 500


app.run()
