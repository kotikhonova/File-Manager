import curses
import os
#from keys import Keys
from widgets.content import Content

class UI:
	def __init__():
		pass

	def ui_conf(sself):
		curses.flash()
		curses.cbreak()
		curses.noecho()
		stdscr.keypad(True)
		curses.halfdelay(20)
		stdscr.refresh()
		curses.start_color()

wd = os.getcwd()
ofl = os.listdir(os.getcwd())

stdscr= curses.initscr()

curses.use_default_colors()
curses.init_pair(1, 0, 255)

begin_x = 1; begin_y = 1
height = 5; width = 40
current_directory = curses.newwin(height, width, begin_y, begin_x)
current_directory.addstr(wd)
current_directory.refresh()
Content.highlightText = curses.color_pair(1)
Content.normalText = curses.A_NORMAL

content = Content(ofl)
content.print_list()

def main():
	while True:
		c = stdscr.getch()
		if c == ord('e'):
			content.keypress()
		elif c == curses.KEY_UP:
			content.up()
		elif c == curses.KEY_DOWN:
			content.down()
		if c == ord('q'):
			curses.nocbreak()
			stdscr.keypad(False)
			curses.echo()
			curses.endwin()
			break
main()
