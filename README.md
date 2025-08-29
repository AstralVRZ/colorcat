# About colorcat

A simple python script to print colored and styled text from a file to your terminal!
I originally created this because I wanted to show my todo list in a more visually appealing way when I open my terminal. But now it can be used for any text file!

# How to install:
You can install colorcat by cloning the repository and running the script directly, or by copying the script to a directory in your PATH.

```bash
git clone https://github.com/AstralVRZ/colorcat.git
cd colorcat
```

Then you can run the script with:

```bash
python colorcat.py <file>
```

Or, to make it globally accessible, copy it to a directory in your PATH:

```bash
sudo cp colorcat.py /usr/local/bin/colorcat
sudo chmod +x /usr/local/bin/colorcat
```
If you want another path directory, run `echo $PATH` to see your PATH directories.

Now you can use it from anywhere:

```bash
colorcat <file>
```

# Color syntax:
To get give the text you want to be read out to your terminal a color or style, use the following syntax in your text file:

### Colors

 Syntax | Color |
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

 Syntax | Color |
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

 Syntax | Style |
| ----------- | ----------- |
| :B; | **bold** |
| :D; | dim |
| :I; | *italic* |
| :N; | reset/normal |
| :R; | reverse (background and text color) |
| :U; | underline |

Styles and colors can be combined by placing them one after another, styles will get reset on a new line, and the color can be changed in a single line.
Here is a quick example:

```
:b;This text is black:r; and this text is red.
:U;This text is underlined.
:B;:U;This text is bold and underlined!
:g;:I;This text is green and italic.
```

If you want to see everything you can run the command on the `examples.txt` file!