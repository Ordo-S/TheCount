#!/usr/bin/python3
import curses


def draw_menu(stdscr):
    k = 0
    count = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Get rid of the cursor
    curses.curs_set(0)

    # Loop where k is the last character pressed
    while k != ord("q"):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "The Count"[: width - 1]
        subtitle = "{}".format(count)[: width - 1]
        statusbarstr = (
            "Press 'q' to exit | Press 'b' to go back | Press 'r' to reset"
        )

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2) - 2)


        # Render status bar
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(
            height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1)
        )
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 3, "-" * 6)
        #stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
        if k == ord('b'):
            count = count - 1
        elif k == ord('r'):
            count = 0
        else:
            count = count + 1

def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
