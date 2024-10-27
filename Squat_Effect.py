import tkinter as tk
from tkinter import ttk


class SquatCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Seahorse Squat")
        self.geometry("300x400")
        self.resizable(False, False)

        # Create gradient background
        self.canvas = tk.Canvas(self, width=400, height=400, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.create_gradient()

        # Main container
        main_container = ttk.Frame(self)
        main_container.place(relx=0.5, rely=0.5, anchor="center")

        # Title frame with border
        title_frame = tk.Frame(
            main_container,
            bd=1,
            relief="solid",
            padx=10,
            pady=3
        )
        title_frame.pack(pady=(0, 15))

        title_label = tk.Label(
            title_frame,
            text="SEAHORSE SQUAT EFFECT\nCALCULATOR",
            font=('Arial', 11, 'bold'),
            justify='center'
        )
        title_label.pack()

        # Draft frame with border
        draft_frame = tk.Frame(
            main_container,
            bd=1,
            relief="solid",
            padx=10,
            pady=3
        )
        draft_frame.pack(pady=8, padx=20, fill="x")

        draft_label = tk.Label(
            draft_frame,
            text="DRAFT\n(Meters)",
            font=('Arial', 10),
            justify='center'
        )
        draft_label.pack()

        self.draft_var = tk.StringVar(value=" ")
        self.draft_entry = tk.Entry(
            draft_frame,
            textvariable=self.draft_var,
            justify='center',
            font=('Arial', 10)
        )
        self.draft_entry.pack(pady=3, fill="x")

        # Speed frame with border
        speed_frame = tk.Frame(
            main_container,
            bd=1,
            relief="solid",
            padx=10,
            pady=3
        )
        speed_frame.pack(pady=8, padx=20, fill="x")

        speed_label = tk.Label(
            speed_frame,
            text="SPEED\n(Knots)",
            font=('Arial', 10),
            justify='center'
        )
        speed_label.pack()

        self.speed_var = tk.StringVar(value=" ")
        self.speed_entry = tk.Entry(
            speed_frame,
            textvariable=self.speed_var,
            justify='center',
            font=('Arial', 10)
        )
        self.speed_entry.pack(pady=3, fill="x")

        # Calculate button frame with border
        button_frame = tk.Frame(
            main_container,
            bd=1,
            relief="solid",
            padx=10,
            pady=3
        )
        button_frame.pack(pady=15)

        self.calc_button = tk.Button(
            button_frame,
            text="CALCULATE SQUAT EFFECT",
            command=self.calculate_squat,
            font=('Arial', 10),
            relief="flat",
            bg="#f0f0f0"
        )
        self.calc_button.pack()

        # Result frame with border
        result_frame = tk.Frame(
            main_container,
            bd=1,
            relief="solid",
            padx=10,
            pady=3
        )
        result_frame.pack(pady=8, padx=20, fill="x")

        result_label = tk.Label(
            result_frame,
            text="SQUAT EFFECT",
            font=('Arial', 10),
            justify='center'
        )
        result_label.pack()

        self.result_value = tk.Label(
            result_frame,
            text="--",
            font=('Arial', 10),
            justify='center'
        )
        self.result_value.pack(pady=3)

        # Constants for calculation
        self.Cb = 0.54  # Block coefficient
        self.L = 162  # Length
        self.B = 38.0  # Breadth

        # Bind entry validation
        self.draft_entry.bind('<KeyRelease>', lambda e: self.validate_input(e, self.draft_var))
        self.speed_entry.bind('<KeyRelease>', lambda e: self.validate_input(e, self.speed_var))

    def validate_input(self, event, var):
        """Validate and format input in real-time"""
        value = var.get()
        # Replace comma with dot
        if ',' in value:
            value = value.replace(',', '.')
            var.set(value)

    def parse_float(self, value):
        """Parse string to float, handling both dot and comma as decimal separator"""
        try:
            # First replace comma with dot if present
            value = value.replace(',', '.')
            return float(value)
        except ValueError:
            raise ValueError("Invalid number format")

    def create_gradient(self):
        height = 400
        width = 300
        for i in range(height):
            intensity = int(240 - (i / height) * 20)
            color = f'#{intensity:02x}{intensity:02x}{intensity:02x}'
            self.canvas.create_line(0, i, width, i, fill=color)

    def calculate_squat(self):
        try:
            # Using parse_float instead of float
            draft = self.parse_float(self.draft_var.get())
            speed = self.parse_float(self.speed_var.get())

            S = (self.B * draft) / (2 * draft * self.B)
            squat = 2.4 * self.Cb * (speed ** 2) * S / 100

            self.result_value.configure(text=f"{squat:.2f} m")
        except ValueError:
            self.result_value.configure(text="Invalid input")


if __name__ == "__main__":
    app = SquatCalculator()
    app.mainloop()