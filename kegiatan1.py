# import modul tkinter untuk GUI
import tkinter as tk
# membuat window utama aplikasi, memberi warna dan judul
my_app = tk.Tk()
my_app.configure(bg="#abd4fd")
my_app.title("Data Diri")

# Label judul "Data Diri" di baris 0
judul = tk.Label(my_app, text="Data Diri", font=("Arial", 20))
judul.grid(row=0, column=0, columnspan=2, pady=10)
# === Data diri: label kiri dan kanan ===
# Label kiri: Nama, NIM, Buku, Idola, Motto
# Label kanan: isi dari data
tk.Label(my_app, text="Nama").grid(row=1, column=0, sticky="w", padx=10)
tk.Label(my_app, text="Rianda Rahma Dewanty").grid(row=1, column=1, sticky="w")
tk.Label(my_app, text="NIM").grid(row=2, column=0, sticky="w", padx=10)
tk.Label(my_app, text="L200250096").grid(row=2, column=1, sticky="w")
tk.Label(my_app, text="Lagu favorit").grid(row=3, column=0, sticky="w", padx=10)
tk.Label(my_app, text="Something About You").grid(row=3, column=1, sticky="w")
tk.Label(my_app, text="Idola kalangan sahabat").grid(row=4, column=0, sticky="w", padx=10)
tk.Label(my_app, text="Umar bin Khattab").grid(row=4, column=1, sticky="w")
tk.Label(my_app, text="Motto").grid(row=5, column=0, sticky="w", padx=10)
tk.Label(my_app, text="Compile the knowledge").grid(row=5, column=1, sticky="w")

# fungsi untuk menutup aplikasi
def close():
    my_app.quit()
# tombol "close"
button = tk.Button(my_app, text="Close", command=close, bg="white")
button.grid(row=6, column=0, columnspan=2, pady=15)

# memunculkan window
my_app.mainloop()