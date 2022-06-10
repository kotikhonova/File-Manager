import os
import curses
import colors

hotkeys = {
	
}

class ERROR:
	hotkeys_error = "No such a keyboard shortcut."


class Content:
	highlightText = None
	normalText = None

	def __init__(self, ofl):
		self.directory_content = None
		self.keybuf = ''
		self.ofl = ofl
		self.pos = 0
		old_pos = 0

	def first_item(self):
		self.file_listing.addstr(0, 0, self.ofl[0], self.highlightText)

	def print_list(self):
		self.file_listing = curses.newwin(len(self.ofl) + 2, 100, 2, 2)
		for i in self.ofl:
			self.file_listing.addstr(f'{i}\n')
		self.first_item()
		self.file_listing.refresh()


	def navigation(self, changed):
		old_pos = self.pos
		self.pos += changed
		self.file_listing.addstr(old_pos, 0, self.ofl[old_pos], self.normalText)
		self.file_listing.addstr(self.pos, 0, self.ofl[self.pos], self.highlightText)
		self.file_listing.refresh()

	def keypress(self, stdscr):
		curses.echo()
		self.keybuf = stdscr.getstr(5,5,5)
		if self.keybuf not in 



	def up(self):
		self.navigation(-1)

	def down(self):
		self.navigation(+1)

