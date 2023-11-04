# Ho Ten Sinh Vien: Pham Tuan Anh MSSV 712188

import tkinter as tk

import svgwrite as svgwrite


class SVGWriter:
    def __init__(self):
        self.root = tk.Tk("diem")
        self.root.title("Thiết kế svg file")
        note = tk.Label(
            text="Tạo hình svg với setup thuộc tính bên dưới và dùng chuột click vào khung vàng \n sau đó bấm save, file được lưu ra file output \n đối với  vẽ line chỉ add toạ độ 2 điểm"
        )
        note.pack(side=tk.TOP)
        self.canvas = tk.Canvas(
            self.root, width=700, height=500, border=1, background="yellow"
        )

        self.canvas.pack()
        self.shapes = []
        self.colors = ["black", "red", "green", "blue", "yellow", "purple"]
        self.current_color = tk.StringVar(self.root)
        self.stroke_width = 1
        self.fill_color = "#FFFFFF"
        self.current_shape = tk.StringVar(self.root)
        self.current_params = {}
        self.width = 50
        self.height = 50
        self.point = [50, 50, 100, 100, 150, 50, 200, 100, 250, 50]
        self.text = ""
        self.x = 0
        self.y = 0
        frame = tk.Frame(self.root, borderwidth=5, width=700, pady=10)
        frame.pack(side=tk.TOP)
        middle_frame = tk.Frame(self.root, borderwidth=5, border=1, pady=10)
        middle_frame.pack(side=tk.TOP)
        text_frame = tk.Frame(self.root, width=700)
        text_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(self.root, pady=20)
        bottom_frame.pack(side=tk.BOTTOM)
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
        shape_inside = tk.StringVar(self.root)
        shape_label = tk.Label(frame, text="Select Shape:")
        shape_label.pack(side=tk.LEFT)
        shape_inside.set("select Shape: ")
        option_shape = tk.OptionMenu(
            frame, self.current_shape, *shapes, command=self.set_shape
        )
        option_shape.pack(side=tk.LEFT)

        # Create color picker
        # color_button = tk.Button(self.root, text="Color", command=self.pick_color)
        color_label = tk.Label(frame, text="Select Color:")
        color_label.pack(side=tk.LEFT)
        color_pick = tk.OptionMenu(
            frame, self.current_color, *self.colors, command=self.pick_color
        )
        color_pick.pack(side=tk.LEFT)
        width_label = tk.Label(frame, text="Width of object: ")
        width_label.pack(side=tk.LEFT)
        width_entry = tk.Entry(frame, width=5)
        width_entry.pack(side=tk.LEFT)
        height_label = tk.Label(frame, text="Height of object: ")
        height_label.pack(side=tk.LEFT)
        height_entry = tk.Entry(frame, width=5)
        height_entry.pack(side=tk.LEFT)

        def set_sizeObject():
            self.width = float(width_entry.get())
            self.height = float(height_entry.get())

        btn_set = tk.Button(frame, text="set Size", command=set_sizeObject)
        btn_set.pack()

        point_label = tk.Label(middle_frame, text="Them diem cho polyline vaf Polygon")
        point_label.pack(side=tk.TOP)
        x_label = tk.Label(middle_frame, text="x:")
        x_label.pack(side=tk.LEFT)
        entry_x = tk.Entry(middle_frame, width=10)
        entry_x.pack(side=tk.LEFT)
        y_label = tk.Label(middle_frame, text="y:")
        y_label.pack(side=tk.LEFT)
        entry_y = tk.Entry(middle_frame, width=10)
        entry_y.pack(side=tk.LEFT)

        def add_point():
            first = float(entry_x.get())
            second = float(entry_y.get())
            self.point.append(first)
            self.point.append(second)

        add_point_button = tk.Button(middle_frame, text="add point", command=add_point)
        add_point_button.pack(side=tk.LEFT)
        clear_point_button = tk.Button(
            middle_frame, text="reset Point", command=self.clear_point
        )
        clear_point_button.pack(side=tk.LEFT)
        title_text = tk.Label(text_frame, text="Setup thông tin tạo text", underline=2)
        title_text.pack(side=tk.TOP)
        text_label = tk.Label(text_frame, text="Nhập tạo text")
        text_label.pack(side=tk.LEFT)
        text_entry = tk.Entry(text_frame, width=40)
        text_entry.pack(side=tk.LEFT)

        def setText():
            self.text = text_entry.get()

        text_btn = tk.Button(text_frame, text="set Text", command=setText)
        text_btn.pack(side=tk.LEFT)

        def clear_text():
            self.text = ""

        text_clear_btn = tk.Button(text_frame, text="clear Text", command=clear_text)
        text_clear_btn.pack(side=tk.LEFT)

        save_button = tk.Button(
            bottom_frame,
            text="Save",
            command=self.save_svg,
            width=5,
            height=2,
            padx=4,
            highlightcolor="blue",
        )
        save_button.pack()

        self.setInputlayout()

    def clear_point(self):
        self.point.clear()

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

    def draw_shape(self, event):
        # draw on screen
        if self.current_shape is None:
            return

        if self.current_shape == "Rectangle":
            x1, y1 = event.x - self.width / 2, event.y - self.height / 2
            x2, y2 = event.x + self.width / 2, event.y + self.height / 2
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

        if self.current_shape == "Circle":
            x1, y1 = event.x - self.width / 2, event.y - self.width / 2
            x2, y2 = event.x + self.width / 2, event.y + self.width / 2
            params = {
                "type": "Circle",
                "cx": event.x,
                "cy": event.y,
                "r": self.width / 2,
                "fill": self.current_color,
                "stroke": self.current_color,
            }
            self.shapes.append(params)
            rect_id = self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color)
            self.canvas.tag_bind(
                rect_id, "<Button-3>", lambda event: self.delete_shape(rect_id)
            )
        if self.current_shape == "Ellipse":
            x1, y1 = event.x - self.width / 2, event.y - self.height / 2
            x2, y2 = event.x + self.width / 2, event.y + self.height / 2
            params = {
                "type": "Circle",
                "cx": event.x,
                "cy": event.y,
                "rx": self.width / 2,
                "ry": self.height / 2,
                "fill": self.current_color,
                "stroke": self.current_color,
            }
            self.shapes.append(params)
            rect_id = self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color)
            self.canvas.tag_bind(
                rect_id, "<Button-3>", lambda event: self.delete_shape(rect_id)
            )
        if self.current_shape == "Polyline" or self.current_shape == "Line":
            newlistpoint = []
            midx = 0
            midy = 0
            listPoint = [(xp, yp) for xp, yp in zip(self.point[::2], self.point[1::2])]
            for xp, yp in listPoint:
                midx += xp
                midy += yp
            midx = midx / len(listPoint)
            midy = midy / len(listPoint)
            for xp, yp in listPoint:
                xc, yc = midx + xp, midy + yp
                newlistpoint.append((xc, yc))
            params = {"points": newlistpoint}
            self.shapes.append(params)
            rect_id = self.canvas.create_line(newlistpoint, fill=self.current_color)
            self.canvas.tag_bind(
                rect_id, "<Button-3>", lambda event: self.delete_shape(rect_id)
            )

        if self.current_shape == "Polygon":
            newlistpoint = []
            midx = 0
            midy = 0
            listPoint = [(xp, yp) for xp, yp in zip(self.point[::2], self.point[1::2])]
            for xp, yp in listPoint:
                midx += xp
                midy += yp
            midx = midx / len(listPoint)
            midy = midy / len(listPoint)
            for xp, yp in listPoint:
                xc, yc = midx + xp, midy + yp
                newlistpoint.append((xc, yc))
            params = {"points": newlistpoint}
            self.shapes.append(params)
            rect_id = self.canvas.create_polygon(newlistpoint, fill=self.current_color)
            self.canvas.tag_bind(
                rect_id, "<Button-3>", lambda event: self.delete_shape(rect_id)
            )
        if self.current_shape == "Text":
            x1, y1 = event.x - self.width / 2, event.y - self.height / 2
            x2, y2 = event.x + self.width / 2, event.y + self.height / 2
            params = {
                "type": "Text",
                "x": event.x,
                "y": event.y,
                "text": self.text,
                "fill": self.current_color,
            }
            self.shapes.append(params)
            rect_id = self.canvas.create_text(
                (event.x, event.y), fill=self.current_color, text=self.text
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

    def setInputlayout(self):
        pass


if __name__ == "__main__":
    writer = SVGWriter()
    writer.canvas.bind("<Button-1>", writer.draw_shape)
    writer.canvas.mainloop()
