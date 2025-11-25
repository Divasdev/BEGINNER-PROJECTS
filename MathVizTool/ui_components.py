import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from math_engine import MathEngine

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, command_callback):
        super().__init__(master, width=250, corner_radius=0)
        self.command_callback = command_callback
        
        self.logo_label = ctk.CTkLabel(self, text="MathVizTool", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Tabview for Modes
        self.tabview = ctk.CTkTabview(self, width=220)
        self.tabview.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.tabview.add("Linear Algebra")
        self.tabview.add("Calculus")
        
        self.setup_linear_algebra_tab()
        self.setup_calculus_tab()

    def setup_linear_algebra_tab(self):
        tab = self.tabview.tab("Linear Algebra")
        
        self.v1_label = ctk.CTkLabel(tab, text="Vector 1 (x,y,z)")
        self.v1_label.pack(pady=5)
        self.v1_entry = ctk.CTkEntry(tab, placeholder_text="1, 2, 3")
        self.v1_entry.pack(pady=5)
        
        self.v2_label = ctk.CTkLabel(tab, text="Vector 2 (x,y,z)")
        self.v2_label.pack(pady=5)
        self.v2_entry = ctk.CTkEntry(tab, placeholder_text="4, 5, 6")
        self.v2_entry.pack(pady=5)
        
        self.calc_btn = ctk.CTkButton(tab, text="Calculate", command=self.on_calculate)
        self.calc_btn.pack(pady=10)

    def setup_calculus_tab(self):
        tab = self.tabview.tab("Calculus")
        
        self.func_label = ctk.CTkLabel(tab, text="Function z = f(x,y)")
        self.func_label.pack(pady=5)
        self.func_entry = ctk.CTkEntry(tab, placeholder_text="sin(sqrt(x**2 + y**2))")
        self.func_entry.pack(pady=5)
        
        self.plot_btn = ctk.CTkButton(tab, text="Plot Surface", command=self.on_plot)
        self.plot_btn.pack(pady=10)
        
        self.explanation_label = ctk.CTkLabel(tab, text="Explanation:", anchor="w")
        self.explanation_label.pack(pady=(10, 0), fill="x")
        
        self.explanation_text = ctk.CTkTextbox(tab, height=150)
        self.explanation_text.pack(pady=5, fill="x")

    def on_calculate(self):
        try:
            v1 = np.fromstring(self.v1_entry.get(), sep=',')
            v2 = np.fromstring(self.v2_entry.get(), sep=',')
            if v1.size == 3 and v2.size == 3:
                self.command_callback("vector_add", (v1, v2))
            else:
                print("Invalid vector input")
        except ValueError:
            print("Error parsing vectors")

    def on_plot(self):
        func = self.func_entry.get()
        if func:
            self.command_callback("surface_plot", func)
            
            # Update explanation
            explanation = MathEngine.explain_function(func)
            self.explanation_text.delete("0.0", "end")
            self.explanation_text.insert("0.0", explanation)

class PlotArea(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.figure.patch.set_facecolor('#2b2b2b') # Match dark theme
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.ax.set_facecolor('#2b2b2b')
        
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        
        # Add Navigation Toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=1, column=0, sticky="ew")
        
        self.setup_axes()

    def setup_axes(self):
        self.ax.clear()
        self.ax.set_facecolor('#2b2b2b')
        self.ax.tick_params(colors='white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)

    def plot_vectors(self, v1, v2, v3):
        self.setup_axes()
        origin = np.array([0, 0, 0])
        self.ax.quiver(*origin, *v1, color='cyan', label='V1')
        self.ax.quiver(*origin, *v2, color='magenta', label='V2')
        self.ax.quiver(*origin, *v3, color='yellow', label='Result')
        
        max_val = np.max(np.abs([v1, v2, v3]))
        self.ax.set_xlim([-max_val, max_val])
        self.ax.set_ylim([-max_val, max_val])
        self.ax.set_zlim([-max_val, max_val])
        self.ax.legend()
        self.canvas.draw()

    def plot_surface(self, X, Y, Z):
        self.setup_axes()
        self.ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
        self.canvas.draw()
