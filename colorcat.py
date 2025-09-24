#!/usr/bin/env python3
import sys
import re
import time

delayMode = False           # set to True to print line by line with a delay
delay = 50                  # delay in milliseconds between lines

# Define the color mappings
MARKERS = {
    # Normal colors
    'b': '\033[30m',       # Black
    'bl': '\033[34m',      # Blue
    'c': '\033[36m',       # Cyan
    'g': '\033[32m',       # Green
    'm': '\033[35m',       # Magenta
    'r': '\033[31m',       # Red
    'w': '\033[37m',       # White
    'y': '\033[33m',       # Yellow

    # Bright colors
    'bb': '\033[90m',      # Bright Black
    'bbl': '\033[94m',     # Bright Blue
    'bc': '\033[96m',      # Bright Cyan
    'bg': '\033[92m',      # Bright Green
    'bm': '\033[95m',      # Bright Magenta
    'br': '\033[91m',      # Bright Red
    'bw': '\033[97m',      # Bright White
    'by': '\033[93m',      # Bright Yellow

    # Styles
    'B': '\033[1m',        # Bold
    'D': '\033[2m',        # Dim
    'I': '\033[3m',        # Italic
    'N': '\033[0m',        # Reset/Normal
    'R': '\033[7m',        # Reverse
    'U': '\033[4m',        # Underline
    
    # Background colors
    'bg_b': '\033[40m',    # Background Black
    'bg_bl': '\033[44m',   # Background Blue
    'bg_c': '\033[46m',    # Background Cyan
    'bg_g': '\033[42m',    # Background Green
    'bg_m': '\033[45m',    # Background Magenta
    'bg_r': '\033[41m',    # Background Red
    'bg_w': '\033[47m',    # Background White
    'bg_y': '\033[43m',    # Background Yellow

    # Bright background colors
    'bg_bb': '\033[100m',   # Background Bright Black
    'bg_bbl': '\033[104m',  # Background Bright Blue
    'bg_bc': '\033[106m',   # Background Bright Cyan
    'bg_bg': '\033[102m',   # Background Bright Green
    'bg_bm': '\033[105m',   # Background Bright Magenta
    'bg_br': '\033[101m',   # Background Bright Red
    'bg_bw': '\033[107m',   # Background Bright White
    'bg_by': '\033[103m',   # Background Bright Yellow

}


def colorize(line):
    """ Replace color markers like :y;, :B;, :bg; etc. in the text. """
    output = ""
    # Sort marker keys by length descending to match longest first
    marker_regex = '|'.join(sorted(MARKERS.keys(), key=len, reverse=True))
    pattern = re.compile(r'(.*?):(' + marker_regex + r')(;)?')
    while line:
        # Find marker (e.g., :y;)
        match = pattern.match(line)
        if match:
            # Add text before the marker
            output += match.group(1)
            # Add color formatting
            output += MARKERS[match.group(2)]
            # Remove marker and text processed
            line = line[len(match.group(0)):]
        else:
            output += line
            break
    # Append reset/normal formatting at the end to avoid bleed-through
    output += MARKERS['N']
    return output


def main():
    """ Main function to read file and output colored content. """
    # Globalize variables to decrease overhead
    global delayMode, delay
    args = sys.argv[1:]
    filename = None
    # Check if any arguments were provided
    if not args:
        print("Usage: colorcat [-d [delay]] <file>")
        sys.exit(1)
    # Parse arguments
    if args[0] == "-d":
        delayMode = True
        if len(args) == 2:  # only `-d` and <file> are provided
            filename = args[1]
        elif len(args) == 3:  # `-d`, [delay], and <file> are provided
            try:
                # Try to create a float from the delay argument
                delay = float(args[1])
            except ValueError:
                print(f"Invalid delay value: {args[1]}", file=sys.stderr)
                sys.exit(3)
            filename = args[2]
        else:
            print("Usage: colorcat [-d [delay]] <file>")
            sys.exit(1)
    else:
        # Only the filename is provided
        if len(args) == 1:
            filename = args[0]
        else:
            print("Usage: colorcat [-d [delay]] <file>")
            sys.exit(1)
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Parse line and print with colors
                print(colorize(line.rstrip()))
                if delayMode:
                    time.sleep(delay / 1000)  # Convert ms to seconds
    except FileNotFoundError:
        print(f"Error: File not found: {filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(99)


if __name__ == '__main__':
    main()
