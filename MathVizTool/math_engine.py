import numpy as np

class MathEngine:
    @staticmethod
    def add_vectors(v1, v2):
        """Adds two 3D vectors."""
        return np.add(v1, v2)

    @staticmethod
    def transform_matrix(matrix, vector):
        """Applies a matrix transformation to a vector."""
        return np.dot(matrix, vector)

    @staticmethod
    def generate_surface(func_str, x_range=(-5, 5), y_range=(-5, 5), points=50):
        """
        Generates X, Y, Z coordinates for a 3D surface from a function string.
        Safe evaluation is a complex topic, for this demo we will use a restricted eval.
        """
        x = np.linspace(x_range[0], x_range[1], points)
        y = np.linspace(y_range[0], y_range[1], points)
        X, Y = np.meshgrid(x, y)
        
        # Safe dictionary for eval
        allowed_names = {
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "sqrt": np.sqrt, "exp": np.exp, "log": np.log,
            "pi": np.pi, "e": np.e, "power": np.power,
            "X": X, "Y": Y
        }
        
        try:
            # Replace x and y with X and Y for meshgrid compatibility if user types lowercase
            # This is a basic replacement, a real parser would be better but this suffices for a demo
            clean_func = func_str.replace("x", "X").replace("y", "Y")
            Z = eval(clean_func, {"__builtins__": {}}, allowed_names)
            return X, Y, Z
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return X, Y, np.zeros_like(X)

    @staticmethod
    def calculate_gradient(Z, spacing):
        """Calculates the gradient of the surface."""
        dy, dx = np.gradient(Z, spacing)
        return dx, dy

    @staticmethod
    def explain_function(func_str):
        """Returns a simple text explanation of the function."""
        explanation = "This is a 3D surface plot defined by z = f(x, y)."
        
        if "sin" in func_str or "cos" in func_str:
            explanation += "\n- It contains periodic elements (waves), likely creating a ripple or hill-valley pattern."
        if "x**2" in func_str and "y**2" in func_str:
            if "+" in func_str:
                explanation += "\n- It has quadratic terms added together, suggesting a paraboloid (bowl shape)."
            elif "-" in func_str:
                explanation += "\n- It has quadratic terms subtracted, suggesting a hyperbolic paraboloid (saddle shape)."
        if "sqrt" in func_str:
            explanation += "\n- The square root dampens the growth, potentially creating a cone-like structure."
        if "exp" in func_str:
            explanation += "\n- It involves exponential growth or decay."
            
        return explanation
