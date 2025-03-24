import tkinter as tk
from sort_menu import sorting_menu

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def main_menu(window):
    clear_window(window)
    window.title("Algorithm Visualiser")

    sort_btn= tk.Button(window,text="Visualise Sorting Algorithms", command=lambda:sorting_menu(window))
    sort_btn.pack(pady=10)
    
    graph_btn = tk.Button(window,text="Visualise Graph Algorithms")
    graph_btn.pack(pady=10)
    
def main():
    window = tk.Tk()

    window.title("Algorithm Visualiser")

    main_menu(window)

    window.mainloop()
if __name__ == "__main__":
    main()