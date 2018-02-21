from tkinter import filedialog
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from colordescriptor import ColorDescriptor
from searcher import Searcher
import cv2

fname = 0
result_array = []
cd = ColorDescriptor((8, 12, 3))
def make_label(master, x, y, w, h, img):

    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.place(x=x, y=y)
    label = Label(f, image=img)
    label.pack()

    return label

def path():

    filename = filedialog.asksaveasfilename(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    global fname
    fname = filename

    label = Label(root, text='Query Image', fg='#F1E710', bg='#34495E')
    label.config(font=("Courier", 20))
    label.pack()
    label.place(x=215, y=50)

    return filename

def imgChose():
    image = Image.open(path())
    image = image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 100, 100, 400, 400, img)
    root.mainloop()

def imgChose1(path):
    image = Image.open(path)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 750, 80, 190, 160, img)
    imgChose2(result_array[1])
    root.mainloop()

def imgChose2(path1):
    image = Image.open(path1)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 750, 250, 190, 160, img)
    imgChose3(result_array[2])
    root.mainloop()

def imgChose3(path3):
    image = Image.open(path3)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 750, 420, 190, 160, img)
    imgChose4(result_array[3])
    root.mainloop()

def imgChose4(path4):
    image = Image.open(path4)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 950, 80, 190, 160, img)
    imgChose5(result_array[4])
    root.mainloop()

def imgChose5(path5):
    image = Image.open(path5)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 950, 250, 190, 160, img)
    imgChose6(result_array[5])
    root.mainloop()

def imgChose6(path6):
    image = Image.open(path6)
    image = image.resize((190, 160), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    make_label(root, 950, 420, 190, 160, img)
    result_array[:] = []
    root.mainloop()


def search():
    query = cv2.imread(fname)
    features = cd.describe(query)
    searcher = Searcher("index.csv")
    results = searcher.search(features)

    label = Label(root, text='Result Images', fg='#F1E710', bg='#34495E')
    label.config(font=("Courier", 20))
    label.pack()
    label.place(x=850, y=30)

    for (score, resultID) in results:
        results = "D:\DOC\PycharmProject\dataset" + "/" + resultID
        result = cv2.imread(results)
        result_array.append(results)

    imgChose1(result_array[0])

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(1200, 700)
    root.configure(background="#34495E")

    root.title("Image Search Engine")

    buttonImg = Button(root, text='Search', command=search, width=10, height=1, bg='#2B70F1', fg='white')
    buttonImg.pack(side=BOTTOM, pady=30)
    buttonImg.config(font=("Courier", 13))

    buttonChos = Button(root, text='Choose Image', command=imgChose, width=13, height=1, bg='#2B70F1', fg='white')
    buttonChos.pack(side=BOTTOM, pady=0)
    buttonChos.config(font=("Courier", 13))

    root.mainloop()
