import numpy as np
from scipy.ndimage.interpolation import shift as s
import tkinter as tk
from tkinter import *
import numpy as np

window = Tk()
window.geometry('450x100')
window.title('Зачёт по прикладному программированию')

array = np.array([1, 2, 3, 4, 5])
num = -3


def start():
    string = arrayInput.get()
    array = string.split(', ')
    array = np.array(array)
    num = int(shiftInput.get())
    shift(array, num, 0)


def shift(arr, num, fill_value):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    output = []
    for i in result:
        output.append(int(i))
    resultValue.set(str(output))


ArrayLabel = Label(text='Введите массив')
ArrayLabel.grid(row=1, column=1)

arrayString = StringVar()
arrayInput = Entry(textvariable=arrayString)
arrayInput.grid(row=1, column=2)

shiftLabel = Label(text='Сдвиг влево на')
shiftLabel.grid(row=2, column=1)

shiftString = IntVar()
shiftInput = Entry(textvariable=shiftString)
shiftInput.grid(row=2, column=2)

spaceLabel = Label(
    text=''
)
spaceLabel.grid(row=2, column=3)

startBtn = Button(
    text='Сдвинуть',
    command=start
)
startBtn.grid(row=2, column=4)

resultValue = StringVar()
resultLabel = Label(
    textvariable=resultValue
)
resultLabel.grid(row=4, column=1)

window.mainloop()
