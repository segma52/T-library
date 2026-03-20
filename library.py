import time
import tkinter as tk
from tkinter import messagebox
import os
if not os.path.exists("books.txt"):
    open("books.txt", "w", encoding = "utf-8").close()
if not os.path.exists("counter.txt"):
    open("counter.txt", "w", encoding = "utf-8").close()
    with open("counter.txt", "w") as file:
        file.write("0")
with open("counter.txt", "r", encoding = "utf-8") as file:
        count = int(file.read())


w = 400
h = 800
top_col = "#131D21"
bg_col = "#2c3e50"
inp_col = "#566573"
text_col = "#FFEB00"
wiget_col = "#0C151A"
name_col = "#FFEB00"
author_col = "#FFF153"
yng_col = "#CCC029"


root = tk.Tk()
root.title("T-Библиотека")
root.geometry(str(w) + "x" + str(h))
root.config(bg = bg_col)


top_canvas = tk.Canvas(root, width = w, height = 100, bg = bg_col, highlightthickness = 0)
top_canvas.pack(side = tk.TOP)
top_canvas.create_rectangle(0, 0, w, 100, fill = top_col, outline = top_col)
top_canvas.create_oval(10, 25, 60, 75, fill = inp_col, outline = inp_col)
top_canvas.create_oval(10 + 230, 25, 60 + 230, 75, fill = inp_col, outline = inp_col)
top_canvas.create_rectangle(35, 25, 35 + 230, 75, fill = inp_col, outline = inp_col)
lupa = tk.Label(root, text = "🔍", font = ("Arial", 20), bg = top_col, fg = text_col)
lupa.place(x = 300, y = 30)


entry_search = tk.Entry(root, width = 14, font = ("Arial", 20), bg = inp_col, bd = 0, fg = text_col)
entry_search.place(x = 25, y = 33)

bot_canvas = tk.Canvas(root, width = w, height = h-700, bg = top_col, highlightthickness = 0)
bot_canvas.pack(side = tk.BOTTOM)


canvas = tk.Canvas(root, width = w, height = h-200, bg = bg_col, highlightthickness = 1)
canvas.pack()
canvas.configure(scrollregion = (0, 0, w, 9999))


def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
canvas.bind_all("<MouseWheel>", on_mousewheel)



#functions
def cnsort():
    nosort.place_forget()
    sort1.place_forget()
    sort2.place_forget()
    sort3.place_forget()
    csort.place_forget()
    sort_menu.destroy()
    



def cancel_add():
    title_l.place_forget()
    author_l.place_forget()
    genre_l.place_forget()
    year_l.place_forget()
    desc_l.place_forget()
    entry_title.place_forget()
    entry_author.place_forget()
    entry_genre.place_forget()
    entry_year.place_forget()
    entry_desc.place_forget()
    save_btn.place_forget()
    cancel_btn.place_forget()
    add_menu.destroy()
    show_books()








def opsomu():
    global sort1, sort2, sort3, csort, nosort
    global sort_menu
    try:
        filter_menu.destroy()
    except:
        pass
    try:
        sort_menu.destroy()
    except:
        pass
    
    sort_menu = tk.Frame(root, bg = top_col, bd = 1, relief = tk.RAISED)
    sort_menu.place(x = 0, y = 560, width = 150, height = 140)
    sort_menu.lift()
    
    nosort = tk.Button(sort_menu, text = "без сортировки", bg = inp_col, fg = text_col, command = show_books)
    nosort.place(x = 10, y = 10)
    sort1 = tk.Button(sort_menu, text = "По названию", bg = inp_col, fg = text_col, command = lambda: sort_books("title"))
    sort1.place(x = 10, y = 45)
    sort2 = tk.Button(sort_menu, text = "По автору", bg = inp_col, fg = text_col, command = lambda: sort_books("author"))
    sort2.place(x = 10, y = 80)
    sort3 = tk.Button(sort_menu, text = "По году", bg = inp_col, fg = text_col, command = lambda: sort_books("year"))
    sort3.place(x = 10, y = 115)
    csort = tk.Button(sort_menu, text = "❌", font = ("Arial", 10), fg = top_col, bg = inp_col, bd = 0, command = cnsort)
    csort.place(x = 110, y = 10)

def cnsort():
    global sort_menu
    try:
        sort_menu.destroy()
    except:
        pass
    



def write_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    year = entry_year.get()
    desc = entry_desc.get()
    
    if title == "":
        messagebox.showwarning("Ошибка","Название обязательно")
        return
    if author =="":
        messagebox.showwarning("Ошибка","Имя автора обязательно")
        return
    if genre == "":
        genre= "-"
    if year == "":
        year= "-"
    if desc == "":
        desc = "-"
        
    with open("counter.txt","r",encoding="utf-8")as file:
        data = file.read().strip()
        count = int(data)if data else 0

    with open("books.txt","a",encoding="utf-8")as file:
        file.write(str(count+1)+"|"+title+"|"+author+"|"+genre+"|"+year+"|"+desc+"|0\n")

    count = count + 1
    with open("counter.txt","w",encoding="utf-8")as file:
        file.write(str(count))
    cancel_add()





        
def add_book():
    global add_menu
    global entry_title, entry_author, entry_genre, entry_year, entry_desc
    global title_l, author_l, genre_l, year_l, desc_l
    global save_btn, cancel_btn
    add_menu = tk.Frame(root, bg = top_col, bd = 2, relief = tk.RAISED)
    add_menu.place(x = 200, y = 100, width = w - 200, height = 250)

    title_l = tk.Label(root, text = "Название:", bg = top_col, fg = text_col)
    title_l.place(x = 220, y = 120)

    entry_title = tk.Entry(root, width = 15, bg = inp_col, bd = 0, fg = text_col)
    entry_title.place(x = 300, y = 120)

    author_l = tk.Label(root, text = "Автор:", bg = top_col, fg = text_col)
    author_l.place(x = 220, y = 160)

    entry_author = tk.Entry(root, width = 15, bg = inp_col, bd = 0, fg = text_col)
    entry_author.place(x = 300, y = 160)

    genre_l = tk.Label(root, text = "Жанр:", bg = top_col, fg = text_col)
    genre_l.place(x = 220, y = 200)

    entry_genre = tk.Entry(root, width = 15, bg = inp_col, bd = 0, fg = text_col)
    entry_genre.place(x = 300, y = 200)

    year_l = tk.Label(root, text = "Год:", bg = top_col, fg = text_col)
    year_l.place(x = 220, y = 240)

    entry_year = tk.Entry(root, width = 15, bg = inp_col, bd = 0, fg = text_col)
    entry_year.place(x = 300, y = 240)

    desc_l = tk.Label(root, text = "Описание:", bg = top_col, fg = text_col)
    desc_l.place(x = 220, y = 280)

    entry_desc = tk.Entry(root, width = 15, bg = inp_col, bd = 0, fg = text_col)
    entry_desc.place(x = 300, y = 280)

    save_btn = tk.Button(root, text = "Сохранить", command = write_book, bg = top_col, fg = text_col, bd = 0)
    save_btn.place(x = 220, y = 320)
    cancel_btn = tk.Button(root, text = "Отмена", command = cancel_add, bg = top_col, fg = text_col, bd = 0)
    cancel_btn.place(x = 320, y = 320)




def delete_book(num):
    with open("books.txt", "r", encoding = "utf-8") as file:
        books = file.readlines()
    remaining = []
    for book in books:
        parts = book.strip().split("|")
        if len(parts) >= 1 and parts[0] != str(num):
            remaining.append(book)
    with open("books.txt", "w", encoding = "utf-8") as file:
        for i, book in enumerate(remaining, 1):
            parts = book.strip().split("|")
            parts[0] = str(i)
            file.write("|".join(parts) + "\n")
    with open("counter.txt", "w", encoding = "utf-8") as file:
        file.write(str(len(remaining)))
    show_books()




def filts():
    global filter_menu
    try:
        sort_menu.destroy()
    except:
        pass
    canvas.delete("sort")
    filter_menu = tk.Frame(root, bg = top_col, bd = 2, relief = tk.RAISED)
    filter_menu.place(x = 0, y = 550, width = w, height = 150)
    filter_menu.lift()
    genres = ["без фильтров", "фантастика", "детектив", "поэзия", "драма", "комедия", "ужасы", "приключения", "проза", "басня", "роман", "другое"]
    x = 10
    y = 10
    for genre in genres:
        btn = tk.Button(filter_menu, text = genre, bg = inp_col, fg = text_col, command = lambda g = genre: search(g))
        btn.place(x = x, y = y, width = 80, height = 30)
        x += 90
        if x > w - 100:
            x = 10
            y += 40
    close_btn = tk.Button(filter_menu, text = "❌", bg = inp_col, fg = text_col, command = lambda: filter_menu.destroy())
    close_btn.place(x = w - 35, y = 10)






def sort_books(tipe):
    with open("books.txt", "r", encoding = "utf-8") as file:
        books = file.readlines()
    
    books_list = []
    for book in books:
        parts = book.strip().split("|")
        if len(parts) >= 6:
            num = int(parts[0])
            title = parts[1]
            author = parts[2]
            genre = parts[3]
            year = int(parts[4]) if parts[4].isdigit() else 0
            desc = parts[5]
            books_list.append([num, title, author, genre, year, desc])
    
    if tipe == "title":
        for i in range(len(books_list)):
            for j in range(i + 1, len(books_list)):
                if books_list[i][1].lower() > books_list[j][1].lower():
                    books_list[i], books_list[j] = books_list[j], books_list[i]
    elif tipe == "author":
        for i in range(len(books_list)):
            for j in range(i + 1, len(books_list)):
                if books_list[i][2].lower() > books_list[j][2].lower():
                    books_list[i], books_list[j] = books_list[j], books_list[i]
    elif tipe == "year":
        for i in range(len(books_list)):
            for j in range(i + 1, len(books_list)):
                if books_list[i][4] > books_list[j][4]:
                    books_list[i], books_list[j] = books_list[j], books_list[i]
    
    canvas.delete("book")
    y = 20
    for book in books_list:
        num = book[0]
        title = book[1]
        author = book[2]
        genre = book[3]
        year = book[4]
        desc = book[5]
        
        canvas.create_oval(15, y, 15 + 20, y + 20, fill = wiget_col, outline = "", tags = "book")
        canvas.create_oval(w - 15, y, w - 15 - 20, y + 20, fill = wiget_col, outline = "", tags = "book")
        canvas.create_oval(15, y + 90, 15 + 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book")
        canvas.create_oval(w - 15, y + 90, w - 15 - 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book")
        canvas.create_rectangle(15, y + 10, w - 14, y + 90 + 10, fill = wiget_col, outline = "", width = 1, tags = "book")
        canvas.create_rectangle(15 + 10, y, w - 14 - 10, y + 90 + 21, fill = wiget_col, outline = "", width = 1, tags = "book")

        canvas.create_text(25, y+15, text = title, fill = name_col, font = ("Arial", 14, "bold"), anchor = "w", tags = "book")
        canvas.create_text(25, y+45, text = "✎ " + author, fill = author_col, font = ("Arial", 12), anchor = "w", tags = "book")
        canvas.create_text(25, y+70, text = "📅 " + str(year) + "  •  " + genre, fill = yng_col, font = ("Arial", 10), anchor = "w", tags = "book")
        del_btn = tk.Button(canvas, text = "🗑", font = ("Arial", 15), bg = wiget_col, fg = text_col, bd = 0, command = lambda n = num: delete_book(n))
        canvas.create_window(w - 50, y + 45, window = del_btn, tags = "book")
        y += 120
    canvas.configure(scrollregion = (0, 0, w, y + 50))








def search(search_text):
    if search_text == "без фильтров":
        show_books()
    else:
        canvas.delete("book")
        
        if not os.path.exists("books.txt"):
            return
        
        with open("books.txt", "r", encoding = "utf-8") as file:
            books = file.readlines()
        
        y = 20
        if search_text == "другое":
            kgn = ["фантастика", "детектив", "поэзия", "драма", "комедия", "ужасы", "приключения", "проза", "басня", "роман"]
            for i in range(len(books)):
                parts = books[i].strip().split("|")
                if len(parts) >= 6:
                    genre = parts[3].lower()
                    if genre not in kgn and genre != "-":
                        num, title, author, genre, year, desc = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
                        
                        canvas.create_oval(15, y, 15 + 20, y + 20, fill = wiget_col, outline = "", tags = "book")
                        canvas.create_oval(w - 15, y, w - 15 - 20, y + 20, fill = wiget_col, outline = "", tags = "book" )
                        canvas.create_oval(15, y + 90, 15 + 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book" )
                        canvas.create_oval(w - 15, y + 90, w - 15 - 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book" )
                        
                        canvas.create_rectangle(15, y + 10, w - 14, y + 90 + 10, fill = wiget_col, outline = "", width = 1, tags = "book")
                        canvas.create_rectangle(15 + 10, y, w - 14 - 10, y + 90 + 21, fill = wiget_col, outline = "", width = 1, tags = "book")
                        
                        canvas.create_text(25, y+15, text = f"" + title, fill = name_col, font = ("Arial", 14, "bold"), anchor = "w", tags = "book")
                        canvas.create_text(25, y+45, text = f"✎ " + author, fill = author_col, font = ("Arial", 12), anchor = "w", tags = "book")
                        canvas.create_text(25, y+70, text = f"📅 " + year + "  •  " + genre, fill = yng_col, font = ("Arial", 10), anchor = "w", tags = "book")
                        del_btn = tk.Button(canvas, text = "🗑", font = ("Arial", 15), bg = wiget_col, fg = text_col, bd = 0, command = lambda n = num: delete_book(n))
                        canvas.create_window(w - 50, y + 45, window = del_btn, tags = "book")
                        y += 120
            canvas.configure(scrollregion = (0, 0, w, y + 50))
        else:
            for i in range(len(books)):
                if search_text == "" or books[i].lower().find(search_text) != -1:
                    parts = books[i].strip().split("|")
                    if len(parts) >= 6:
                        num, title, author, genre, year, desc = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
                        
                        canvas.create_oval(15, y, 15 + 20, y + 20, fill = wiget_col, outline = "", tags = "book")
                        canvas.create_oval(w - 15, y, w - 15 - 20, y + 20, fill = wiget_col, outline = "", tags = "book" )
                        canvas.create_oval(15, y + 90, 15 + 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book" )
                        canvas.create_oval(w - 15, y + 90, w - 15 - 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book" )
                        
                        canvas.create_rectangle(15, y + 10, w - 14, y + 90 + 10, fill = wiget_col, outline = "", width = 1, tags = "book")
                        canvas.create_rectangle(15 + 10, y, w - 14 - 10, y + 90 + 21, fill = wiget_col, outline = "", width = 1, tags = "book")
                        
                        canvas.create_text(25, y+15, text = f"" + title, fill = name_col, font = ("Arial", 14, "bold"), anchor = "w", tags = "book")
                        canvas.create_text(25, y+45, text = f"✎ " + author, fill = author_col, font = ("Arial", 12), anchor = "w", tags = "book")
                        canvas.create_text(25, y+70, text = f"📅 " + year + "  •  " + genre, fill = yng_col, font = ("Arial", 10), anchor = "w", tags = "book")
                        del_btn = tk.Button(canvas, text = "🗑", font = ("Arial", 15), bg = wiget_col, fg = text_col, bd = 0, command = lambda n = num: delete_book(n))
                        canvas.create_window(w - 50, y + 45, window = del_btn, tags = "book")
                        y += 120
            canvas.configure(scrollregion = (0, 0, w, y + 50))







def show_books():
    canvas.delete("book")
    if not os.path.exists("books.txt"):
        return
    with open("books.txt", "r", encoding = "utf-8") as file:
        books = file.readlines()
    y = 20
    for book in books:
        parts = book.strip().split("|")
        if len(parts) >= 6:

            num, title, author, genre, year, desc = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
            canvas.create_oval(15, y, 15 + 20, y + 20, fill = wiget_col, outline = "", tags = "book")
            canvas.create_oval(w - 15, y, w - 15 - 20, y + 20, fill = wiget_col, outline = "", tags = "book")
            canvas.create_oval(15, y + 90, 15 + 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book")
            canvas.create_oval(w - 15, y + 90, w - 15 - 20, y + 90 + 20, fill = wiget_col, outline = "", tags = "book")
            
            canvas.create_rectangle(15, y + 10, w - 14, y + 90 + 10, fill = wiget_col, outline = "", width = 1, tags = "book")
            
            canvas.create_rectangle(15 + 10, y, w - 14 - 10, y + 90 + 21, fill = wiget_col, outline = "", width = 1, tags = "book")
            
            canvas.create_text(25, y+15, text = f"" + title, fill = name_col, font = ("Arial", 14, "bold"), anchor = "w", tags = "book")
            canvas.create_text(25, y+45, text = f"✎ " + author, fill = author_col, font = ("Arial", 12), anchor = "w", tags = "book")
            canvas.create_text(25, y+70, text = f"📅 " + year + "  •  " + genre, fill = yng_col, font = ("Arial", 10), anchor = "w", tags = "book")
            del_btn = tk.Button(canvas, text = "🗑", font = ("Arial", 15), bg = wiget_col, fg = text_col, bd = 0, command = lambda n = num: delete_book(n))
            canvas.create_window(w - 50, y + 45, window = del_btn, tags = "book")
            y += 120
    canvas.configure(scrollregion = (0, 0, w, y + 50))




sort_btn = tk.Button(root, text = "сортировка", font = ("Arial", 20), fg = top_col, bg = inp_col, bd = 0, command = opsomu)
sort_btn.place(x = 100, y = 750, anchor = tk.CENTER)
sort_btn = tk.Button(root, text = "фильтры", font = ("Arial", 20), fg = top_col, bg = inp_col, bd = 0, command = filts)
sort_btn.place(x = w - 100, y = 750, anchor = tk.CENTER)
cnf_btn = tk.Button(root, text = "❌", font = ("Arial", 10), fg = "#bdc3c7", bg = inp_col, bd = 0, command = lambda: [entry_search.delete(0, tk.END), show_books()])
cnf_btn.place(x = 275, y = 50, anchor = tk.CENTER)
add_btn = tk.Button(root, text = "➕", font = ("Arial", 20), fg = text_col, bg = top_col, bd = 0, command = add_book)
add_btn.place(x = 290 + 75, y = 50, anchor = tk.CENTER)
#main


show_books()
def on_search_change(event):
    if entry_search.get() != "":
        search(entry_search.get().lower())
    else:
        show_books()
entry_search.bind("<KeyRelease>", on_search_change)
root.mainloop()
