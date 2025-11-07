import vector as v
import body as b
import tkinter as tk


DT = 0.01  # Time step
CANVAS_SIZE = 1000  # Canvas size for visualization


class TrisolaranSystem:
    def __init__(self):
        self.bodies = [
            b.CelestialBody(-1.0, 0.5, 0.0, -0.5, 1.0, "orange", 8),
            b.CelestialBody(1.0, -0.5, 0.0, 0.5, 1.0, "yellow", 8),
            b.CelestialBody(0.5, 1.0, -0.5, 0.0, 1.0, "red", 8),
            b.CelestialBody(0.3, 0.3, 0.2, -0.1, 0.001, "blue", 4)  ,
            b.CelestialBody(-1.0, 0.5, 0.0, -0.5, 1.0, "orange", 8),
            b.CelestialBody(1.5, -0.5, 0.0, 0.5, 1.0, "yellow", 8),
            b.CelestialBody(6.5, 1.0, -0.5, 0.0, 1.0, "red", 8),
            b.CelestialBody(-5.3, 0.3, 0.2, -0.1, 0.001, "blue", 4),
            b.CelestialBody(-4.0, 0.5, 0.0, -0.5, 1.0, "orange", 8),
            b.CelestialBody(4.0, -0.5, 0.0, 0.5, 1.0, "yellow", 8),
            b.CelestialBody(-6, 1.0, -0.5, 0.0, 1.0, "red", 8),
            b.CelestialBody(-3.3, 0.3, 0.2, -0.1, 0.001, "blue", 4)
        ]
        self.init_gui()
        self.update()
        self.root.mainloop()
    
    def init_gui(self):
        self.root = tk.Tk()
        self.root.title("Trisolaran System Simulation")
        self.canvas = tk.Canvas(self.root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black")
        self.canvas.pack()
        self.visuals = [self.canvas.create_oval(0, 0, 0, 0, fill=body.color) for body in self.bodies]
    
    def scale_coords(self, pos):
        return ((pos.x + 2) * CANVAS_SIZE / 4, (2 - pos.y) * CANVAS_SIZE / 4)
    
    def runge_kutta_step(self):
        forces = [v.Vector(0, 0) for _ in self.bodies]
        for i, body in enumerate(self.bodies):
            for j, other in enumerate(self.bodies):
                if i != j:
                    forces[i] = forces[i] + body.acceleration(other)
        for i, body in enumerate(self.bodies):
            body.update(forces[i], DT)
    
    def update(self):
        self.runge_kutta_step()
        for i, body in enumerate(self.bodies):
            x, y = self.scale_coords(body.pos)
            r = body.radius
            self.canvas.coords(self.visuals[i], x - r, y - r, x + r, y + r)
        self.root.after(10, self.update)
