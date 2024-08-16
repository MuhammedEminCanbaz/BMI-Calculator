from tkinter import *

# window is created and it's properties are defined
window = Tk()
window.title("BMI Calculator")
window.minsize(350, 400)
window.config(padx=30, pady=50)

def BMI_calculate():
    """to control the value's that user entered, try-expect method is used.
    If user enters a string or a negative number or forget to enter a value
     and keep an entry empty, our program will show a feedback
    that is aimed to make user enter correct values.
    """
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            result_label.config(text="Lütfen geçerli bir değer girin")
        else:
            result = weight / (height * height)
            if result < 18.5:
                result_label.config(text=f"BMI : {result:.2f} you are too thin")
            elif result >= 18.5 and result < 24.9:
                result_label.config(text=f"BMI : {result:.2f} you are normal")
            elif result >= 24.9 and result < 39.9:
                result_label.config(text=f"BMI : {result:.2f} you are overweight")
            else:
                result_label.config(text=f"BMI : {result:.2f} you are obese")
    except ValueError:
        if not weight_entry.get() or not height_entry.get():
            result_label.config(text="Lütfen tüm alanları doldurduğunuzdan emin olun")
        else:
            result_label.config(text="Lütfen geçerli bir değer girin")

# weight label is created and some of it's properties are defined
weight_label = Label(text="Please Enter Your Weight (kg)", font=('Arial', 8, "normal"))
weight_label.config(width=35, pady=5)
weight_label.pack(side="top", pady=5)

# weight entry is created and some of it's properties are defined
weight_entry = Entry()
weight_entry.config(width=35)
weight_entry.pack(side="top", pady=5)

# height label is created and some of it's properties are defined
height_label = Label(text="Please Enter Your Height (m)", font=('Arial', 8, "normal"))
height_label.config(width=35)
height_label.config(pady=5)
height_label.pack(side="top", pady=5)

# height entry is created and some of it's properties are defined
height_entry = Entry()
height_entry.config(width=35)
height_entry.pack(side="top", pady=5)

# The button which calculates the BMI Score is created and some of it's properties defined
calculate_button = Button(text="Calculate", command=BMI_calculate)
calculate_button.config()
calculate_button.pack(side="top", pady=5)

# The result label is created and it's first value is "Result"
result_label = Label(text="Result")
result_label.config(width=35)
result_label.pack(side="top", pady=5)

window.mainloop()
