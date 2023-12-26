import requests as req
import tkinter as tk
from tkinter import messagebox, filedialog

def save_to_file(html, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html)
    messagebox.showinfo("Success", f"Data successfully saved in file:\n{filename}")

def fetch_and_save():
    url = entry.get()

    try:
        response = req.get(url)
        response.raise_for_status()
        html = response.text

        file_types = [("HTML files", "*.html"), ("Text files", "*.txt"), ("All files", "*.*")]
        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=file_types)

        if file_path:
            save_to_file(html, file_path)

    except req.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while parsing the page: {e}")

root = tk.Tk()
root.title("Parsing page")

label = tk.Label(root, text="Enter page URL:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Parse&Save", command=fetch_and_save)
button.pack(pady=10)

root.mainloop()
