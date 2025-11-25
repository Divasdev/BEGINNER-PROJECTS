import customtkinter as ctk
from ui_components import Sidebar, PlotArea
from math_engine import MathEngine

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MathVizTool - Linear Algebra & Calculus Visualization")
        self.geometry("1100x700")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self, self.handle_command)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.plot_area = PlotArea(self)
        self.plot_area.grid(row=0, column=1, sticky="nsew")

    def handle_command(self, command, data):
        if command == "vector_add":
            v1, v2 = data
            v3 = MathEngine.add_vectors(v1, v2)
            self.plot_area.plot_vectors(v1, v2, v3)
        elif command == "surface_plot":
            func_str = data
            X, Y, Z = MathEngine.generate_surface(func_str)
            self.plot_area.plot_surface(X, Y, Z)

if __name__ == "__main__":
    app = App()
    app.mainloop()
