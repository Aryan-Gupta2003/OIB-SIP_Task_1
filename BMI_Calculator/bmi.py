import tkinter as tk
import csv

class BMI_Calculator:
    def __init__(self, a):
        self.a = a
        a.title("BMI Calculator")

        self.label_weight = tk.Label(a, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0)

        self.label_height = tk.Label(a, text="Height (m):")
        self.label_height.grid(row=1, column=0)

        self.entry_weight = tk.Entry(a)
        self.entry_weight.grid(row=0, column=1)   

        self.entry_height = tk.Entry(a)
        self.entry_height.grid(row=1, column=1)

        self.calculate_button = tk.Label(a, text='')
        self.calculate_button.grid(row=2, column=0)

        self.calculate_button = tk.Button(a, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.bmi_label = tk.Label(a, text="")
        self.bmi_label.grid(row=5, column=0)
        self.bmi_label = tk.Label(a, text="")
        self.bmi_label.grid(row=6, column=0, columnspan=2)

        self.bmi_detail = tk.Label(a, text="")
        self.bmi_detail.grid(row=7, column=0)

        self.bmi_detail = tk.Label(a, text="")
        self.bmi_detail.grid(row=8, column=0, columnspan=2)

        self.bmi_c = tk.Label(a, text="")
        self.bmi_c.grid(row=9, column=0)

        self.bmi_c = tk.Label(a, text="BMI", font=('Helvetica', 10, 'bold'), borderwidth=1, relief="solid", background="yellow", width=15)
        self.bmi_c.grid(row=10, column=0)
        self.bmi_c = tk.Label(a, text="Classification", font=('Helvetica', 10, 'bold'), borderwidth=1, relief="solid", background="yellow", width=15)
        self.bmi_c.grid(row=10, column=1)
        self.bmi_c = tk.Label(a, text="Health Risk", font=('Helvetica', 10, 'bold'), borderwidth=1, relief="solid", background="yellow", width=15)
        self.bmi_c.grid(row=10, column=2)
        self.bmi_c = tk.Label(a, text="Under 18.5", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=11, column=0)
        self.bmi_c = tk.Label(a, text="Underweight", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=11, column=1)
        self.bmi_c = tk.Label(a, text="Minimal", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=11, column=2)
        self.bmi_c = tk.Label(a, text="18.5 - 24.9", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=12, column=0)
        self.bmi_c = tk.Label(a, text="Normal Weight", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=12, column=1)
        self.bmi_c = tk.Label(a, text="Minimal", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=12, column=2)
        self.bmi_c = tk.Label(a, text="25 - 29.9", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=13, column=0)
        self.bmi_c = tk.Label(a, text="Overweight", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=13, column=1)
        self.bmi_c = tk.Label(a, text="Increased", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=13, column=2)
        self.bmi_c = tk.Label(a, text="30 - 34.9", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=14, column=0)
        self.bmi_c = tk.Label(a, text="Obese", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=14, column=1)
        self.bmi_c = tk.Label(a, text="High", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=14, column=2)
        self.bmi_c = tk.Label(a, text="35 - 39.9", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=15, column=0)
        self.bmi_c = tk.Label(a, text="Severely Obese", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=15, column=1)
        self.bmi_c = tk.Label(a, text="Very High", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=15, column=2)
        self.bmi_c = tk.Label(a, text="40 and aboveh", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=16, column=0)
        self.bmi_c = tk.Label(a, text="Morbidly Obese", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=16, column=1)
        self.bmi_c = tk.Label(a, text="Extremly High", borderwidth=1, relief="solid", width=17)
        self.bmi_c.grid(row=16, column=2)

        self.current_id = self.get_last_id() + 1

    def get_last_id(self):
        try:
            with open('bmi_data.csv', mode='r') as file:
                reader = csv.reader(file)
                last_row = None
                for row in reader:
                    last_row = row
                if last_row:
                    return int(last_row[0])
        except FileNotFoundError:
            return 0

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)
            detail = self.get_bmi_details(bmi)
            self.bmi_label.config(text=f"Your BMI: {bmi:.2f}", font=('Helvetica', 10, 'bold'))
            self.bmi_detail.config(text=detail, font=('Helvetica', 9, 'bold'))
            self.save_data(self.current_id, weight, height, bmi)
            self.current_id += 1
        except ValueError:
            self.bmi_label.config(text="Invalid input")

    def save_data(self, id, weight, height, bmi):
        with open('bmi_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, weight, height, bmi])

    def get_bmi_details(self, bmi):
        if bmi < 18.5:
            return "Underweight: You may need to gain weight."
        elif 18.5 <= bmi < 25:
            return "Normal weight: Maintain a healthy lifestyle."
        elif 25 <= bmi < 30:
            return "Overweight: Consider losing weight for better health."
        elif 30 <= bmi < 35:
            return "Obese: Significant health risks. Consult a healthcare provider."
        elif 35 <= bmi < 40:
            return "Severely Obese: Health risks. Consult a healthcare provider (Recommended)."
        else:
            return "Morbudly Obese: High Health risks. Consult a healthcare provider immediately."

    

def main():
    root = tk.Tk()
    root.geometry("400x400")
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
