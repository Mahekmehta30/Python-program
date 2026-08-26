import tkinter as tk
from tkinter import ttk, messagebox


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("600x650")
root.resizable(False, False)


# =====================================================
# VARIABLES
# =====================================================

employee_id = tk.StringVar()
employee_name = tk.StringVar()
dob = tk.StringVar()
gender = tk.StringVar()
email = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
department = tk.StringVar()
designation = tk.StringVar()
salary = tk.StringVar()


# =====================================================
# TITLE
# =====================================================

title = tk.Label(
    root,
    text="Employee Registration Form",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)


frame = tk.Frame(root)
frame.pack(pady=10)


# =====================================================
# 1. EMPLOYEE ID
# =====================================================

tk.Label(
    frame,
    text="Employee ID:",
    font=("Arial", 11)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=employee_id,
    width=35
).grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 2. EMPLOYEE NAME
# =====================================================

tk.Label(
    frame,
    text="Employee Name:",
    font=("Arial", 11)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=employee_name,
    width=35
).grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 3. DATE OF BIRTH
# =====================================================

tk.Label(
    frame,
    text="Date of Birth:",
    font=("Arial", 11)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=dob,
    width=35
).grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 4. GENDER
# =====================================================

tk.Label(
    frame,
    text="Gender:",
    font=("Arial", 11)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

gender_frame = tk.Frame(frame)
gender_frame.grid(
    row=3,
    column=1,
    sticky="w"
)

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender,
    value="Male"
).pack(side="left")

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender,
    value="Female"
).pack(side="left")


# =====================================================
# 5. EMAIL
# =====================================================

tk.Label(
    frame,
    text="Email:",
    font=("Arial", 11)
).grid(
    row=4,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=email,
    width=35
).grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 6. PHONE
# =====================================================

tk.Label(
    frame,
    text="Phone:",
    font=("Arial", 11)
).grid(
    row=5,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=phone,
    width=35
).grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 7. ADDRESS
# =====================================================

tk.Label(
    frame,
    text="Address:",
    font=("Arial", 11)
).grid(
    row=6,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=address,
    width=35
).grid(
    row=6,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 8. DEPARTMENT
# =====================================================

tk.Label(
    frame,
    text="Department:",
    font=("Arial", 11)
).grid(
    row=7,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

department_box = ttk.Combobox(
    frame,
    textvariable=department,
    values=[
        "HR",
        "IT",
        "Finance",
        "Sales",
        "Marketing"
    ],
    width=32,
    state="readonly"
)

department_box.grid(
    row=7,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 9. DESIGNATION
# =====================================================

tk.Label(
    frame,
    text="Designation:",
    font=("Arial", 11)
).grid(
    row=8,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=designation,
    width=35
).grid(
    row=8,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# 10. SALARY
# =====================================================

tk.Label(
    frame,
    text="Salary:",
    font=("Arial", 11)
).grid(
    row=9,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

tk.Entry(
    frame,
    textvariable=salary,
    width=35
).grid(
    row=9,
    column=1,
    padx=10,
    pady=8
)


# =====================================================
# REGISTER FUNCTION
# =====================================================

def register_employee():

    # Check required fields
    if employee_id.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Employee ID."
        )
        return

    if employee_name.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Employee Name."
        )
        return

    if dob.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Date of Birth."
        )
        return

    if gender.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select Gender."
        )
        return

    if email.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Email."
        )
        return

    if phone.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Phone."
        )
        return

    if address.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Address."
        )
        return

    if department.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select Department."
        )
        return

    if designation.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Designation."
        )
        return

    if salary.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Salary."
        )
        return


    # Check salary
    try:
        float(salary.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Salary must contain numbers only."
        )
        return


    # =================================================
    # SUCCESS MESSAGE WITH DATA
    # =================================================

    messagebox.showinfo(
        "Registration Successful",
        f"""
Employee Registered Successfully!

Employee ID : {employee_id.get()}
Name        : {employee_name.get()}
DOB         : {dob.get()}
Gender      : {gender.get()}
Email       : {email.get()}
Phone       : {phone.get()}
Address     : {address.get()}
Department  : {department.get()}
Designation : {designation.get()}
Salary      : ₹{salary.get()}
"""
    )


    # Clear form after successful registration
    clear_form()


# =====================================================
# CLEAR FUNCTION
# =====================================================

def clear_form():

    employee_id.set("")
    employee_name.set("")
    dob.set("")
    gender.set("")
    email.set("")
    phone.set("")
    address.set("")
    department.set("")
    designation.set("")
    salary.set("")


# =====================================================
# BUTTONS
# =====================================================

button_frame = tk.Frame(root)
button_frame.pack(pady=20)


# Register Button
tk.Button(
    button_frame,
    text="Register",
    width=15,
    font=("Arial", 11, "bold"),
    command=register_employee
).pack(
    side="left",
    padx=10
)


# Clear Button
tk.Button(
    button_frame,
    text="Clear",
    width=15,
    font=("Arial", 11),
    command=clear_form
).pack(
    side="left",
    padx=10
)


# =====================================================
# RUN APPLICATION
# =====================================================

root.mainloop()