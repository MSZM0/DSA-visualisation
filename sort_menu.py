import tkinter as tk

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def sorting_menu(window):
    
    clear_window(window)

    label = tk.Label(window,text="Select sorting algorithm:")
    label.pack(pady=20)

    from sort_visualisations.bubblesort import visualize_bubble_sort
    bubble_btn = tk.Button(window,text="Bubble Sort",command=lambda:visualize_bubble_sort())
    bubble_btn.pack(pady=10)

    insertion_btn = tk.Button(window,text = "Insertion Sort",)
    insertion_btn.pack(pady=10)

    from start import main_menu

    back_btn = tk.Button(window,text="Back",command=lambda: main_menu(window))
    back_btn.pack(pady=10)