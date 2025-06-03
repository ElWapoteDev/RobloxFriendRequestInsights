import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading
# Import functions from main.py
import main
from main import iterate_roblox_friend_pages

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roblox Friend Insights")
        self.geometry("400x300")
        self.resizable(False, False)

        self.configure(bg='white')

        ttk.Style().configure('TButton', padding=6)
        ttk.Style().configure('TLabel', background='white')

        tk.Label(self, text="Cookie de seguridad:", bg='white').pack(pady=10)
        self.cookie_entry = tk.Entry(self, width=50)
        self.cookie_entry.pack(pady=5)

        self.start_btn = ttk.Button(self, text="Iniciar", command=self.start)
        self.start_btn.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(self, height=10, state='disabled')
        self.log_area.pack(fill='both', padx=10, pady=10)

    def log(self, message: str):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.configure(state='disabled')
        self.log_area.see(tk.END)

    def start(self):
        cookie = self.cookie_entry.get().strip()
        if not cookie:
            self.log("Por favor ingresa la cookie.")
            return
        self.start_btn.config(state='disabled')
        thread = threading.Thread(target=self.run_script, args=(cookie,), daemon=True)
        thread.start()

    def run_script(self, cookie: str):
        def patched_get_page(*args, **kwargs):
            succ, data = original_get_page(*args, **kwargs)
            if succ:
                self.log(f"Recuperada pagina: {len(data.get('data', []))} entradas")
            else:
                self.log(f"Error: {data}")
            return succ, data

        original_get_page = main.get_page
        main.get_page = patched_get_page
        iterate_roblox_friend_pages(cookie)
        main.get_page = original_get_page
        self.log("Proceso completado")
        self.start_btn.config(state='normal')

if __name__ == '__main__':
    app = App()
    app.mainloop()
