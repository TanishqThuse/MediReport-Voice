from tkinter import *
from tkinter import filedialog
from tkinter import messagebox  
import prescription as pr
import speech_recognition as sr
import cv2
from PIL import Image,ImageTk
import pyttsx3
import os
import smtplib
import base64
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.environ["TCL_LIBRARY"] = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tk8.6"

window = Tk()
window.title("< JUST - A - WORD >")
window.iconbitmap("@icon.xbm")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(),window.winfo_screenheight()-50))
window.resizable(0,0)
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def cv():
    img = cv2.cvtColor(pr.templete, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(int(img.shape[1]*(window.winfo_screenheight()/float(img.shape[0]))),window.winfo_screenheight() - 50))
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image= img)
    image_frame.ImageTk = img
    image_frame.configure(image = img)
    showid = image_frame.after(10,show)

left_frame = Frame(window)
image_frame = Label(left_frame)
image_frame.grid(row=0,column=0)
left_frame.grid()

middle_frame = Frame(window,width =0.700,highlightcolor='green',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50)

def name():
    with sr.Microphone() as source:
        speak("patient's name")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            name_entry.insert(0,t1)
            pr.name(name_entry.get())
        except:
            speak('could not recognize')

name_label = Label(middle_frame,text="Name",font=("Poor Richard",15))
name_label.grid(row=1,column=0)
name_entry = Entry(middle_frame,width=50)
name_entry.grid(row=1,column=1)
b = Button(middle_frame, text="name",bg='lightgreen', command=name)
b.config( height = 1, width = 6)
b.grid(row=1,column=5)

def age():
    with sr.Microphone() as source:
        speak("patient's age")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            age_entry.insert(0,t1)
            pr.age(age_entry.get())
        except:
            speak('could not recognize')

age_label = Label(middle_frame,text="age",font=("Poor Richard",15))
age_label.grid(row=5,column=0)
age_entry = Entry(middle_frame,width=50)
age_entry.grid(row=5,column=1)
b1 = Button(middle_frame, text="age",bg='lightgreen', command=age)
b1.config( height = 1, width = 6)
b1.grid(row=5,column=5)

def gender():
    with sr.Microphone() as source:
        speak("patient's gender")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            if t1=='mail':
                t1='male'
            gen_entry.insert(0,t1)
            pr.gender(gen_entry.get())
        except:
            speak('could not recognize')

gen_label = Label(middle_frame,text="gender",font=("Poor Richard",15))
gen_label.grid(row=10,column=0)
gen_entry = Entry(middle_frame,width=50)
gen_entry.grid(row=10,column=1)
b2 = Button(middle_frame, text="gender",bg='lightgreen', command=gender)
b2.config( height = 1, width = 6)
b2.grid(row=10,column=5)

def serial():
    with sr.Microphone() as source:
        speak("patient's serial number")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            sl_entry.insert(0,t1)
            pr.serial(sl_entry.get())
        except:
            speak('could not recognize')

sl_label = Label(middle_frame,text="serial",font=("Poor Richard",15))
sl_label.grid(row=15,column=0)
sl_entry = Entry(middle_frame,width=50)
sl_entry.grid(row=15,column=1)
b3 = Button(middle_frame, text="serial",bg='lightgreen', command=serial)
b3.config( height = 1, width = 6)
b3.grid(row=15,column=5)

count=0
def medicines():
    global count
    with sr.Microphone() as source:
        speak("patient's medicines")
        try:
            count+=1
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            t1=t1.replace('tablets','').strip()
            t1=t1.split()
            md_entry.insert(0,t1[0])
            pr.medicine(count,t1[0],t1[1],0,1)
        except:
            speak('could not recognize')

md_label = Label(middle_frame,text="medicines",font=("Poor Richard",15))
md_label.grid(row=20,column=0)
md_entry = Entry(middle_frame,width=50)
md_entry.grid(row=20,column=1)
b4 = Button(middle_frame, text="medicines",bg='lightgreen', command=medicines)
b4.config( height = 1, width = 8)
b4.grid(row=20,column=5)

def symptoms():
    with sr.Microphone() as source:
        speak("patient's symptoms")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            sm_entry.insert(0,t1)
            pr.symptoms(sm_entry.get())
        except:
            speak('could not recognize')

sm_label = Label(middle_frame,text="symptoms",font=("Poor Richard",15))
sm_label.grid(row=30,column=0)
sm_entry = Entry(middle_frame,width=50)
sm_entry.grid(row=30,column=1)
b5 = Button(middle_frame, text="symptoms",bg='lightgreen', command=symptoms)
b5.config( height = 1, width = 8)
b5.grid(row=30,column=5)

def diag():
    with sr.Microphone() as source:
        speak("diagnosis")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            dia_entry.insert(0,t1)
            pr.diagnosis(dia_entry.get())
        except:
            speak('could not recognize')

dia_label = Label(middle_frame,text="diagnosis",font=("Poor Richard",15))
dia_label.grid(row=35,column=0)
dia_entry = Entry(middle_frame,width=50)
dia_entry.grid(row=35,column=1)
b6 = Button(middle_frame, text="diagnosis",bg='lightgreen', command=diag)
b6.config( height = 1, width = 8)
b6.grid(row=35,column=5)

def advice():
    with sr.Microphone() as source:
        speak("advice for patient")
        try:
            r.adjust_for_ambient_noise(source,duration=2.0)
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            ad_entry.insert(0,t1)
            pr.advice(ad_entry.get())
        except:
            speak('could not recognize')

ad_label = Label(middle_frame,text="advice",font=("Poor Richard",15))
ad_label.grid(row=40,column=0)
ad_entry = Entry(middle_frame,width=50)
ad_entry.grid(row=40,column=1)
b7 = Button(middle_frame, text="advice",bg='lightgreen', command=advice)
b7.config( height = 1, width = 6)
b7.grid(row=40,column=5)

# 🗣️ New One-shot Dictation Feature
def full_dictation():
    with sr.Microphone() as source:
        speak("Start speaking the full prescription.")
        try:
            r.adjust_for_ambient_noise(source, duration=2.0)
            audio = r.listen(source)
            t = r.recognize_google(audio)
            print("Captured text:", t)

            if 'name' in t:
                name = t.split("name")[1].split("age")[0].strip()
                name_entry.delete(0, END)
                name_entry.insert(0, name)
                pr.name(name)

            if 'age' in t:
                age = t.split("age")[1].split("gender")[0].strip()
                age_entry.delete(0, END)
                age_entry.insert(0, age)
                pr.age(age)

            if 'gender' in t:
                gender = t.split("gender")[1].split("serial")[0].strip()
                gen_entry.delete(0, END)
                gen_entry.insert(0, gender)
                pr.gender(gender)

            if 'serial' in t:
                serial = t.split("serial")[1].split("symptom")[0].strip()
                sl_entry.delete(0, END)
                sl_entry.insert(0, serial)
                pr.serial(serial)

            if 'symptom' in t:
                symptoms = t.split("symptom")[1].split("diagnosis")[0].strip()
                sm_entry.delete(0, END)
                sm_entry.insert(0, symptoms)
                pr.symptoms(symptoms)

            if 'diagnosis' in t:
                diagnosis = t.split("diagnosis")[1].split("medicine")[0].strip()
                dia_entry.delete(0, END)
                dia_entry.insert(0, diagnosis)
                pr.diagnosis(diagnosis)

            if 'medicine' in t:
                meds = t.split("medicine")[1].split("advice")[0].strip()
                md_entry.delete(0, END)
                md_entry.insert(0, meds)
                pr.medicine(0, meds, '', 0, 1)

            if 'advice' in t:
                advice = t.split("advice")[1].strip()
                ad_entry.delete(0, END)
                ad_entry.insert(0, advice)
                pr.advice(advice)

        except Exception as e:
            print(e)
            speak("Could not understand your dictation.")

b10 = Button(middle_frame, text="🗣️ Full Dictation", bg='orange', command=full_dictation)
b10.config(height=2, width=20)
b10.grid(row=42, column=1)

sig_label = Label(middle_frame,text="signature",font=("Poor Richard",15))
sig_label.grid(row=45,column=0)
sig_entry = Entry(middle_frame,width=50)
sig_entry.grid(row=45,column=1)

def save():
    pr.save()
    messagebox.showinfo("information","saved at location : "+os.getcwd())
b8 = Button(middle_frame, text=" --- save --- ",bg='lightgreen', command=save)
b8.config( height = 4, width = 20)
b8.grid(row=50,column=1)

middle_frame.grid(row=0,column=2,stick=E)

# Email Section
right_frame = Frame(window,highlightcolor='red',highlightbackground='blue',highlightthickness=1,height=window.winfo_screenheight()-50)
e = Label(right_frame,text="your mail id ",font=("Poor Richard",15))
e.grid(row=1,column=0)
e_entry = Entry(right_frame,width=50)
e_entry.grid(row=1,column=1)

f = Label(right_frame,text="your password ",font=("Poor Richard",15))
f.grid(row=6,column=0)
f_entry = Entry(right_frame,width=50)
f_entry.config(show='*')
f_entry.grid(row=6,column=1)

g = Label(right_frame,text="host mail id",font=("Poor Richard",15))
g.grid(row=11,column=0)
g_entry = Entry(right_frame,width=50)
g_entry.grid(row=11,column=1)

right_frame.grid(row=0,column=2,sticky=N)

def attachments():
    file_path = filedialog.askopenfilename()
    return file_path

def send():
    try:
        msg = MIMEMultipart()
        filename=attachments()
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(e_entry.get(),f_entry.get())
        server.sendmail(e_entry.get(),g_entry.get(),text)
        server.close()
        messagebox.showinfo("information","< MAIL SENT >") 
    except:
        messagebox.showwarning("warning","mail NOT sent. Try again")  

b9 = Button(right_frame, text=" --- share --- ",bg='magenta', command=send)
b9.config( height = 3, width = 20)
b9.grid(row=20,column=1)

def show():
    pr.name(name_entry.get())
    pr.age(age_entry.get())
    pr.gender(gen_entry.get())
    pr.serial(sl_entry.get())
    pr.medicine(0,md_entry.get(),'',0,1)
    pr.symptoms(sm_entry.get())
    pr.diagnosis(dia_entry.get())
    pr.advice(ad_entry.get())
    pr.signature(sig_entry.get())
    cv()

show()

def about():
    messagebox.showinfo('About <JUST A WORD>! ','JAW is a speech-based prescription generator that can directly send prescriptions via Gmail.\nDeveloped by Bharat Chandra.')

def guide():
    messagebox.showinfo('USER MANUAL',
        '1. Click on buttons (name, age, etc.) to fill fields via voice.\n'
        '2. Or use "Full Dictation" to fill all in one go.\n'
        '3. Click save.\n'
        '4. Enter email details and send the prescription.')

def destroy():
    window.destroy()

menubar = Menu(window)
window.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About", command=about)
subMenu.add_command(label="guide", command=guide)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=destroy)

window.mainloop()
# This code is a GUI application for generating medical prescriptions using speech recognition.

#try - 2 above

# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox  
# import prescription as pr
# import speech_recognition as sr
# import cv2
# from PIL import Image,ImageTk
# import pyttsx3
# import os
# import smtplib
# import base64
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# os.environ["TCL_LIBRARY"] = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tcl8.6"
# os.environ["TK_LIBRARY"] = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tk8.6"

# window = Tk()
# window.title("< JUST - A - WORD >")
# #window.iconbitmap("ICON vp.ico")
# window.iconbitmap("@icon.xbm")
# window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(),window.winfo_screenheight()-50))
# window.resizable(0,0)
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# r=sr.Recognizer()
# def cv():
#     img = cv2.cvtColor(pr.templete, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img,(int(img.shape[1]*(window.winfo_screenheight()/float(img.shape[0]))),window.winfo_screenheight() - 50))
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(image= img)
#     image_frame.ImageTk = img
#     image_frame.configure(image = img)
#     showid = image_frame.after(10,show)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# r=sr.Recognizer()
   
# left_frame = Frame(window)
# image_frame = Label(left_frame)
# image_frame.grid(row=0,column=0)
# left_frame.grid()
# middle_frame = Frame(window,width =0.700,highlightcolor='green',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50)
# def name():
#         with sr.Microphone() as source:
                 
#                 speak("patient\'s name")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         name_entry.insert(0,t1)
#                         pr.name(name_entry.get())
#                 except:
#                         speak(' could not recognize ')
# name_label = Label(middle_frame,text="Name",font=("Poor Richard",15))
# name_label.grid(row=1,column=0)
# name_entry = Entry(middle_frame,width=50)
# name_entry.grid(row=1,column=1)
# b = Button(middle_frame, text="name",bg='lightgreen', command=name)
# b.config( height = 1, width = 6)
# b.grid(row=1,column=5)
# def age():
#         with sr.Microphone() as source:
                 
#                 speak("patient\'s age")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         age_entry.insert(0,t1)
#                         pr.age(age_entry.get())
#                 except:
#                         speak(' could not recognize ')
# age_label = Label(middle_frame,text="age",font=("Poor Richard",15))
# age_label.grid(row=5,column=0)
# age_entry = Entry(middle_frame,width=50)
# age_entry.grid(row=5,column=1)
# b1 = Button(middle_frame, text="age",bg='lightgreen', command=age)
# b1.config( height = 1, width = 6)
# b1.grid(row=5,column=5)
# def gender():
#         with sr.Microphone() as source:
#                 speak("patient\'s gender")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         if t1=='mail':
#                             t1='male'
#                         gen_entry.insert(0,t1)
#                         pr.gender(gen_entry.get())
#                 except:
#                         speak(' could not recognize ')
# gen_label = Label(middle_frame,text="gender",font=("Poor Richard",15))
# gen_label.grid(row=10,column=0)
# gen_entry = Entry(middle_frame,width=50)
# gen_entry.grid(row=10,column=1)
# b2 = Button(middle_frame, text="gender",bg='lightgreen', command=gender)
# b2.config( height = 1, width = 6)
# b2.grid(row=10,column=5)
# def serial():
#         with sr.Microphone() as source:
                 
#                 speak("patient\'s serial nmber")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         sl_entry.insert(0,t1)
#                         pr.serial(sl_entry.get())
#                 except:
#                         speak(' could not recognize ')
# sl_label = Label(middle_frame,text="serial",font=("Poor Richard",15))
# sl_label.grid(row=15,column=0)
# sl_entry = Entry(middle_frame,width=50)
# sl_entry.grid(row=15,column=1)
# b3= Button(middle_frame, text="serial",bg='lightgreen', command=serial)
# b3.config( height = 1, width = 6)
# b3.grid(row=15,column=5)
# count=0
# def medicines():
#         global count
#         with sr.Microphone() as source: 
#                 speak("patient\'s medicines")
#                 try:
#                         count+=1
#                         r.adjust_for_ambient_noise(source,duration=1)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         t1.remove('tablets')
#                         t1=t1.split()
#                         md_entry.insert(0,t1[0])
#                         pr.medicine(count,t1[0],t1[1],0,1)
#                 except:
#                         speak(' could not recognize ')
# md_label = Label(middle_frame,text="medicines",font=("Poor Richard",15))
# md_label.grid(row=20,column=0)
# md_entry = Entry(middle_frame,width=50)
# md_entry.grid(row=20,column=1)
# ##md1_label = Label(middle_frame,text="Qty ,ab(0 or 1) , time ",font=("Poor Richard",15))
# ##md1_label.grid(row=25,column=0)
# ##md1_entry = Entry(middle_frame,width=10)
# ##md1_entry.grid(row=25,column=3)
# ##md2_entry = Entry(middle_frame,width=10)
# ##md2_entry.grid(row=25,column=4)
# ##md3_entry = Entry(middle_frame,width=10)
# ##md3_entry.grid(row=25,column=5)
# b4= Button(middle_frame, text="medicines",bg='lightgreen', command=medicines)
# b4.config( height = 1, width = 8)
# b4.grid(row=20,column=5)
# def symptoms():
#         with sr.Microphone() as source:
                 
#                 speak("patient\'s symptoms")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         sm_entry.insert(0,t1)
#                         pr.symptoms(sm_entry.get())
#                 except:
#                         speak(' could not recognize ')
# sm_label = Label(middle_frame,text="symptoms",font=("Poor Richard",15))
# sm_label.grid(row=30,column=0)
# sm_entry = Entry(middle_frame,width=50)
# sm_entry.grid(row=30,column=1)
# b5 = Button(middle_frame, text="symptoms",bg='lightgreen', command=symptoms)
# b5.config( height = 1, width = 8)
# b5.grid(row=30,column=5)
# def diag():
#         with sr.Microphone() as source:
                 
#                 speak(" diagnosis ")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         dia_entry.insert(0,t1)
#                         pr.diagnosis(dia_entry.get())
#                 except:
#                         speak(' could not recognize ')
# dia_label = Label(middle_frame,text="diagnosis",font=("Poor Richard",15))
# dia_label.grid(row=35,column=0)
# dia_entry = Entry(middle_frame,width=50)
# dia_entry.grid(row=35,column=1)
# b6 = Button(middle_frame, text="diagnosis",bg='lightgreen', command=diag)
# b6.config( height = 1, width = 8)
# b6.grid(row=35,column=5)
# def advice():
#         with sr.Microphone() as source:
                 
#                 speak("advice for patient")
#                 try:
#                         r.adjust_for_ambient_noise(source,duration=0.7)
#                         audio= r.listen(source)
#                         t1 = r.recognize_google(audio)
#                         ad_entry.insert(0,t1)
#                         pr.advice(ad_entry.get())
#                 except:
#                         speak(' could not recognize ')
# ad_label = Label(middle_frame,text="advice",font=("Poor Richard",15))
# ad_label.grid(row=40,column=0)
# ad_entry = Entry(middle_frame,width=50)
# ad_entry.grid(row=40,column=1)
# b7 = Button(middle_frame, text="advice",bg='lightgreen', command=advice)
# b7.config( height = 1, width = 6)
# b7.grid(row=40,column=5)
# sig_label = Label(middle_frame,text="signature",font=("Poor Richard",15))
# sig_label.grid(row=45,column=0)
# sig_entry = Entry(middle_frame,width=50)
# sig_entry.grid(row=45,column=1)

# def save():
#         pr.save()
#         messagebox.showinfo("information","saved at location : "+os.getcwd())
# b8 = Button(middle_frame, text=" --- save --- ",bg='lightgreen', command=save)
# b8.config( height = 4, width = 20)
# b8.grid(row=50,column=1)

# middle_frame.grid(row=0,column=2,stick=E)

# right_frame = Frame(window,highlightcolor='red',highlightbackground='blue',highlightthickness=1,height=window.winfo_screenheight()-50)
# e = Label(right_frame,text="your mail id ",font=("Poor Richard",15))
# e.grid(row=1,column=0)
# e_entry = Entry(right_frame,width=50)
# e_entry.grid(row=1,column=1)

# f= Label(right_frame,text="your password ",font=("Poor Richard",15))
# f.grid(row=6,column=0)
# f_entry = Entry(right_frame,width=50)
# f_entry.config(show='*')
# f_entry.grid(row=6,column=1)
# g= Label(right_frame,text="host mail id",font=("Poor Richard",15))
# g.grid(row=11,column=0)
# g_entry = Entry(right_frame,width=50)
# g_entry.grid(row=11,column=1)
# right_frame.grid(row=0,column=2,sticky=N)
# def attachments():
#     file_path = filedialog.askopenfilename()
#     return file_path
# def send():
#     try:
#         msg = MIMEMultipart()
#         filename=attachments()
#         with open(filename, "rb") as attachment:
#             part = MIMEBase("application", "octet-stream")
#             part.set_payload(attachment.read())

#         encoders.encode_base64(part)

#         part.add_header(
#             "Content-Disposition",
#             f"attachment; filename= {filename}",)
#         msg.attach(part)
#         text = msg.as_string()
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(e_entry.get(),f_entry.get())
#         server.sendmail(e_entry.get(),g_entry.get(),text)
#         server.close()
#         messagebox.showinfo("information","< MAIL SENT >") 
#     except:
#         messagebox.showwarning("warning","mail NOT sent. Try again")  
 
# b9 = Button(right_frame, text=" --- share --- ",bg='magenta', command=send)
# b9.config( height = 3, width = 20)
# b9.grid(row=20,column=1)
# def show():
#     pr.name(name_entry.get())
#     pr.age(age_entry.get())
#     pr.gender(gen_entry.get())
#     pr.serial(sl_entry.get())
#     pr.medicine(0,md_entry.get(),'',0,1)
#     pr.symptoms(sm_entry.get())
#     pr.diagnosis(dia_entry.get())
#     pr.advice(ad_entry.get())
#     pr.signature(sig_entry.get())
#     cv()
# show()
# def about():
#         messagebox.showinfo('About <JUST A WORD>! ','JAW is a application that designes medical prescription based on speech recognition.'
#                                               ' which can directly sent to patient via gmail.\n'
#                                               '-Developed by Bharat Chandra.\n\nMobile version will be soon...')
# def guide():
#     messagebox.showinfo('USER MANUAL',
#         '1.click on the button that u want to fill the field.\n'
#                         'eg: name,age,advice,etc...\n'
#                         '2.click on save button after completion of writing prescription.\n'
#                         '3.enter mail and click on send button to select file and send.')
# def destroy():
#     window.destroy()
# menubar = Menu(window)
# window.config(menu=menubar)
# subMenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Help", menu=subMenu)
# subMenu.add_command(label="About", command=about)
# subMenu.add_command(label="guide", command=guide)
# subMenu.add_separator()
# subMenu.add_command(label="Exit", command=destroy)
# window.mainloop()
