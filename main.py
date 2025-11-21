nev = "Szabó Dániel József"
hallgatoi_kod = "K4RBFO"
monogram = "SzD"

print("Név:", nev)
print("Hallgatói kód:", hallgatoi_kod)
print("Monogram:", monogram)

from tkinter import Tk
import app

def main():
    root = Tk()
    root.title("app")
    app.run(root)
    root.mainloop()

if __name__ == "__main__":
    main()