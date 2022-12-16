from tkinter import *
from tkinter import ttk, messagebox
from Mediateka_database import BD
from tkinter.filedialog import *
from PIL import ImageTk, Image

bd = BD()
# bd.create_database()
# bd.add_table()

class Window:
    def __init__(self, window):
        self.window = window
        self.window.geometry("650x500+{}+{}".format(300, 100))
        Label(self.window, text="Назва", font='None, 10').place(x=0, y=10, width=60, height=24)
        Label(self.window, text="Рік", font='None, 10').place(x=0, y=44, width=60, height=24)
        Label(self.window, text="Жанр", font='None, 10').place(x=340, y=10, width=60, height=24)
        Label(self.window, text="IMDB", font='None, 10').place(x=340, y=44, width=60, height=24)
        Label(self.window, text='Фото', font='None, 10').place(x=0, y=88, width=60, height=24)
        self.txt_title = Entry(self.window)
        self.txt_title.place(x=70, y=10, width=220, height=24)
        self.txt_year = Entry(self.window)
        self.txt_year.place(x=70, y=44, width=220, height=24)
        self.genre = [" ", "Бойовик", "Комедія", "Мультфільм", "Сімейний", "Фантастика"]
        self.combo_genre = ttk.Combobox(self.window, values=self.genre, state="readonly")
        self.combo_genre.place(x=400, y=10, width=220, height=24)
        self.txt_imdb = Entry(self.window)
        self.txt_imdb.place(x=400, y=44, width=220, height=24)
        self.but_photo = Button(self.window, text='Додати фото', font=(None, 10), command=self.dialog_photo)
        self.but_photo.place(x=70, y=88, width=220, height=24)
        self.btn_show = Button(self.window, text="Показати все", width=18 , command=self.films_show)
        self.btn_show.place(x=400, y=90, width=220, height=24)
        self.btn_search = Button(self.window, text="Пошук фільму", width=18,  command=self.film_search)
        self.btn_search.place(x=400, y=120, width=220, height=24)
        self.btn_add = Button(self.window, text="Додати фільм", width=18 , command=self.film_add)
        self.btn_add.place(x=400, y=150, width=220, height=24)
        self.btn_exit = Button(self.window, text="Вихід", width=18, command=window.destroy)
        self.btn_exit.place(x=400, y=180, width=220, height=24)
        # Резервування місця під мітку для виведення фото
        self.image_label = Label(self.window, image=None)
        self.image_label.place(x=70, y=120)
        columns = ('Id', 'Film_title', 'Year', 'Genre', 'IMDB')
        self.tree = ttk.Treeview(self.window, columns=columns, show='headings', selectmode='browse')
        self.tree.heading('Id', text='Id')
        self.tree.column('Id', width=50, stretch=NO)
        self.tree.heading('Film_title', text='Назва')
        self.tree.column('Film_title', width=200, stretch=NO)
        self.tree.heading('Year', text='Рік виходу')
        self.tree.column('Year', width=80, stretch=NO)
        self.tree.heading('Genre', text='Жанр фільму')
        self.tree.column('Genre', width=120, stretch=NO)
        self.tree.heading('IMDB', text='IMDB рейтинг')
        self.tree.column('IMDB', width=120, stretch=NO)
        self.tree.place(x=30, y=270)
        self.vertical_scroll = ttk.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.vertical_scroll.place(x=30 + 570 + 2, y=270, height=200 + 25)
        self.tree.bind("<<TreeviewSelect>>", self.show_selection)

    def visualize_photo(self, var):
        image = Image.open(var)
        image = ImageTk.PhotoImage(image.resize((150, 130)))
        self.image_label.photo = image
        self.image_label.config(image=image)

    def dialog_photo(self):
        try:
            self.path = askopenfilename(filetypes=(("Графічні формати", "*.png; *.jpg"), ("Всі файли", "*.*")))
            self.visualize_photo(self.path)
        except:
            messagebox.showerror('Помилка', 'Файл не обрано')

    def film_add(self):
        try:
            bd.add(self.txt_title.get().strip(), self.txt_year.get().strip(), self.combo_genre.get(),
                   self.txt_imdb.get().strip(), self.path)
            self.entry_clear()
            self.films_show()
        except:
            messagebox.showerror('Помилка', 'Щось пішло не так')

    def entry_clear(self):
        self.txt_title.delete(0, END)
        self.txt_year.delete(0, END)
        self.combo_genre.current(0)
        self.txt_imdb.delete(0, END)
        self.image_label.config(image='')

    def films_show(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        all_results = bd.show()
        print(all_results)
        for i in all_results:
            print(i)
            self.tree.insert('', END, values=i)

    def show_selection(self, event):
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            self.index_vubranuj = item["values"][0:5]
            print(self.index_vubranuj[3])
            self.entry_clear()
            self.txt_title.insert(END, self.index_vubranuj[1])
            self.txt_year.insert(END, self.index_vubranuj[2])
            for poz, znach in enumerate(self.genre):
                if znach == self.index_vubranuj[3]:
                    self.combo_genre.current(poz)
            self.txt_imdb.insert(END, self.index_vubranuj[4])
            self.show_pic(self.index_vubranuj[0])

    def show_pic(self, id):
        rez = bd.readBlobData(id)
        self.visualize_photo(rez)

    def film_search(self):
        try:
            for row in self.tree.get_children():
                self.tree.delete(row)
            data = bd.search(self.txt_title.get(), self.txt_year.get(), self.combo_genre.get(),
                             self.txt_imdb.get())
            print(self.txt_title.get(), self.txt_year.get(), self.combo_genre.get(),
                  self.txt_imdb.get())
            if len(data) == 0:
                messagebox.showwarning("Увага", "Не знайдено результатів, які б відповідали вашим критеріям пошуку.")
            else:
                for i in data:
                    self.tree.insert('', END, values=i)

        except:
            messagebox.showwarning("Увага", "Введіть критерії пошуку!")


root = Tk()
main_window=Window(root)
root.mainloop()
