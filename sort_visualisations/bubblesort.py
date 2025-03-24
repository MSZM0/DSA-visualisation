import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button

class SortingVisualizer:
    def __init__(self):
        self.arr = [random.randint(1, 100) for _ in range(20)]
        self.sorted = False
        self.fig, self.ax = plt.subplots()
        self.bars = self.ax.bar(range(len(self.arr)), self.arr)
        self.i = 0  
        self.j = 0  
        self.ax_button = plt.axes([0.75, 0.01, 0.15, 0.075])
        self.button = Button(self.ax_button, 'Next Step')
        self.button.on_clicked(self.next_step)

    def update_bars(self):
        for i, bar in enumerate(self.bars):
            bar.set_height(self.arr[i])
        plt.draw()

    def bubble_sort_step(self):
        if not self.sorted:
            n = len(self.arr)
            if self.i < n - 1:
                if self.j < n - self.i - 1:
                    #Compare and change positions where necessary
                    if self.arr[self.j] > self.arr[self.j + 1]:
                        self.arr[self.j], self.arr[self.j + 1] = self.arr[self.j + 1], self.arr[self.j]
                    self.j += 1
                else:
                    self.j = 0
                    self.i += 1
            else:
                self.sorted = True

    def next_step(self, event):
        self.bubble_sort_step()
        self.update_bars()

    def visualize(self):
        plt.show()

def visualize_bubble_sort():
    visualizer = SortingVisualizer()
    visualizer.visualize()

if __name__ == "__main__":
    visualize_bubble_sort()
