import curses

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 0, 255)
    stdscr.addstr(str(1), curses.color_pair(1))
    stdscr.getch()

curses.wrapper(main)