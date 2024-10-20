import tkinter as tk
from tkinter import messagebox


class Fridge:
    def __init__(self, numMainShelves, numFreezerShelves):
        self.isOn = False
        self.mainShelves = [[] for _ in range(numMainShelves)]
        self.freezerShelves = [[] for _ in range(numFreezerShelves)]

    def powerOn(self):
        self.isOn = True
        return "Fridge is now ON."

    def powerOff(self):
        self.isOn = False
        return "Fridge is now OFF."

    def addItemToShelf(self, shelfNum, item):
        if not self.isOn:
            raise ValueError("The fridge is off!")
        if 0 <= shelfNum < len(self.mainShelves):
            self.mainShelves[shelfNum].append(item)
            return f'{item} added to shelf {shelfNum + 1}.'
        else:
            raise ValueError("Invalid shelf number.")

    def addItemToFreezer(self, sectionNum, item):
        if not self.isOn:
            raise ValueError("The fridge is off!")
        if 0 <= sectionNum < len(self.freezerShelves):
            self.freezerShelves[sectionNum].append(item)
            return f'{item} added to freezer section {sectionNum + 1}.'
        else:
            raise ValueError("Invalid freezer section.")

    def removeItemFromShelf(self, shelfNum, item):
        if not self.isOn:
            raise ValueError("The fridge is off!")
        if 0 <= shelfNum < len(self.mainShelves):
            if item in self.mainShelves[shelfNum]:
                self.mainShelves[shelfNum].remove(item)
                return f'{item} removed from shelf {shelfNum + 1}.'
            else:
                raise ValueError(f'{item} not found on shelf {shelfNum + 1}.')
        else:
            raise ValueError("Invalid shelf number.")

    def removeItemFromFreezer(self, sectionNum, item):
        if not self.isOn:
            raise ValueError("The fridge is off!")
        if 0 <= sectionNum < len(self.freezerShelves):
            if item in self.freezerShelves[sectionNum]:
                self.freezerShelves[sectionNum].remove(item)
                return f'{item} removed from freezer section {sectionNum + 1}.'
            else:
                raise ValueError(f'{item} not found in freezer section {sectionNum + 1}.')
        else:
            raise ValueError("Invalid freezer section.")

    def getContents(self):
        if not self.isOn:
            return "Fridge is off. Please turn it on to view contents."
        contents = "Fridge Contents:\n"
        for i, shelf in enumerate(self.mainShelves):
            contents += f'Shelf {i + 1}: {shelf}\n'
        for i, section in enumerate(self.freezerShelves):
            contents += f'Freezer Section {i + 1}: {section}\n'
        return contents


class FridgeApp:
    def __init__(self, root, fridge):
        self.fridge = fridge
        self.root = root
        self.root.title("Fridge App")
        self.root.geometry("400x700")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(0, 0)

        self.titleLabel = tk.Label(root, text="Fridge Manager", bg="#f7f7f7", font=("Arial", 18, "bold"))
        self.titleLabel.pack(pady=10)

        self.powerButton = tk.Button(root, text="Power On", command=self.togglePower, bg="#28a745", fg="white", font=("Arial", 12, "bold"))
        self.powerButton.pack(pady=10)

        self.mainFrame = tk.LabelFrame(root, text="Main Compartment", font=("Arial", 12), bg="#f7f7f7")
        self.mainFrame.pack(pady=10, padx=10, fill="both", expand=True)

        self.itemLabel = tk.Label(self.mainFrame, text="Item:", font=("Arial", 10), bg="#f7f7f7")
        self.itemLabel.pack(pady=5)
        self.itemEntry = tk.Entry(self.mainFrame, width=30)
        self.itemEntry.pack(pady=5)

        self.shelfLabel = tk.Label(self.mainFrame, text="Shelf Number (0 to 2):", font=("Arial", 10), bg="#f7f7f7")
        self.shelfLabel.pack(pady=5)
        self.shelfEntry = tk.Entry(self.mainFrame, width=30)
        self.shelfEntry.pack(pady=5)

        self.addButton = tk.Button(self.mainFrame, text="Add to Shelf", command=self.addToShelf, bg="#17a2b8", fg="white", font=("Arial", 10, "bold"))
        self.addButton.pack(pady=10)

        self.removeButton = tk.Button(self.mainFrame, text="Remove from Shelf", command=self.removeFromShelf, bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
        self.removeButton.pack(pady=10)

        self.freezerFrame = tk.LabelFrame(root, text="Freezer", font=("Arial", 12), bg="#f7f7f7")
        self.freezerFrame.pack(pady=10, padx=10, fill="both", expand=True)

        self.freezerLabel = tk.Label(self.freezerFrame, text="Item:", font=("Arial", 10), bg="#f7f7f7")
        self.freezerLabel.pack(pady=5)
        self.freezerEntry = tk.Entry(self.freezerFrame, width=30)
        self.freezerEntry.pack(pady=5)

        self.freezerSectionLabel = tk.Label(self.freezerFrame, text="Freezer Section Number (0 to 1):", font=("Arial", 10), bg="#f7f7f7")
        self.freezerSectionLabel.pack(pady=5)
        self.freezerSectionEntry = tk.Entry(self.freezerFrame, width=30)
        self.freezerSectionEntry.pack(pady=5)

        self.addFreezerButton = tk.Button(self.freezerFrame, text="Add to Freezer", command=self.addToFreezer, bg="#17a2b8", fg="white", font=("Arial", 10, "bold"))
        self.addFreezerButton.pack(pady=10)

        self.removeFreezerButton = tk.Button(self.freezerFrame, text="Remove from Freezer", command=self.removeFromFreezer, bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
        self.removeFreezerButton.pack(pady=10)

        self.showButton = tk.Button(root, text="Show Fridge Contents", command=self.showContents, bg="#007bff", fg="white", font=("Arial", 12, "bold"))
        self.showButton.pack(pady=20)

        self.outputText = tk.Text(root, height=10, width=50, bg="#ffffff", font=("Arial", 10), state=tk.DISABLED)
        self.outputText.pack(pady=5)

        self.addButton.config(state=tk.DISABLED)
        self.removeButton.config(state=tk.DISABLED)
        self.addFreezerButton.config(state=tk.DISABLED)
        self.removeFreezerButton.config(state=tk.DISABLED)

    def togglePower(self):
        if self.fridge.isOn:
            result = self.fridge.powerOff()
            self.powerButton.config(text="Power On", bg="#28a745")
            self.addButton.config(state=tk.DISABLED)
            self.removeButton.config(state=tk.DISABLED)
            self.addFreezerButton.config(state=tk.DISABLED)
            self.removeFreezerButton.config(state=tk.DISABLED)
        else:
            result = self.fridge.powerOn()
            self.powerButton.config(text="Power Off", bg="#dc3545")
            self.addButton.config(state=tk.NORMAL)
            self.removeButton.config(state=tk.NORMAL)
            self.addFreezerButton.config(state=tk.NORMAL)
            self.removeFreezerButton.config(state=tk.NORMAL)
        messagebox.showinfo("Fridge", result)

    def addToShelf(self):
        item = self.itemEntry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Item field cannot be empty!")
            return
        try:
            shelfNum = int(self.shelfEntry.get())
            result = self.fridge.addItemToShelf(shelfNum, item)
            messagebox.showinfo("Fridge", result)
            self.clearInputs()
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def removeFromShelf(self):
        item = self.itemEntry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Item field cannot be empty!")
            return
        try:
            shelfNum = int(self.shelfEntry.get())
            result = self.fridge.removeItemFromShelf(shelfNum, item)
            messagebox.showinfo("Fridge", result)
            self.clearInputs()
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def addToFreezer(self):
        item = self.freezerEntry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Item field cannot be empty!")
            return
        try:
            sectionNum = int(self.freezerSectionEntry.get())
            result = self.fridge.addItemToFreezer(sectionNum, item)
            messagebox.showinfo("Fridge", result)
            self.clearInputs()
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def removeFromFreezer(self):
        item = self.freezerEntry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Item field cannot be empty!")
            return
        try:
            sectionNum = int(self.freezerSectionEntry.get())
            result = self.fridge.removeItemFromFreezer(sectionNum, item)
            messagebox.showinfo("Fridge", result)
            self.clearInputs()
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def showContents(self):
        result = self.fridge.getContents()
        self.outputText.config(state=tk.NORMAL)
        self.outputText.delete(1.0, tk.END)
        self.outputText.insert(tk.END, result)
        self.outputText.config(state=tk.DISABLED)

    def clearInputs(self):
        self.itemEntry.delete(0, tk.END)
        self.shelfEntry.delete(0, tk.END)
        self.freezerEntry.delete(0, tk.END)
        self.freezerSectionEntry.delete(0, tk.END)



fridge = Fridge(3, 2)
root = tk.Tk()
app = FridgeApp(root, fridge)
root.mainloop()
