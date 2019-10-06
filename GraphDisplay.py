import tkinter as tk
import VecMath


def draw_spatial_graph(graph):
    root = tk.Tk()
    root.geometry("1200x800")
    canvas = tk.Canvas(width=1200, height=800)
    radius = 15
    for node in graph.nodes:
        pos = node.position
        canvas.create_oval(pos[0] - radius, pos[1] - radius, pos[0] + radius, pos[1] + radius, fill='red')
        canvas.create_text(pos[0], pos[1], text=str(node.id), anchor='center')
        for succ in node.successors:
            to_succ = VecMath.normal(VecMath.sub(succ.position, node.position))
            arrow_start = VecMath.add(node.position, VecMath.multiply(to_succ, radius))
            arrow_end = VecMath.sub(succ.position, VecMath.multiply(to_succ, radius))
            canvas.create_line(arrow_start[0], arrow_start[1], arrow_end[0], arrow_end[1], arrow=tk.LAST)

    canvas['bg'] = 'green'
    canvas.pack()
    root.mainloop()
