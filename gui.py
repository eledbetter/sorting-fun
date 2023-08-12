'''
UI for user to input settings for the list each algorithm will sort

TODO: multiple plot management & cleanup
'''
import tkinter as tk
import random
import graph

class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("title")
        self.geometry('300x200')

        self.intInput = tk.IntVar(value=5)

        self.createGUI()

    # create main input GUI
    def createGUI(self):

        self.entryLabel = tk.Label(self, text="List Size")
        self.entry = tk.Entry(self, textvariable=self.intInput)
        self.submitButton = tk.Button(self, text="Sort!", command=lambda: self.createRandomizedList())

        self.entryLabel.grid(row=0, column=0, padx=5, pady=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.submitButton.grid(row=1, column=1, padx=5, pady=5)

    # create randomized list of inputted length and pass it to graph module
    def createRandomizedList(self):
        listSize = self.intInput.get()
        unsorted = []

        for a in range(0, listSize):
            unsorted.append(random.randrange(0, 100))
        print("Sorting list with", listSize, "random elements")
        graph.compareSort(unsorted)

if __name__ == "__main__":
    app = gui()
    app.mainloop()