import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from PIL import Image, ImageTk  # 🆕 For images
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import messagebox
import threading
import time

# Function to validate the key
def validate_key():
    key = key_entry.get()  # Get the value entered by the user
    if key != "ZAFONIX-1234":
        messagebox.showerror("Invalid Key", "The key you entered is incorrect.")
        root.quit()  # Close the app if the key is invalid
    else:
        root.deiconify()  # Show the main window if the key is valid

# Function to create the key window
def create_key_window():
    root.withdraw()  # Hide the root window initially

    key_window = tk.Toplevel(root)
    key_window.title("Enter Key")
    key_window.geometry("400x200")
    key_window.configure(bg="#f7f5f2")

    tk.Label(key_window, text="Enter Key to Access Tool:", font=("Helvetica", 14, "bold"), bg="#f7f5f2", fg="#d63384").pack(pady=20)

    global key_entry
    key_entry = tk.Entry(key_window, font=("Helvetica", 12), show="*", bd=2, relief="solid", width=20)
    key_entry.pack(pady=10)

    key_button = tk.Button(key_window, text="Submit", font=("Helvetica", 12, "bold"), command=lambda: validate_key(), relief="raised", bd=5, bg="#d63384", fg="white")
    key_button.pack(pady=20)

    key_window.mainloop()

# Function to create the main window
def create_main_window():
    global root, process_button
    root = tk.Tk()
    root.title("ZAFONIX - Personalized Medicine Guide")
    root.geometry("1000x750")
    root.configure(bg="#f7f5f2")  # Light pastel background color

    # Header with modern font and centered title
    header_frame = tk.Frame(root, bg="#d63384", pady=20)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(header_frame, text="ZAFONIX - Personalized Medicine Guide", font=("Helvetica", 18, "bold"), fg="white", bg="#d63384")
    header_label.pack()

    # Add a stylish processing button
    process_button = tk.Button(root, text="Start Processing", font=("Helvetica", 14, "bold"), command=start_processing, relief="raised", bd=5, bg="#4CAF50", fg="white", width=20)
    process_button.pack(pady=50)

    root.mainloop()

# Function to start processing
def start_processing():
    # Disable the button to avoid further clicks
    process_button.config(state="disabled", text="Processing...")
    
    # Simulate a long-running task using a thread
    processing_thread = threading.Thread(target=long_running_task)
    processing_thread.start()

# Function to simulate a long-running task
def long_running_task():
    time.sleep(3)  # Simulate a 3-second delay (e.g., loading a dataset or processing)

    # After the task is done, re-enable the button and update the text
    root.after(0, update_button_after_processing)

# Function to update the button after processing
def update_button_after_processing():
    process_button.config(state="normal", text="Start Processing")
    messagebox.showinfo("Task Complete", "Processing is complete!")

# First, create the main window but keep it hidden
root = tk.Tk()
create_key_window()

# Load the dataset
file_path = "C:/Users/GCA/Downloads/DrugBank Project/DrugsList.xlsx"
df = pd.read_excel(file_path)

def create_main_window():
    global root, entry, approved_var, experimental_var, investigational_var
    
    root = tk.Tk()
    root.title("ZAFONIX - Personalized Medicine Guide")
    root.geometry("1000x750")  
    root.configure(bg="#ffe6f2")  

    # 🏥 Header Section
    header_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=10, relief=tk.RIDGE, borderwidth=2)
    header_frame.pack(pady=10, padx=10, fill=tk.X)

    tk.Label(header_frame, text="🔬 ZAFONIX - Personalized Medicine Guide ", font=("Arial", 16, "bold"), bg="#ffffff", fg="#d63384").pack()
    tk.Label(header_frame, text="Providing clinicians guidance on targeted therapies based on genetic test results.",
             font=("Arial", 10), bg="#ffffff", fg="#333").pack()
    tk.Label(header_frame, text="Developed by Zarlish Attique", font=("Arial", 9, "italic"), bg="#ffffff", fg="#777").pack()

    # 🔍 Search Section
    search_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, borderwidth=2)
    search_frame.pack(pady=10, padx=10, fill=tk.X)

    tk.Label(search_frame, text="Enter Disease, Drug Name, or Gene ID:", font=("Arial", 10, "bold"), bg="#ffffff", fg="#d63384").pack(pady=5)
    entry = tk.Entry(search_frame, width=50, font=("Arial", 10), bg="#ffe6f2")
    entry.pack(pady=5)

    # Checkboxes for filtering
    approved_var = tk.BooleanVar()
    experimental_var = tk.BooleanVar()
    investigational_var = tk.BooleanVar()

    tk.Checkbutton(search_frame, text="FDA Approved Drugs", variable=approved_var, bg="#ffffff", font=("Arial", 9), fg="#d63384").pack(anchor="w")
    tk.Checkbutton(search_frame, text="Experimental Drugs", variable=experimental_var, bg="#ffffff", font=("Arial", 9), fg="#d63384").pack(anchor="w")
    tk.Checkbutton(search_frame, text="Investigational Drugs", variable=investigational_var, bg="#ffffff", font=("Arial", 9), fg="#d63384").pack(anchor="w")

    tk.Button(search_frame, text="Search", command=search_drug, font=("Arial", 10, "bold"), bg="#d63384", fg="white", padx=15, pady=5).pack(pady=10)

    # 🖼️ Scientist Images (Adjusted for better spacing and centralization)
    scientist_frame = tk.Frame(root, bg="#ffe6f2")
    scientist_frame.pack(pady=25, padx=25)

    scientist_images = [
        "C:/Users/GCA/Downloads/sc1.jpeg",
        "C:/Users/GCA/Downloads/sc2.jpeg",
        "C:/Users/GCA/Downloads/sc3.jpeg",
        "C:/Users/GCA/Downloads/sc4.jpeg",
        "C:/Users/GCA/Downloads/SC5.jpeg"
    ]

    image_labels = []
    for img_path in scientist_images:
        try:
            image = Image.open(img_path)
            image = image.resize((180, 180), Image.LANCZOS)  # Adjusted size
            img = ImageTk.PhotoImage(image)
            img_label = tk.Label(scientist_frame, image=img, bg="#ffe6f2")
            img_label.image = img
            image_labels.append(img_label)
        except Exception as e:
            print(f"Could not load image {img_path}: {e}")

    # Pack images in a centered layout
    for i, img_label in enumerate(image_labels):
        img_label.grid(row=0, column=i, padx=20, pady=10)  # Adjusted spacing

    root.mainloop()


def search_drug():
    query = entry.get().lower()
    if not query:
        messagebox.showinfo("Input Error", "PLEASE ENTER A VALID GENE OR DRUGID.")
        return

    filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]

    if approved_var.get():
        filtered_df = filtered_df[filtered_df['Approved'] == 1.0]
    if experimental_var.get():
        filtered_df = filtered_df[filtered_df['Experimental'] == 1.0]
    if investigational_var.get():
        filtered_df = filtered_df[filtered_df['Investigational'] == 1.0]

    if filtered_df.empty:
        messagebox.showinfo("No Results", "No matching drugs found.")
    else:
        detail_window = tk.Toplevel(root)
        detail_window.title("ZAFONIX - Personalized Medicine Guide  - Search Results")
        detail_window.geometry("1100x850")
        detail_window.configure(bg="#ffe6f2")

        # 🛠️ Scrollable Table
        table_frame = tk.Frame(detail_window)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tree_scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        tree_scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)

        tree = ttk.Treeview(table_frame, columns=list(filtered_df.columns), show="headings",
                            yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

        tree_scroll_y.config(command=tree.yview)
        tree_scroll_x.config(command=tree.xview)

        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        for col in filtered_df.columns:
            tree.heading(col, text=col, anchor="center")
            tree.column(col, width=150, anchor="center")

        for _, row in filtered_df.iterrows():
            tree.insert("", tk.END, values=list(row))

        # 📉 Graphs with Smaller Font Size
        fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), constrained_layout=True)  # ✅ Added constrained_layout for better spacing

        # Set font sizes for better readability
        title_font = 9
        label_font = 8
        tick_font = 7

        counts = filtered_df[['Approved', 'Experimental', 'Investigational']].sum()
        axes[0].bar(counts.index, counts.values, color=['#ff69b4', '#ffb6c1', '#ff1493'])
        axes[0].set_title("Drug Types Distribution", fontsize=title_font)
        axes[0].set_ylabel("Count", fontsize=label_font)
        axes[0].tick_params(axis='both', labelsize=tick_font)

        filtered_df['Small molecule'].value_counts().plot(kind='pie', ax=axes[1], autopct='%1.1f%%', colors=['#ff69b4', '#ffb6c1'])
        axes[1].set_title("Small Molecule vs Others", fontsize=title_font)
        axes[1].tick_params(axis='both', labelsize=tick_font)

        filtered_df['Target actions'].str.split(';').explode().str.strip().value_counts().head(10).plot(
            kind='bar', ax=axes[2], color='#d63384')
        axes[2].set_title("Top 10 Target Actions", fontsize=title_font)
        axes[2].set_ylabel("Count", fontsize=label_font)
        axes[2].set_xlabel("Target actions", fontsize=label_font)
        axes[2].tick_params(axis='both', labelsize=tick_font)
        axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=45, ha="right", fontsize=tick_font)

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=detail_window)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        # 🔥 Auto-save results
        save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")],
                                                 title="Save Search Results")
        if save_path:
            try:
                if save_path.endswith(".csv"):
                    filtered_df.to_csv(save_path, index=False)
                elif save_path.endswith(".xlsx"):
                    filtered_df.to_excel(save_path, index=False)
                messagebox.showinfo("Success", f"Results saved successfully at:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

# Run the main window
create_main_window()


