from cProfile import label
import datetime
from tkinter import*
import random
import tkinter.font as tkFont
from tkinter.ttk import Labelframe
from turtle import color
from cv2 import resize
from pandas import to_datetime
import qrcode
from PIL import Image, ImageTk
import time
import schedule

def valider ():
    doc_save=open("card.txt","a+")
    bankentry.get()
    card_number_entry.get()
    expire_month_entry.get()
    expire_year_entry.get()
    cvv_entry.get()

    cardFinal=[]
    cardFinal.append("LE NOM DE LA BANQUE EST: "+bankentry.get())
    cardFinal.append("LE NUMERO DE LA CARTE EST: "+card_number_entry.get())
    cardFinal.append("LE MOIS D'EXPIRATION EST: "+expire_month_entry.get())
    cardFinal.append("L'ANNEE D'EXPIRATION EST: "+expire_year_entry.get())
    cardFinal.append("LE CVV EST : "+cvv_entry.get())
    cardFinal.append(to_datetime(datetime.datetime.now()))
    doc_save.write(str(cardFinal)+"\n")
    
    print(cardFinal)
    doc_save.close()    

    qr = qrcode.QRCode(
        version=15, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
    )            

    qr.add_data(str(cardFinal))
    qr.make()
    img = qr.make_image()
    img.save(bankentry.get()+"_card"+".png")


    photo=PhotoImage(file=bankentry.get()+"_card"+".png")
    label=Label(card_gestion,image=photo)
    label.place(x=600,y=150)


def reset():
    bankentry.delete(0,END)
    card_number_entry.delete(0,END)
    expire_month_entry.delete(0,END)
    expire_year_entry.delete(0,END)
    cvv_entry.delete(0,END)
    
    
    

card_gestion  = Tk()
card_gestion.title("Card")
card_gestion.geometry("960x540")
card_gestion.resizable(width=False, height=False)

bank_font=tkFont.Font(family="Helvetica", size=14, weight="bold")

bank=Label(card_gestion,text="Bank name : ",bg="white",fg="black",font=bank_font)
bankentry=Entry(card_gestion)
bankentry.place(x=600,y=5)
bank.pack()

card_number=Label(card_gestion,text="Numéro de la, carte :",bg="white",fg="black",font=bank_font)
card_number_entry=Entry(card_gestion)
card_number_entry.place(x=600,y=35)
card_number.pack()

expire_month=Label(card_gestion,text="Expire Month:",bg="white",fg="black",font=bank_font)
expire_month_entry=Entry(card_gestion)
expire_month_entry.place(x=600,y=60)
expire_month.pack()

expire_year=Label(card_gestion,text="Expire Year:",bg="white",fg="black",font=bank_font)
expire_year_entry=Entry(card_gestion)
expire_year_entry.place(x=600,y=90)
expire_year.pack()

cvv=Label(card_gestion,text="CVV2 ou CVC2:",bg="white",fg="black",font=bank_font)
cvv_entry=Entry(card_gestion)
cvv_entry.place(x=600,y=115)
cvv.pack()



valider=Button(card_gestion,text="Valider",bg="white",fg="black",font=bank_font, command=valider)
valider.place(x=100,y=155)
valider.pack()

reset=Button(card_gestion,text="Reset",bg="white",fg="black",font=bank_font, command=reset)
reset.place(x=100,y=400)
reset.pack()

quit=Button(card_gestion,text="Quit",bg="white",fg="black",font=bank_font, command=card_gestion.destroy)
quit.place(x=100,y=430)
quit.pack()

card_gestion.mainloop()

#credit card manager
#TODO :resize l'image du qr code qui s'affiche dans le label 


