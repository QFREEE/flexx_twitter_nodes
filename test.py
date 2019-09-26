from flexx import flx

class Example(flx.Widget):
    def init(self):
        flx.Label(text='hello world')

app = flx.App(Example)


app.launch('browser')  # show it now in a browser
flx.run()  # enter the mainloop