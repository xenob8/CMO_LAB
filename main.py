import sys

f = open('output.txt','w')
from app import App
app = App()
app.run(100)
print(app.put_disp.n_refused, file=f)
app.refresh()
app.run(100)
print(app.put_disp.n_refused, file=f)
app.refresh()
app.run(100)
print(app.put_disp.n_refused, file=f)
app.refresh()
app.run(100)
print(app.put_disp.n_refused, file=f)
app.refresh()

