import tkinter as tk
import VecMath


class GraphDisplay:
    def __init__(self, graph, path=None):
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.root.config(bg='white')
        self.canvas = tk.Canvas(width=1200, height=800)
        self.canvas.config(bg='white')
        self.radius = 15
        for node in graph.nodes:
            pos = node.position
            self.canvas.create_oval(pos[0] - self.radius, pos[1] - self.radius, pos[0] + self.radius, pos[1] + self.radius, fill='red')
            self.canvas.create_text(pos[0], pos[1], text=str(node.id), anchor='center')
            for succ in node.successors:
                to_succ = VecMath.normal(VecMath.sub(succ.position, node.position))
                arrow_start = VecMath.add(node.position, VecMath.multiply(to_succ, self.radius))
                arrow_end = VecMath.sub(succ.position, VecMath.multiply(to_succ, self.radius))
                self.canvas.create_line(arrow_start[0], arrow_start[1], arrow_end[0], arrow_end[1], arrow=tk.LAST)

        if path is not None:
            self.path_lines = []
            for i in range(1, len(path)):
                a_to_b = VecMath.normal(VecMath.sub(path[i].position, path[i - 1].position))
                arrow_start = VecMath.add(path[i - 1].position, VecMath.multiply(a_to_b, self.radius))
                arrow_end = VecMath.sub(path[i].position, VecMath.multiply(a_to_b, self.radius))
                self.path_lines.append(
                    self.canvas.create_line(arrow_start[0], arrow_start[1], arrow_end[0], arrow_end[1], arrow=tk.LAST,
                                            dash=(2, 2), fill='yellow', width=10))
            self.canvas.update()

        self.canvas['bg'] = 'green'
        self.canvas.pack()
        self.root.mainloop()

    def highlight_path(self, path):
        pass



