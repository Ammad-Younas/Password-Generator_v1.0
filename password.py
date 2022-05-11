from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import string
import random

root = Tk()

root.title("Password-Generator | Cyber-Spider")
root.iconbitmap('icon/logo.ico')
root.geometry("640x400+350+150")
root.resizable(height=FALSE, width=FALSE)


def upper():
    if password_variable.get() == 0 or password_variable.get() >= 27:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 27")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u1 = string.ascii_uppercase
        list1 = []
        list1.extend(list(u1))
        random.shuffle(list1)
        output_text.config(state=NORMAL)
        result1 = "".join(list1[0:int(password_variable.get())])
        output_text.insert('1.0', result1)
        output_text.config(state=DISABLED)


def lower():
    if password_variable.get() == 0 or password_variable.get() >= 27:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 27")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        l1 = string.ascii_lowercase
        list2 = []
        list2.extend(list(l1))
        random.shuffle(list2)
        output_text.config(state=NORMAL)
        result2 = "".join(list2[0:int(password_variable.get())])
        output_text.insert('1.0', result2)
        output_text.config(state=DISABLED)


def digit():
    if password_variable.get() == 0 or password_variable.get() >= 11:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 11")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        d1 = string.digits
        list3 = []
        list3.extend(list(d1))
        random.shuffle(list3)
        output_text.config(state=NORMAL)
        result3 = "".join(list3[0:int(password_variable.get())])
        output_text.insert('1.0', result3)
        output_text.config(state=DISABLED)


def punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 33:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 33")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        p1 = string.punctuation
        list4 = []
        list4.extend(list(p1))
        random.shuffle(list4)
        output_text.config(state=NORMAL)
        result4 = "".join(list4[0:int(password_variable.get())])
        output_text.insert('1.0', result4)
        output_text.config(state=DISABLED)


def upper_and_lower():
    if password_variable.get() == 0 or password_variable.get() >= 53:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 53")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u2 = string.ascii_uppercase
        l2 = string.ascii_lowercase
        list5 = []
        list5.extend(list(u2))
        list5.extend(list(l2))
        random.shuffle(list5)
        output_text.config(state=NORMAL)
        result5 = "".join(list5[0:int(password_variable.get())])
        output_text.insert('1.0', result5)
        output_text.config(state=DISABLED)


def upper_and_digit():
    if password_variable.get() == 0 or password_variable.get() >= 37:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 37")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u3 = string.ascii_uppercase
        d2 = string.digits
        list6 = []
        list6.extend(list(u3))
        list6.extend(list(d2))
        random.shuffle(list6)
        output_text.config(state=NORMAL)
        result6 = "".join(list6[0:int(password_variable.get())])
        output_text.insert('1.0', result6)
        output_text.config(state=DISABLED)


def upper_and_punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 59:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 59")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u4 = string.ascii_uppercase
        p2 = string.punctuation
        list7 = []
        list7.extend(list(u4))
        list7.extend(list(p2))
        random.shuffle(list7)
        output_text.config(state=NORMAL)
        result7 = "".join(list7[0:int(password_variable.get())])
        output_text.insert('1.0', result7)
        output_text.config(state=DISABLED)


def lower_and_digit():
    if password_variable.get() == 0 or password_variable.get() >= 37:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 37")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        l3 = string.ascii_lowercase
        d3 = string.digits
        list8 = []
        list8.extend(list(l3))
        list8.extend(list(d3))
        random.shuffle(list8)
        output_text.config(state=NORMAL)
        result8 = "".join(list8[0:int(password_variable.get())])
        output_text.insert('1.0', result8)
        output_text.config(state=DISABLED)


def lower_and_punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 59:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 59")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        l4 = string.ascii_lowercase
        p3 = string.punctuation
        list9 = []
        list9.extend(list(l4))
        list9.extend(list(p3))
        random.shuffle(list9)
        output_text.config(state=NORMAL)
        result9 = "".join(list9[0:int(password_variable.get())])
        output_text.insert('1.0', result9)
        output_text.config(state=DISABLED)


def digit_and_punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 43:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 43")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        d4 = string.digits
        p4 = string.punctuation
        list10 = []
        list10.extend(list(d4))
        list10.extend(list(p4))
        random.shuffle(list10)
        output_text.config(state=NORMAL)
        result10 = "".join(list10[0:int(password_variable.get())])
        output_text.insert('1.0', result10)
        output_text.config(state=DISABLED)


def upper_and_lower_and_digit():
    if password_variable.get() == 0 or password_variable.get() >= 63:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 63")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u5 = string.ascii_uppercase
        l5 = string.ascii_lowercase
        d5 = string.digits
        list11 = []
        list11.extend(list(u5))
        list11.extend(list(l5))
        list11.extend(list(d5))
        random.shuffle(list11)
        output_text.config(state=NORMAL)
        result11 = "".join(list11[0:int(password_variable.get())])
        output_text.insert('1.0', result11)
        output_text.config(state=DISABLED)


def upper_and_lower_and_punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 85:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 85")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u6 = string.ascii_uppercase
        l6 = string.ascii_lowercase
        p5 = string.punctuation
        list12 = []
        list12.extend(list(u6))
        list12.extend(list(l6))
        list12.extend(list(p5))
        random.shuffle(list12)
        output_text.config(state=NORMAL)
        result12 = "".join(list12[0:int(password_variable.get())])
        output_text.insert('1.0', result12)
        output_text.config(state=DISABLED)


def upper_and_lower_and_digit_and_punctuation():
    if password_variable.get() == 0 or password_variable.get() >= 95:
        messagebox.showwarning("Warning!", "Password Length should be 1 and less then 95")
        generate_btn.config(state=NORMAL)
    else:
        password_length_entry.config(state=DISABLED)
        option.config(state=DISABLED)
        u7 = string.ascii_uppercase
        l7 = string.ascii_lowercase
        d6 = string.digits
        p6 = string.punctuation
        list13 = []
        list13.extend(list(u7))
        list13.extend(list(l7))
        list13.extend(list(p6))
        list13.extend(list(d6))
        random.shuffle(list13)
        output_text.config(state=NORMAL)
        result13 = "".join(list13[0:int(password_variable.get())])
        output_text.insert('1.0', result13)
        output_text.config(state=DISABLED)


#===============Clear Programme===============
def clear_programme():
    option.set("Options")
    password_variable.set("")
    output_text.config(state=NORMAL)
    output_text.delete('1.0', END)
    output_text.config(state=DISABLED)
    generate_btn.config(state=NORMAL)
    password_length_entry.config(state=DISABLED)
    option.config(state=NORMAL)
    copy_btn.config(state=DISABLED)
    clear_btn.config(state=DISABLED)


#=================Copy Programme===========
def copy_programme():
    output_text.config(state=NORMAL)
    pyperclip.copy(output_text.get('1.0', END))
    messagebox.showinfo("Info!", "Copied!")
    output_text.config(state=DISABLED)
    copy_btn.config(state=DISABLED)


#=================Generate Programme=======
def generate_programme():
    selected_option = option.get()
    for_checking_int_or_str = password_length_entry.get()
    if selected_option == "Options":
        messagebox.showwarning("Warning!", "Select Option!")
    elif password_variable.get() == "":
        messagebox.showwarning("Warning!", "Enter Password Length!")
    else:
        if for_checking_int_or_str.isdigit():
            generate_btn.config(state=DISABLED)
            copy_btn.config(state=NORMAL)
            clear_btn.config(state=NORMAL)
            if selected_option == "Only Upper Case":
                upper()
            elif selected_option == "Only Lower Case":
                lower()
            elif selected_option == "Only Digits":
                digit()
            elif selected_option == "Only Puntuation":
                punctuation()
            elif selected_option == "Upper Case + Lower Case":
                upper_and_lower()
            elif selected_option == "Upper Case + Digits":
                upper_and_digit()
            elif selected_option == "Upper Case + Puntuation":
                upper_and_punctuation()
            elif selected_option == "Lower Case + Digits":
                lower_and_digit()
            elif selected_option == "Lower Case + Puntuation":
                lower_and_punctuation()
            elif selected_option == "Digits + Puntuation":
                digit_and_punctuation()
            elif selected_option == "Upper Case + Lower Case + Digits":
                upper_and_lower_and_digit()
            elif selected_option == "Upper Case + Lower Case + Puntuation":
                upper_and_lower_and_punctuation()
            elif selected_option == "Upper Case + Lower Case + Digits + Puntuation":
                upper_and_lower_and_digit_and_punctuation()
        else:
            messagebox.showerror("Error!", "Length should be interger.")
    


#==============Password Generator Text=================
intro = Label(root,text="Password Generator", font=("times new roman", 30), bg='#053246', fg='White')
intro.place(x=0, y=0, relwidth=1)




#==============Select Option Text=====================
option_label = Label(root, text="Select Option: ", fg="#262626", font=("Times new roman", 12, "bold"))
option_label.place(x=20, y=70)


#==============Option Menu============================
option = ttk.Combobox(root, width=45, values=("Only Upper Case", "Only Lower Case", "Only Digits", "Only Puntuation", "Upper Case + Lower Case", "Upper Case + Digits", "Upper Case + Puntuation", "Lower Case + Digits", "Lower Case + Puntuation", "Digits + Puntuation", "Upper Case + Lower Case + Digits", "Upper Case + Lower Case + Puntuation", "Upper Case + Lower Case + Digits + Puntuation"), state="readonly")
option.set("Options")
option.place(x=170, y=70)



#=================Set Password Length Text=============
password_length_label = Label(root, text="Set Password Length: ", fg="#262626", font=("Times new roman", 10, "bold"))
password_length_label.place(x=20, y=130)


#================Variable For Password Storing
password_variable = IntVar()


#================Password Entry================
password_length_entry = Entry(root, bd=2, relief=RIDGE, textvariable=password_variable)
password_length_entry.place(x=250, y=130)



#===============Setting State of Password Entry Disabled==========
password_length_entry.delete(0, END)


#=============Frame For Generated Password============
output = LabelFrame(root, text="Generated Password", bd=7, relief=GROOVE, font=("Segoe Script", 12, "bold"), fg="purple")
output.place(x=110, y=200, height=75, width=420)


#==============Scrollbar For Frame================
scroolbar_for_output = Scrollbar(output, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_output.pack(side=BOTTOM, fill=X)


#==============Text Area In Frame=================
output_text = Text(output, wrap=NONE, xscrollcommand=scroolbar_for_output.set)
output_text.pack(fill=BOTH, expand=1)



#===============Configuring Scrollbar==============
scroolbar_for_output.config(command=output_text.xview)


#===============Setting State of Frame Disabled==========
output_text.config(state=DISABLED)


#===============Generate Button==============
generate_btn = Button(root, text="Generate", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",activebackground="white", command=generate_programme)
generate_btn.place(x=110, y=300)


#===============Copy Button==============
copy_btn = Button(root, text="Copy", font=("times new roman", 15, "bold"), bg="grey", fg="white", cursor="hand2",activebackground="white", command=copy_programme)
copy_btn.place(x=290, y=300)
copy_btn.config(state=DISABLED)


#===============Clear Button==============
clear_btn = Button(root, text="Clear *", font=("times new roman", 15, "bold"), bg="#A16DF0", fg="white", cursor="hand2",activebackground="white", command=clear_programme)
clear_btn.place(x=445, y=300)
clear_btn.config(state=DISABLED)


root.mainloop()