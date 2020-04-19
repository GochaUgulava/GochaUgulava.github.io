from tkinter import *
from tkinter.ttk import Combobox, Separator


def get_easter_date(year):
    """Calculate orthodox easter date for XX-XXI centuries """
    f = (19 * (year % 19) + 15) % 30 + (2 * (year % 4) + 4 * (year % 7) + 6 * ((19 * (year % 19) + 15) % 30) + 6) % 7
    if f <= 9:
        day_old = 22 + f
        month_old = 'March'
    else:
        day_old = f - 9
        month_old = 'April'
    day_new = day_old + 13
    month_new = "March"
    if month_old == 'March':
        if day_new > 31:
            month_new = "April"
            day_new -= 31
    if month_old == "April":
        if day_new > 30:
            month_new = "May"
            day_new -= 30
        else:
            month_new = "April"
    easter_date = [day_old, month_old, day_new, month_new]
    return easter_date


def calculate():
    """Handler for button """
    year = int(combo.get())
    easter_date = get_easter_date(year)
    msg = ('The Orthodox Easter for ' + str(year) + ': \n' + easter_date[1] + ' ' +
           str(easter_date[0]) + ' -   O.S. (Julian calendar) \n' + easter_date[3] + ' ' + str(easter_date[2]) +
           ' -   N.S. (Gregorian calendar)')
    if len(root.winfo_children()) > 5:
        root.winfo_children()[-1].destroy()
    ans = Label(root, text=msg, font='Calibri 14')
    ans.grid(column=0, row=4, columnspan=2, pady=10, padx=10)


if __name__ == "__main__":
    root = Tk()
    root.geometry('400x300')
    root.title('Orthodox Easter date calculation')

    txt = Label(root, text='This program calculates \n Orthodox Easter date for XX-XXI centuries', font=('Arial', 14))
    txt.grid(column=0, row=0, columnspan=2, pady=10, padx=10)

    txt = Label(root, text='Choose year: ', font=('Calibri', 14))
    txt.grid(column=0, row=1, pady=10, padx=10, sticky=E)

    combo = Combobox(root)
    combo['values'] = list(range(1900, 2100))
    combo.current(120)
    combo.grid(column=1, row=1, padx=10, sticky=W)

    button_calculate = Button(root, text='Calculate', font='Calibri 12',  command=calculate)
    button_calculate.grid(column=0, row=2, columnspan=2, pady=10, padx=10)

    sep = Separator(root, orient=HORIZONTAL)
    sep.grid(column=0, row=3, columnspan=2, pady=5, sticky=W+E)

    root.mainloop()
