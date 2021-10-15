#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Project 1
#10/13/21
#Steven Garcia
#Dennis Dinh

from tkinter import * 
import tkinter as tk
import math
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk  

#creates dimensions class for either circular or rectangular cross section        
def dimensions():  
    #Adds a button to call on Calculations command
    B2 = tk.Button(text="Results", command=calculations).grid(row=8, column=4)
    #Removes Used button
    B1.destroy()
    #If Circular Beam shape is selected
    if Button.get()==1:
        #hides rectangular button once one is selected
        r2.destroy()  
        #hides Rectagular picture
        label2.destroy()
        #distinguishes what value to input regarding Circular Beam
        tk.Label(root,text="""What is the radius in mm?""").grid(row = 4, column = 0) 
        tk.Label(root,text="""What is the length of the beam in mm?""").grid(row = 5, column = 0)
        tk.Label(root,text="""What is the transverse force in N?""").grid(row = 6, column = 0)
        tk.Label(root,text="""What is the axial force in N?""").grid(row = 7, column = 0)
        #user inputted value for Circular Beam
        tk.Entry(textvariable = l).grid(row=4, column=1)           
        tk.Entry(textvariable = r).grid(row=5, column=1)
        tk.Entry(textvariable = TransverseForce).grid(row=6,column=1)
        tk.Entry(textvariable = AxialForce).grid(row=7,column=1)
    #If Rectangular Beam shape is selected     
    elif Button.get()==2:
        #hides rectangular button once one is selected
        r1.destroy()
        #hides Rectagular picture
        label1.destroy()
        #distinguishes what value to input regarding Rectangular Beam
        tk.Label(root,text="""What is the base of the cross section in mm?""").grid(row = 4, column = 0)
        tk.Label(root,text="""What is the height of the cross section in mm?""").grid(row = 5, column = 0)
        tk.Label(root,text="""What is the length of the beam in mm?""").grid(row = 6, column = 0)
        tk.Label(root,text="""What is the transverse force in N?""").grid(row = 7, column = 0)
        tk.Label(root,text="""What is the axial force in N?""").grid(row = 8, column = 0)
        #user inputted value for Rectangular Beam
        tk.Entry(textvariable = b).grid(row=4, column=1)
        tk.Entry(textvariable = h).grid(row=5, column=1)
        tk.Entry(textvariable = l).grid(row=6, column=1)
        tk.Entry(textvariable = TransverseForce).grid(row=7, column=1)
        tk.Entry(textvariable = AxialForce).grid(row=8,column=1)

#creates the calculations class for the different stresses in certain cross section
def calculations(): 
    #If Circular Beam shape is selected
    if Button.get() == 1:
        M = (int(TransverseForce.get()))*(int(l.get()))  #int.get allows the string to be converted to an integer
        y=(int(r.get()))
        I=((math.pi)/(4))*((int(r.get()))**4)
        A=(math.pi)*(int(r.get()))**2
        bending=(M*y)/(I)
        axial=(int(AxialForce.get()))/A
        res = bending + axial
    #If Rectangular Beam shape is selected    
    elif Button.get() == 2:
        M = (int(TransverseForce.get()))*(int(l.get()))  
        y=(int(h.get()))/ (2)  
        I=((int(b.get()))*((int(h.get()))**3))/(12)
        A=(int(b.get()))*(int(h.get()))
        bending=(M*y)/(I)
        axial=(int(AxialForce.get()))/(A)
        res = bending + axial
    else:
        res ="No Choice selected"
    #Pop-up window with Stress results
    messagebox.showinfo("Found Stresses",  "\n".join(["Bending:"+str(bending) + "MPa" ,"Axial:"+str(axial) + "MPa","Resultant:" +str(res) + "MPa"]))
    
#creates root window    
root = tk.Tk()  
#assigns variables as strings
r =tk.StringVar()  
b =tk.StringVar()
h =tk.StringVar()
l =tk.StringVar()
AxialForce =tk.StringVar()
TransverseForce =tk.StringVar()
root.title("Stress Calculator")   

Button = tk.IntVar()
myText=tk.StringVar()

#Applied image of Circular Beam
image1 = PhotoImage(file = "circular.png")  
#Resized imagae to fit in window
resize_image = image1.subsample(6, 6)
label1 = Label(image=resize_image)
label1.grid(row=0, column = 0)


#Applied image of Circular Beam
image2 = PhotoImage(file = "rectangle.png")
#Resized imagae to fit in window
resize_image1 = image2.subsample(2, 2)
label2 = Label(image=resize_image1)
label2.grid(row=0, column = 7)

#Radio Button Selection for Circular
r1 = tk.Radiobutton(text="Circular",
    variable=Button, value=1)
r1.grid(row=2,column=0)

#Radio Button Selection for Rectangular
r2 = tk.Radiobutton(text="Rectangular",
    variable=Button, value=2)
r2.grid(row=2,column=7) 

#Continue button to call on dimension function
B1 = tk.Button(text="Continue", command=dimensions)
B1.grid(row=1, column=4)
result=tk.Label(text="(result)", textvariable=myText).grid(row=5,column=0)

root.mainloop()


# In[ ]:




