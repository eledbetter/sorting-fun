'''
UI for user to input settings for the list each algorithm will sort

TODO: get user input and pass it to graph.py
'''
import tkinter as tk
import random
import graph

# create randomized list of inputted length and pass it to graph module
def createRandomizedList(numElements):
    unsorted = []

    for a in range(0, numElements):
        unsorted.append(random.randrange(0, 100))
    print("Sorting list with", numElements, "random elements")
    graph.compareSort(unsorted)

# create main input GUI
def createGUI():
    mainWindow = tk.Tk()
    mainWindow.title("title")
    mainWindow.geometry('300x200')

    tk.Label(mainWindow, text="List size").grid(row=0)
    sizeInput = tk.Entry(mainWindow)
    sizeInput.grid(row=0, column=1)
    
    # TODO: get user input
    submitButton = tk.Button(mainWindow, text="Sort!", command=lambda: createRandomizedList(5)).grid(row=1)

    mainWindow.mainloop()

if __name__ == "__main__":
    createGUI()