import keyboard

def press_key(gesture):
	key=""
	try:
		key=dict[gesture]
		keyboard.send(key)
		print("Initiate key stroke "+key)
	except:
		pass
	return






dict = {"PointLeft":"left",
	"PointRight":"right",
	"Fist":"space",
	}
