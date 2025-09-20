#!/usr/bin/env python3
import sys
import re
import time

slow = False               # set to True to print line by line with a delay
delay = 0.05               # delay in seconds between lines

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
    if len(sys.argv) < 2:
        print("Usage: colorcat <file>")
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                # colorize each line and print
                print(colorize(line.rstrip()))
                # Add a delay to printing each line if slow mode is enabled
                if slow:
                    time.sleep(delay)
    except FileNotFoundError:
        print(f"Error: File not found: {sys.argv[1]}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(3)


if __name__ == '__main__':
    main()
