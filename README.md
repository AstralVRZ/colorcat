
# About colorcat

A simple python script to print colored and styled text from a file to your terminal!
I originally created this because I wanted to show my todo list in a more visually appealing way when I open my terminal. But now it can be used for any text file!

## Installation

Clone the repository and run the script directly, or copy it to a directory in your PATH for global access.

```bash
git clone https://github.com/AstralVRZ/colorcat.git
cd colorcat
```

### Running colorcat

Run the script with:

```bash
python colorcat.py [-d [delay]] <file>
```

- `-d [delay]` (optional): Set a custom delay (in seconds) between lines. Default is `0.05`.

#### Examples

```bash
python colorcat.py -d ~/Documents/todo.txt      # Uses default delay (0.05)
python colorcat.py -d 0.1 ~/Documents/todo.txt  # Uses custom delay (0.1)
python colorcat.py ~/Documents/todo.txt         # Instant output (no delay)
```

### Make colorcat Globally Accessible

Copy the script to a directory in your PATH:

```bash
sudo cp colorcat.py /usr/local/bin/colorcat
sudo chmod +x /usr/local/bin/colorcat
```

Check your PATH directories with:

```bash
echo $PATH
```

Now you can run colorcat from anywhere:

```bash
colorcat <file>
```

## Color syntax

To give the text you want to be read out to your terminal a color or style, use the following syntax in your text file:

### Colors

| Syntax | Color |
| ----------- | ----------- |
| :b; | black ⚫ |
| :bl; | blue 🔵 |
| :c; | cyan 🔵 |
| :g; | green 🟢 |
| :m; | magenta 🟣 |
| :r; | red 🔴 |
| :w; | white ⚪ |
| :y; | yellow 🟡 |

### Bright Colors

| Syntax | Color |
| ----------- | ----------- |
| :bb; | bright black ⚫ |
| :bbl; | bright blue 🔵 |
| :bc; | bright cyan 🔵 |
| :bg; | bright green 🟢 |
| :bm; | bright magenta 🟣 |
| :br; | bright red 🔴 |
| :bw; | bright white ⚪ |
| :by; | bright yellow 🟡 |

### Styles

| Syntax | Style |
| ----------- | ----------- |
| :B; | **bold** |
| :D; | dim |
| :I; | *italic* |
| :N; | reset/normal |
| :R; | reverse (background and text color) |
| :U; | underline |

Styles and colors can be combined by placing them one after another, styles will get reset on a new line, and the color can be changed in a single line.
Here is a quick example:

```txt
:b;This text is black:r; and this text is red.
:U;This text is underlined.
:B;:U;This text is bold and underlined!Reorganize this part of the readme, line 7-54


:g;:I;This text is green and italic.
```

If you want to see everything you can run the command on the `examples.txt` file!
