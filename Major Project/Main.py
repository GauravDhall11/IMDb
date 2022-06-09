from tkinter import *
from Code_IMDB import *
import webbrowser
window=Tk()
window.geometry("850x700")
img=PhotoImage(file="F:\g.png")
labelbg = Label(
    window,
    image=img
)
labelbg.place(x=0, y=0)
img1=PhotoImage(file="F:\g1.png")
labelbg1 = Label(
    window,
    image=img1
)
labelbg1.place(x=850, y=5)
window.configure(bg="floral white")
lb1=Label(window, text="Movie_Crawler", fg='blue', font=("Calisto MT", 20,'italic', 'bold'))
lb1.pack(side="top",padx="5",pady="5")
lb2=Label(window,text="Title:",fg='green',font=('Calibri',18,'italic','bold'))
lb2.place(x=5,y=70)
lb3=Label(window,text="Story:",fg='orange',font=('Calibri',18,'italic','bold'))
lb3.place(x=5,y=120)
lb4=Label(window,text="Details:",fg='red',font=('Calibri',18,'italic','bold'))
lb4.place(x=5,y=260)
lb5=Label(window,text="Story_line:",fg='purple',font=('Calibri',18,'italic','bold'))
lb5.place(x=590,y=260)
lb6=Label(window,text="Rating:",fg='yellow',font=('Calibri',18,'italic','bold'),bg="floral white")
lb6.place(x=5,y=600)
#lb7=Label(window,text="Image")
#lb7.place(x=1070,y=80)
lb8=Label(window,text="Reviews:",fg='brown',font=('Calibri',18,'italic','bold'),bg="floral white")
lb8.place(x=5,y=400)
lb9=Label(window,text="Trailer:",fg='blue',font=('Calibri',18,'italic','bold'),bg="floral white")
lb9.place(x=990,y=590)
def callback(url):
   webbrowser.open_new_tab(url)
lb9.bind("<Button-1>", lambda e:
callback("https://www.youtube.com/results?search_query="+moviename+"+trailer"))
lb10=Label(window,text="Photos:",fg='grey',font=('Calibri',18,'italic','bold'),bg="floral white")
lb10.place(x=1075,y=590)
lb10.bind("<Button-1>", lambda e:
callback("https://www.google.com/search?q="+moviename+"+images"))
lb11=Label(window,text="Videos:",fg='red',font=('Calibri',18,'italic','bold'),bg="floral white")
lb11.place(x=1165,y=590)
lb11.bind("<Button-1>", lambda e:
callback("https://www.google.com/search?q="+moviename+"+videos"))
lb12=Label(window,text="Movie_List:",fg='brown',font=('Calibri',18,'italic','bold'),bg="floral white")
lb12.place(x=587,y=520)
text=Text(window,height=1,width=22,wrap="word",borderwidth="2")
Details=details_()
text.insert(END,Details)
text.config(font=('Calibri', 16, 'italic','bold'),state='disabled')
text.place(x=75,y=70)
text1=Text(window,height=4,width=57,wrap="word",borderwidth="2")
Details2=details_2()
text1.insert(END,Details2)
text1.config(font=('Calibri', 16, 'italic'),state='disabled')
text1.place(x=75,y=120)
text2=Text(window,height=4,width=39,wrap="word",borderwidth="2")
Details3=details_3()
text2.insert(END,Details3)
text2.config(font=('Calibri', 16, 'italic'),state='disabled',pady=10)
text2.place(x=105,y=260)
text3=Text(window,height=9,width=48,wrap="word",borderwidth="2")
Details4=details_4()
text3.insert(END,Details4)
text3.config(font=('Calibri', 16, 'italic'),state='disabled')
text3.place(x=710,y=260)
text4=Text(window,height=1,width=10,wrap="word",borderwidth="2")
Details5=details_5()
text4.insert(END,Details5)
text4.config(font=('Calibri', 16, 'italic'),state='disabled',pady=10)
text4.place(x=105,y=600)
'''
text5=Text(window, height=10, width=15)
#Details6=details_6()
#canvas = Canvas(window, width = 300, height = 300)
#canvas.pack()
photo=PhotoImage(file="./assets/imdb.png")
#canvas.create_image(20,20, anchor=NW, image=photo)
text5.insert(END,photo)
text5.image_create(END, image=photo)
text5.pack(side=RIGHT)
text5.place(x=1120,y=80)
'''
text6=Text(window,height=7,width=39,wrap="word",borderwidth="2")
Details7=details_7()
text6.insert(END,Details7)
text6.config(font=('Calibri', 16, 'italic'),state='disabled')
text6.place(x=105,y=410)

#def Callback():
   #webbrowser.open_new_tab("https://www.imdb.com/find?ref_=nv_sr_fn&q="+clicked)

options = [
    "Uri: The Surgical Strike", "Gully Boy", "Kesari","Article 15", "Section 375","Bala","Good Newwz","Mardaani 2","Dream Girl","Chhichhore",
    "Batla House","Super 30","Kabir Singh","Brightburn","Shazam!","Booksmart","Joker","Avengers:Endgame","Rocketman","Us","Official Secrets"
]
clicked = StringVar()
clicked.set("Select movie")
#movie="https://www.imdb.com/find?q="+clicked1
drop = OptionMenu( window , clicked , *options)
drop.config(width=20,bg="floral white")
drop.pack()
drop.place(x=712,y=520)
#button = Button( window , text = "click Me" , command = Callback()).pack()
label = Label( window , text = "Click me",fg='cyan',font=('Calibri',18,'italic','bold'),bg="floral white")
label.bind("<Button-1>", lambda e:
callback("https://www.imdb.com/find?q="+clicked.get()))
label.pack()
label.place(x=735,y=560)
labelbg2=Label(window,text="Hyperlinks",fg='green',font=('Calibri',18,'italic','bold'),bg="floral white")
labelbg2.place(x=1050,y=520)
window.title('Welcome')
window.mainloop()
