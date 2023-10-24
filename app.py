import tkinter as tk
from typing import List

import svgwrite


class SVGWriter:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.shapes = []
        self.colors = ["black", "red", "green", "blue", "yellow", "purple"]
        self.current_color = ""
        self.current_shape = ""
        self.current_params = {}

        # Create buttons for each shape
        shapes: list[str] = [
            "Rectangle",
            "Circle",
            "Ellipse",
            "Line",
            "Polyline",
            "Polygon",
            "Text",
        ]
        # for i, shape in enumerate(shapes):
        #     # button = tk.Button(
        #     #     self.root, self.current_shape, *shapes, command=self.set_shape
        #     # )
        #     button = tk.Radiobutton(
        #         self.root, text=shape, value=shape, command=lambda: self.set_shape
        #     )
        #     button.pack(side=tk.LEFT)
        shape_inside = tk.StringVar(self.root)
        shape_inside.set("select Shape: ")
        option_shape = tk.OptionMenu(self.root, shape_inside, *shapes, command=self.set_shape)
        option_shape.pack()

        # Create color picker
        # color_button = tk.Button(self.root, text="Color", command=self.pick_color)
        color_inside = tk.StringVar(self.root)
        color_pick = tk.OptionMenu(self.root, color_inside, *self.colors, command=self.pick_color)
        color_pick.pack()

        insert_button = tk.Button(self.root, text="Insert Shape", command=self.draw_shape)
        insert_button.pack()

        # Create save button
        save_button = tk.Button(self.root, text="Save", command=self.save_svg)
        save_button.pack()

    def set_shape(self, shape):
        self.current_shape = shape

    def pick_color(self, color):
        self.current_color = color

    def save_svg(self):
        dwg = svgwrite.Drawing("output.svg")
        for shape in self.shapes:
            if shape["type"] == "Rectangle":
                dwg.add(
                    dwg.rect(
                        insert=(shape["x"], shape["y"]),
                        size=(shape["width"], shape["height"]),
                        fill=shape["fill"],
                        stroke=shape["stroke"],
                    )
                )
            elif shape["type"] == "Circle":
                dwg.add(
                    dwg.circle(
                        center=(shape["cx"], shape["cy"]),
                        r=shape["r"],
                        fill=shape["fill"],
                        stroke=shape["stroke"],
                    )
                )
            elif shape["type"] == "Ellipse":
                dwg.add(
                    dwg.ellipse(
                        center=(shape["cx"], shape["cy"]),
                        r=(shape["rx"], shape["ry"]),
                        fill=shape["fill"],
                        stroke=shape["stroke"],
                    )
                )
            elif shape["type"] == "Line":
                dwg.add(
                    dwg.line(
                        start=(shape["x1"], shape["y1"]),
                        end=(shape["x2"], shape["y2"]),
                        stroke=shape["stroke"],
                    )
                )
            elif shape["type"] == "Polyline":
                points = [
                    (x, y) for x, y in zip(shape["points"][::2], shape["points"][1::2])
                ]
                dwg.add(
                    dwg.polyline(points=points, fill="none", stroke=shape["stroke"])
                )
            elif shape["type"] == "Polygon":
                points = [
                    (x, y) for x, y in zip(shape["points"][::2], shape["points"][1::2])
                ]
                dwg.add(
                    dwg.polygon(
                        points=points, fill=shape["fill"], stroke=shape["stroke"]
                    )
                )
            elif shape["type"] == "Text":
                dwg.add(
                    dwg.text(
                        shape["text"],
                        insert=(shape["x"], shape["y"]),
                        fill=shape["fill"],
                    )
                )
        dwg.save()

    def draw_shape(self):
        if self.current_shape is None:
            return

        if self.current_shape == "Rectangle":
            x1, y1 = 0 - 50, 0 - 50
            x2, y2 = 0 + 50, 0 + 50
            width = x2 - x1
            height = y2 - y1
            params = {
                "type": "Rectangle",
                "x": x1,
                "y": y1,
                "width": width,
                "height": height,
                "fill": self.current_color,
                "stroke": self.current_color,
            }
            self.shapes.append(params)
            rect_id = self.canvas.create_rectangle(
                x1, y1, x2, y2, fill=self.current_color
            )
            self.canvas.tag_bind(
                rect_id, "<Button-3>", lambda event: self.delete_shape(rect_id)
            )

    def delete_shape(self, id):
        index = None
        for i in range(len(self.shapes)):
            if id in self.canvas.find_withtag(i + 1):
                index = i
                break

        if index is not None:
            del self.shapes[index]
            self.canvas.delete(id)