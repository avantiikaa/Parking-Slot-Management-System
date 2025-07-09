from tkinter import *
from tkinter import messagebox, ttk
from database import insert_vehicle, fetch_vehicles

# --- Login Window ---
def login():
    if entry_username.get() == "admin" and entry_password.get() == "password":
        login_win.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login", "Invalid credentials")

login_win = Tk()
login_win.title("Admin Login")
login_win.geometry("300x180")

Label(login_win, text="Username :").pack(pady=(10,0))
entry_username = Entry(login_win)
entry_username.pack()

Label(login_win, text="Password :").pack(pady=(10,0))
entry_password = Entry(login_win, show="*")
entry_password.pack()

Button(login_win, text="Login", bg="green", fg="white", command=login).pack(pady=10)

# --- Main Window ---
def open_main_window():
    root = Tk()
    root.title("Parking Management")

    # Left Menu
    menu_frame = Frame(root, bg="#8b7d7b")
    menu_frame.pack(side=LEFT, fill=Y)

    Button(menu_frame, text="Home", width=20, command=show_home).pack(pady=2)
    Button(menu_frame, text="Add Vehicle", width=20, command=show_add_vehicle).pack(pady=2)
    Button(menu_frame, text="History", width=20, command=show_history).pack(pady=2)

    # Main Content
    global content_frame
    content_frame = Frame(root, bg="black")
    content_frame.pack(side=LEFT, fill=BOTH, expand=True)

    def clear_frame():
        for widget in content_frame.winfo_children():
            widget.destroy()

    def show_home():
        clear_frame()
        Label(content_frame, text="Parking Slots Overview", fg="white", bg="black").pack(pady=20)

    def show_add_vehicle():
        clear_frame()

        Label(content_frame, text="Name:", fg="white", bg="black").grid(row=0, column=0, padx=5, pady=5)
        e_name = Entry(content_frame)
        e_name.grid(row=0, column=1, padx=5, pady=5)

        Label(content_frame, text="Mobile:", fg="white", bg="black").grid(row=1, column=0, padx=5, pady=5)
        e_mobile = Entry(content_frame)
        e_mobile.grid(row=1, column=1, padx=5, pady=5)

        Label(content_frame, text="Vehicle No:", fg="white", bg="black").grid(row=2, column=0, padx=5, pady=5)
        e_vehicle_no = Entry(content_frame)
        e_vehicle_no.grid(row=2, column=1, padx=5, pady=5)

        Label(content_frame, text="Vehicle Type:", fg="white", bg="black").grid(row=3, column=0, padx=5, pady=5)
        vehicle_type_var = StringVar()
        vehicle_type = OptionMenu(content_frame, vehicle_type_var, "2 Wheeler", "4 Wheeler")
        vehicle_type.grid(row=3, column=1, padx=5, pady=5)
        vehicle_type_var.set("2 Wheeler")

        def save_vehicle():
            insert_vehicle(
                e_name.get(),
                e_mobile.get(),
                e_vehicle_no.get(),
                vehicle_type_var.get()
            )
            messagebox.showinfo("Saved", "Vehicle added successfully.")

        Button(content_frame, text="Add Vehicle", bg="green", fg="white", command=save_vehicle).grid(row=4, column=0, columnspan=2, pady=10)

    def show_history():
        clear_frame()
        Label(content_frame, text="History", fg="white", bg="black").pack(pady=5)

        cols = ("ID","Name","Vehicle No","Mobile","Type","Entry Time")
        tree = ttk.Treeview(content_frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill=BOTH, expand=True)

        for row in fetch_vehicles():
            tree.insert("", END, values=row)

    show_home()
    root.mainloop()

login_win.mainloop()
