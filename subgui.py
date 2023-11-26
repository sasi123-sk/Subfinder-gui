#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess

class SubdomainFinderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Subdomain Finder GUI")

        # Set the size of the GUI interface
        master.geometry("600x400")

        # Create a notebook (tabbed widget)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        # Add "Scan" tab
        scan_tab = ttk.Frame(self.notebook)
        self.notebook.add(scan_tab, text="Scan")

        self.scan_input_label = tk.Label(scan_tab, text="Enter domain:")
        self.scan_input_label.pack()

        self.scan_input_entry = tk.Entry(scan_tab)
        self.scan_input_entry.pack()

        self.find_button = tk.Button(scan_tab, text="Find Subdomains", command=self.find_subdomains)
        self.find_button.pack(side="top", padx=(10, 0))

        # Add "Output" tab
        output_tab = ttk.Frame(self.notebook)
        self.notebook.add(output_tab, text="Output")

        self.output_text = scrolledtext.ScrolledText(output_tab, height=10, width=70)
        self.output_text.pack()

        # Add "About" tab
        about_tab = ttk.Frame(self.notebook)
        self.notebook.add(about_tab, text="About")

        about_text = """Subdomain Finder Tool\n\n
        Created by: Sasikaran\n
        Insta : https://www.instagram.com/0xwhitedevil\n
        Github : https://github.com/sasi123-sk\n
        LinkedIn : https://www.linkedin.com/in/sasi-karan-1bb48a226/"""
        self.about_label = tk.Label(about_tab, text=about_text)
        self.about_label.pack()

        # Button to save output to a file
        self.save_button = tk.Button(output_tab, text="Save Output", command=self.save_output)
        self.save_button.pack()

    def find_subdomains(self):
        domain = self.scan_input_entry.get()
        if domain:
            try:
                # Run subfinder command and display the result
                result = subprocess.run(["subfinder", "-d", domain], text=True, capture_output=True)

                # Display the output in the "Output" tab
                self.output_text.delete(1.0, tk.END)  # Clear previous content
                if result.returncode == 0:
                    self.output_text.insert(tk.END, result.stdout)
                else:
                    self.output_text.insert(tk.END, f"Error: {result.stderr}")
            except Exception as e:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Error: {e}")

    def save_output(self):
        # Save the output to a file inside a folder named after the input domain
        domain = self.scan_input_entry.get()
        folder_name = f"subdomain_output_{domain}"
        os.makedirs(folder_name, exist_ok=True)
        filename = os.path.join(folder_name, "output.txt")
        with open(filename, "w") as file:
            file.write(self.output_text.get(1.0, tk.END))
        self.output_text.insert(tk.END, f"\nOutput saved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubdomainFinderGUI(root)
    root.mainloop()
