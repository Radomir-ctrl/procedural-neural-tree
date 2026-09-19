import math
import tkinter as tk
from random import randint, random, uniform


window = tk.Tk()
window.geometry("500x500")
window.title("Procedural Tree Generator")

canvas = tk.Canvas(window, width=500, height=500, bg="#012")
canvas.pack()


def make_genome_line(length, min_size, max_size):
    return {
        "length": length,
        "size": randint(min_size, max_size),
        "size shift": uniform(-0.3, 0.3),
        "red": randint(0, 255),
        "green": randint(0, 255),
        "blue": randint(0, 255),
        "red shift": uniform(-3, 3),
        "green shift": uniform(-3, 3),
        "blue shift": uniform(-3, 3),
        "branch amount": randint(1, 4),
        "max branch angle": randint(10, 60),
        "size from parent": random(),
        "color from parent": random(),
        "color deviation": randint(5, 40),
        "turn": uniform(-1, 1),
        "random turn": uniform(0, 5),
        "random length": randint(0, 30),
        "random angle": uniform(0, 20),
    }


genome = [
    make_genome_line(length, min_size, max_size)
    for length, min_size, max_size in (
        (100, 15, 25),
        (70, 12, 22),
        (50, 10, 20),
        (40, 8, 18),
        (35, 7, 16),
        (30, 6, 14),
    )
]


def rgb(red, green, blue):
    red = math.floor(min(max(red, 0), 255))
    green = math.floor(min(max(green, 0), 255))
    blue = math.floor(min(max(blue, 0), 255))
    return f"#{red:02x}{green:02x}{blue:02x}"


def radians_from_vertical(angle):
    return (angle - 90) * math.pi / 180


def circle(center_x, center_y, diameter, color):
    shift = max(abs(diameter), 3) / 2
    canvas.create_oval(
        center_x - shift,
        center_y - shift,
        center_x + shift,
        center_y + shift,
        fill=color,
        width=0,
    )


def blend_with_parent(child, parent, percent):
    return (parent - child) * percent + child


def branch(genome_line, parent_info):
    next_x = parent_info["endx"]
    next_y = parent_info["endy"]

    diameter = blend_with_parent(
        genome_line["size"], parent_info["last size"], genome_line["size from parent"]
    )

    percent_color = genome_line["color from parent"]
    red = blend_with_parent(genome_line["red"], parent_info["last red"], percent_color)
    green = blend_with_parent(genome_line["green"], parent_info["last green"], percent_color)
    blue = blend_with_parent(genome_line["blue"], parent_info["last blue"], percent_color)

    red += uniform(-genome_line["color deviation"], genome_line["color deviation"])
    green += uniform(-genome_line["color deviation"], genome_line["color deviation"])
    blue += uniform(-genome_line["color deviation"], genome_line["color deviation"])

    angle = parent_info["angle"] + uniform(
        -genome_line["random angle"], genome_line["random angle"]
    )
    length = genome_line["length"] + randint(
        -genome_line["random length"], genome_line["random length"]
    )

    for _ in range(length):
        next_x += math.cos(radians_from_vertical(angle))
        next_y += math.sin(radians_from_vertical(angle))

        angle += genome_line["turn"] * (
            parent_info["angle diff"] / genome_line["length"] * 3
        )
        angle += uniform(-genome_line["random turn"], genome_line["random turn"])
        diameter += genome_line["size shift"]
        red += genome_line["red shift"]
        green += genome_line["green shift"]
        blue += genome_line["blue shift"]
        circle(next_x, next_y, diameter, rgb(red, green, blue))

    return {
        "endx": next_x,
        "endy": next_y,
        "angle": angle,
        "last size": diameter,
        "last red": red,
        "last green": green,
        "last blue": blue,
    }


def tree(genome, parent_info, depth=0):
    if depth == len(genome):
        return

    branch_end = branch(genome[depth], parent_info)
    branch_amount = genome[depth]["branch amount"]
    max_angle = genome[depth]["max branch angle"]
    saved_angle = branch_end["angle"]

    for index in range(branch_amount):
        normalized_angle = 0
        if branch_amount != 1:
            normalized_angle = -1 + (2 / (branch_amount - 1)) * index
        child_info = branch_end.copy()
        child_info["angle"] = saved_angle + normalized_angle * max_angle
        child_info["angle diff"] = normalized_angle * max_angle
        tree(genome, child_info, depth + 1)


start_parent = {
    "endx": 250,
    "endy": 450,
    "angle": 0,
    "last size": 0,
    "last red": 0,
    "last green": 0,
    "last blue": 0,
    "angle diff": 0,
}

tree(genome, start_parent)
window.mainloop()
