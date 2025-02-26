import curses
import time
import random
import argparse

crab = "🦀"

def crabbing(stdscr, target_count):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    max_y, max_x = stdscr.getmaxyx()
    x, y = random.randint(0, max_x - 1), random.randint(0, max_y - 1)
    direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    
    # Define a set of characters suitable for collection
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Calculate the number of characters to fill 40% of the terminal
    num_chars = int(0.40 * max_y * max_x)
    random_chars = {}
    for _ in range(num_chars):
        char_x = random.randint(0, max_x - 1)
        char_y = random.randint(0, max_y - 1)
        random_chars[(char_y, char_x)] = random.choice(valid_chars)

    collected_chars = ""

    while True:
        stdscr.clear()
        
        # Draw random characters
        for (char_y, char_x), char in random_chars.items():
            if 0 <= char_x < max_x and 0 <= char_y < max_y:
                try:
                    stdscr.addstr(char_y, char_x, char)
                except curses.error:
                    pass
        
        # Draw the crab
        if 0 <= x < max_x and 0 <= y < max_y:
            try:
                stdscr.addstr(y, x, crab)
            except curses.error:
                pass
        stdscr.refresh()
        time.sleep(0.1)

        # Check if the crab collects a character
        if (y, x) in random_chars:
            collected_char = random_chars.pop((y, x))
            collected_chars += collected_char

            # Check if the target number of characters have been collected
            if len(collected_chars) >= target_count:
                break

        if random.random() < 0.3:
            direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

        new_x = x + direction[0]
        new_y = y + direction[1]

        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            x, y = new_x, new_y
        else:
            direction = (-direction[0], -direction[1])

    return collected_chars

def run_crabbing():
    parser = argparse.ArgumentParser(description="Crab animation with character collection.")
    parser.add_argument("--target", type=int, default=16, help="Number of characters to collect before exiting.")
    args = parser.parse_args()
    collected_chars = curses.wrapper(crabbing, args.target)
    print(f"{collected_chars}")

if __name__ == "__main__":
    run_crabbing()