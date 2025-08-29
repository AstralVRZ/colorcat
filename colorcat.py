#!/usr/bin/env python3
import sys
import re
import subprocess

# Mapping markers to Fish set_color keywords
MARKERS = {
    'y': 'yellow',   # Yellow
    'g': 'green',    # Green
    'r': 'red',      # Red
    'B': '-o',     # Bold text
    'I': '-i',   # Italic text
    'R': 'normal'    # Reset to normal formatting
}

def fish_set_color(color_keyword):
    """
    Run the Fish shell command 'set_color <color_keyword>',
    capturing its ANSI escape code output.
    """
    return subprocess.check_output(['fish', '-c', f'set_color {color_keyword}'], text=True)

def colorize(line):
    """
    Replace markers like ::y, ::I, etc. with actual ANSI codes from Fish.
    This ensures the terminal interprets and renders the formatting.
    """
    output = ""
    while line:
        match = re.match(r'(.*?)::([ygrBIR])', line)
        if match:
            output += match.group(1)  # Text before the marker
            ansi = fish_set_color(MARKERS[match.group(2)])  # Execute set_color
            output += ansi
            line = line[len(match.group(0)):]  # Remove processed part
        else:
            output += line
            break
    # Append reset/normal formatting at the end to avoid bleed-through
    output += fish_set_color('normal')
    return output

def main():
    """Reads the given file and outputs colorized content line by line."""
    if len(sys.argv) < 2:
        print("Usage: colorcat <file>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                print(colorize(line.rstrip()))
    except FileNotFoundError:
        print(f"Error: File not found: {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
