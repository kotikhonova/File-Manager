import sys
from collections import namedtuple
from runner import Runner


'''
как вызывается?
class Fm:
self.keymap = Keymap()
self.keybuffer = Keybuffer(self.keymap)

'''

class Hotkeys:
	def __init__(self, keymap):
		self.keymap = keymap

	def load():
		if config:
			pass
		#else error

	def update():
		pass

	def destroy():
		pass




class KeyBindings:
	def __init__():
		pass

	def parse_keys(self):
		return 

	def get_key(self):
		# how to add keymap
		Keys = namedtuple('Keys', 'hotkeys, command')
		return sorted((
			Keys(*parse_keys(hotkey))
			for hotkey in keymap), key=attrgetter('hotkeys'))


	def print_help(self, mode=False):
		for k in get_keys():
			print(k.hotkeys, k.command)





class KeyBuf:
	def __init__(self, keys):
		self.keys = keys

	def buf_clear():
		pass

	def add_key():
		pass


