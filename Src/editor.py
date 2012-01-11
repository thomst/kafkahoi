#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import Tkinter as tk
import tkMessageBox

class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editor")

        self.conn = sqlite3.connect('db')
        self.f_list = 0

        self.add()
        self.list()
        #self._popup()  #Wie auf die Zwischenablag zugreifen?

        self.root.mainloop()

    def _popup(self):
        self.popup = tk.Menu(self.f_add, tearoff=0)
        self.popup.add_command(label='paste', command=self.paste)

        self.titleform.bind('<Button-3>', self.pos)
        self.poemform.bind('<Button-3>', self.pos)

    def pos(self, event):
        self.popup.post(event.x_root, event.y_root)

    def paste(self):
        pass

    def add(self):
        self.f_add = tk.Frame(self.root)
        self.f_add.pack()

        oben_l = tk.Frame(self.f_add)
        oben_l.pack(fill=tk.X)
        title = tk.Label(oben_l, text=u"title:")
        title.pack(side=tk.LEFT)

        oben_f = tk.Frame(self.f_add)
        oben_f.pack(fill=tk.X)
        self.titleform = tk.Entry(oben_f, width=20)
        self.titleform.pack(fill=tk.X)

        mitte = tk.Frame(self.f_add)
        mitte.pack(fill=tk.X)
        poem = tk.Label(mitte, text=u"poem:")
        poem.pack(side=tk.LEFT)

        unten = tk.Frame(self.f_add)
        unten.pack()
        self.poemform = tk.Text(unten, height=20, width=50)
        self.poemform.pack()

        button = tk.Button(unten, text="save", command=self.save)
        button.pack(side=tk.RIGHT)

    def save(self):
        title = self.titleform.get()
        poem = self.poemform.get('1.0', tk.END)

        if title and poem and not poem == '\n':
            curs = self.conn.cursor()
            curs.execute('insert into poems values (?, ?)', (title, poem))
            self.conn.commit()
            #curs.execute('select * from poems')
            #for r in curs: print r

            self.titleform.delete(0, tk.END)
            self.poemform.delete('1.0',tk.END)

            self.list()
            tkMessageBox.showinfo('saved', 'saved {0}'.format(title))
        elif title: tkMessageBox.showinfo('info', 'please also insert a poem')
        elif poem and not poem == '\n': 
            tkMessageBox.showinfo('info', 'please also insert a title')
        else: tkMessageBox.showinfo('info', 'please insert a title and a poem')

    def list(self):
        if self.f_list: self.f_list.destroy()
        self.f_list = tk.Frame(self.root)
        self.f_list.pack(fill=tk.BOTH)

        curs = self.conn.cursor()
        curs.execute('select title from poems order by title')
        self.items = [x for x in curs]

        # Kleiner Info Text
        label = tk.Frame(self.f_list)
        label.pack(fill=tk.BOTH)
        tk.Label(label, text="choose one or more to delete:").pack(side=tk.LEFT)

        # Die Listbox erstellen
        self.listbox = tk.Listbox(
            self.f_list,
            selectmode=tk.MULTIPLE, # multiple choice
            #selectmode=tk.SINGLE # single select mode
            height=5, width=25
        )
        self.listbox.pack(fill=tk.BOTH)

        # Einträge einfügen
        for txt in self.items:
            self.listbox.insert(tk.END, txt)

        # Vor-Aktivierte Punkte selektieren
        #for index in activated:
        #    self.listbox.selection_set(index)

        b = tk.Button(self.f_list, text = "delete", command=self.delete)
        b.pack(side=tk.RIGHT)

    def delete(self):
        selection = []
        for i in self.listbox.curselection():
            index = int(i) # i ist ein String
            selection.append(self.items[index])

        if selection:
            curs = self.conn.cursor()
            curs.executemany('delete from poems where title=?', selection)
            self.conn.commit()

            self.list()
            tkMessageBox.showinfo('delete', 'deleted: {0}'.format(', '.join([x[0] for x in selection])))

if __name__ == '__main__':
    Main()
