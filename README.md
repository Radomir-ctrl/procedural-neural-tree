# Procedural Tree Generator

A Python/Tkinter program that draws a different branching tree each time it starts. The tree is made from many small colored ovals. Its branches vary in length, width, direction, and color.

## How the tree is generated

The program starts at the bottom center of the canvas and recursively draws six levels of branches. At each level it takes a step along the current angle, draws a small oval, and changes the angle, diameter, and RGB values. The number and spread of child branches come from that level's parameters. Random deviations add variation to lengths, turns, angles, and colors.

The code calls its list of six parameter sets a **genome**. Each set controls a branch level's base length and size, size and color shifts, number of child branches, maximum branch angle, how much size and color are inherited from the parent, and the amount of random variation. The parameters are sampled once when the program starts.

Despite the historical file name and the word “genome,” this is **procedural graphics**. There is no neural network, machine-learning model, training, fitness calculation, selection, or mutation across generations.

## Requirements

Python 3 with Tkinter support. The program uses only the Python standard library and has no external dependencies or assets.

## Run

```powershell
python neuroweb.py
```

You can run the script from any working directory. Close the window to exit. Restart it to generate a new tree.

## Project structure

- `neuroweb.py` — randomized parameters, recursive branching, and Tkinter drawing
- `.gitignore` — Python and editor-generated files

Originally developed as part of a programming/neural-network course and later cleaned up for publication.

**Author:** Radomyr Karpan
