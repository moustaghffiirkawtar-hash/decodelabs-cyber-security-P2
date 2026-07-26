import tkinter as tk
from tkinter import ttk

def cypherchar(c):
    shift = 4
    return chr((ord(c.upper()) - 65 + shift) % 26 + 65)

def cyphertext(text):
    cytext = ""
    for c in text:
        if c.isalpha():
            encrypted = cypherchar(c)
            cytext += encrypted.lower() if c.isupper() else encrypted.upper()
        else:
            cytext += c
    return cytext

def decypherchar(c):
    shift = 4
    return chr((ord(c.upper()) - 65 - shift) % 26 + 65)

def decyphertext(text):
    decytext = ""
    for c in text:
        if c.isalpha():
            decrypted = decypherchar(c)
            decytext += decrypted.lower() if c.isupper() else decrypted.upper()
        else:
            decytext += c
    return decytext

def process():
    text = entry.get()
    if not text.strip():
        result_var.set("⚠️ Please enter some text.")
        result_label.config(fg="#e74c3c")
        return
    if mode.get() == "e":
        result = cyphertext(text)
        result_label.config(fg="#2ecc71")
    else:
        result = decyphertext(text)
        result_label.config(fg="#f39c12")
    result_var.set(result)

# --- Window setup ---
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("420x280")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# --- Title ---
tk.Label(root, text="Caesar Cipher", font=("Helvetica", 18, "bold"),
         bg="#1e1e2e", fg="#89b4fa").pack(pady=(20, 5))
tk.Label(root, text="shift 4 + case reversal", font=("Helvetica", 9),
         bg="#1e1e2e", fg="#6c7086").pack()

# --- Input ---
tk.Label(root, text="Enter text:", font=("Helvetica", 11),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=(20, 4))
entry = tk.Entry(root, font=("Helvetica", 12), width=32,
                 bg="#313244", fg="#cdd6f4", insertbackground="white",
                 relief="flat", bd=6)
entry.pack()

# --- Mode toggle ---
mode = tk.StringVar(value="e")
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=12)
tk.Radiobutton(frame, text="Encrypt", variable=mode, value="e",
               bg="#1e1e2e", fg="#2ecc71", selectcolor="#1e1e2e",
               activebackground="#1e1e2e", font=("Helvetica", 10)).pack(side="left", padx=10)
tk.Radiobutton(frame, text="Decrypt", variable=mode, value="d",
               bg="#1e1e2e", fg="#f39c12", selectcolor="#1e1e2e",
               activebackground="#1e1e2e", font=("Helvetica", 10)).pack(side="left", padx=10)

# --- Button ---
tk.Button(root, text="Go", font=("Helvetica", 11, "bold"),
          bg="#89b4fa", fg="#1e1e2e", activebackground="#74c7ec",
          relief="flat", padx=20, pady=4, command=process).pack()

# --- Result ---
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 13, "bold"),
                        bg="#1e1e2e", fg="#2ecc71", wraplength=380)
result_label.pack(pady=(16, 0))

root.mainloop()