from tkinter import*
#from button_functions import*
#from button_functions_mha import*

from class_button_function_mhacommand import Person


root = Tk()


#-----------------------------------------------------------------------------------------------------------
# gui interface

root.title("Hearability GUI")


# define the frames to delimatate the interface into areas--------------------------------------------------

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.grid(row = 0, column = 4)

f2 = Frame(root, width=1200, height=1200, bg="powder blue", relief=SUNKEN)
f2.grid(row = 1, column = 4)

UnTops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
UnTops.grid(row = 2, column = 4)

#title---------------------------------------------------------------------------------------------------------------

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Hearability control command", fg="Steel blue", bd=10, anchor="w")
lblInfo.grid(row = 0, column = 0)


#input field -------------------------------------------------------------------------------------------------------------------------------------------------

input_text = IntVar()
txtDisplay = Entry(f2, font=("Arial", 20, "bold"), bd=20, insertwidth = 4, bg='powder blue', justify  ='right')
txtDisplay.grid(row = 1, column = 1)
input_frame = Frame(txtDisplay, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.grid(row = 0, column = 0)
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 5, bg = "#eee", bd = 0, justify = RIGHT).pack()


var_fqcyshift = IntVar()
txtDisplay_fqcyshift = Entry(f2, font=("Arial", 20, "bold"), bd=20, insertwidth = 4, bg='powder blue', justify  ='right')
txtDisplay_fqcyshift.grid(row = 5, column = 1)
input_frame_fqcyshift = Frame(txtDisplay_fqcyshift, width = 50, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame_fqcyshift.grid(row = 5, column = 1)
input_field_fqcyshift = Entry(input_frame_fqcyshift, font = ('arial', 18, 'bold'), textvariable = var_fqcyshift, width = 5, bg = "#eee", bd = 0, justify = RIGHT).pack()




#gain value display -------------------------------------------------------------------------------------------------------------------------------------------------
person = Person()

def display_gain_gain():
    global person
    gainc3 = person.gainbb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=1, column = 6)

def display_CoherenceFilter_gain():
    global person
    gainc3 = person.gainCoherencebb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2,height=1).grid(row=2, column=6)

def display_SCNoiseReduction_gain():
    global person
    gainc3 = person.gainSCbb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=3, column = 6)

def display_fqcyshift_gain():
    global person
    gainc3 = person.gainfshiftbb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=5, column = 6)

def display_LowPassFilter_gain():
    global person
    gainc3 = person.gainLPfilterbb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=6, column = 6)

def display_HighPassFilter_gain():
    global person
    gainc3 = person.gainHPfilterbb
    gainStr = str(gainc3)
    Label(f2, text= gainStr, fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=7, column = 6)

label_cfield_plugin = Label(f2, text="option", fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=40, height=2).grid(row=0, column = 0)
label_cfield_value = Label(f2, text="value", fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=20, height=2).grid(row=0, column = 1)
label_cfield_update_value = Label(f2, text="Update value", fg="white smoke",bg="Steel blue", font="Helvetica 16 bold italic", width=30, height=2).grid(row=0, column = 2)
label_cfield_VolumeUp = Label(f2, text="Vol Up", fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=10, height=2).grid(row=0, column = 3)
label_cfield_VolumeDown = Label(f2, text="Vol Down", fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=10, height=2).grid(row=0, column = 4)
label_cfield_Volume = Label(f2, text="Volume",fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=10, height=2).grid(row=0, column = 6)
label_cfield_stamp = Label(f2, fg="white smoke", bg="Steel blue", font="Helvetica 16 bold italic", width=5, height=2).grid(row=0, column = 5)

label_stamp = Label(f2, fg="powder blue", bg="powder blue", font="Helvetica 16 bold italic", width=4, height=4).grid(row=1, column = 5)

label_Gain_gain = Label(f2, text="0", fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=1, column = 6)
label_CoherenceFilter_gain = Label(f2, text="0", fg="red", bg="black",font=("Helvetica", 40), width=2, height=1).grid(row=2, column = 6)
label_SCNoiseReduction_gain = Label(f2, text="0", fg="red", bg="black",font=("Helvetica", 40), width=2, height=1).grid(row=3, column = 6)
label_FqcyShift_gain = Label(f2, text="0", fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=5, column = 6)
label_LowPassFilter_gain = Label(f2, text="0", fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=6, column = 6)
label_HighPassFilter_gain = Label(f2, text="0", fg="red", bg="black", font=("Helvetica", 40), width=2, height=1).grid(row=7, column = 6)







#buttons -------------------------------------------------------------------------------------------------------------------------------------------------

text_button_size = 15

btn1_On = Button(UnTops, padx=8, pady=8, bd=18, fg="black", font=('arial', text_button_size, 'bold'), text="On", bg = "powder blue",
              command=lambda: [person.BtnClick_On(), display_gain_gain(), display_SCNoiseReduction_gain(), display_fqcyshift_gain(), display_LowPassFilter_gain(),
                              display_HighPassFilter_gain(), display_CoherenceFilter_gain()]).grid(row = 0, column=0)

btn2_Off = Button(UnTops, padx = 8, pady = 8, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="Off", bg = "powder blue",
              command=lambda:[person.BtnClick_Off(), display_gain_gain(), display_SCNoiseReduction_gain(), display_fqcyshift_gain(), display_LowPassFilter_gain(),
                              display_HighPassFilter_gain(), display_CoherenceFilter_gain()]).grid(row = 0, column=1)

btn3_GainOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="               Gain On             ", bg = "powder blue",
              command=lambda: person.BtnClick_GainOn()).grid(row = 1, column=0)

btn3_0_UpdateGain = Button(f2, padx = 32, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="     update gain     ", bg = "powder blue",
              command=lambda:[person.BtnClick_UpdateGain(input_text), display_gain_gain()]).grid(row =1, column=2)

btn3_1_GainUp = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda: [person.BtnClick_GainUp(), display_gain_gain()]).grid(row = 1, column=3)

btn3_2_GainDown = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda: [person.BtnClick_GainDown(), display_gain_gain()]).grid(row = 1, column=4)

btn6_CoherenceFilOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="     Coherence filter On     ", bg = "powder blue",
              command=lambda: person.BtnClick_CoherenceOn()).grid(row = 2, column=0)

btn6_0_CoherenceFilOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda: [person.BtnClick_CoherenceGainUp(), display_CoherenceFilter_gain() ]).grid(row = 2, column=3)

btn6_1_CoherenceFilOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda: [person.BtnClick_CoherenceGainDown(), display_CoherenceFilter_gain() ]).grid(row = 2, column=4)

btn7_SCNoiseRedOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text=" SC Noise Reduction On  ", bg = "powder blue",
              command=lambda:[person.BtnClick_SCNoiseReductionOn(), display_SCNoiseReduction_gain()]).grid(row = 3, column=0)

btn7_1_SCNoiseRed_GainUp = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda:[person.BtnClick_SCNoiseReductionGainUp(), display_SCNoiseReduction_gain()]).grid(row = 3, column=3)

btn7_2_SCNoiseRed_GainDown = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda:[person.BtnClick_SCNoiseReductionGainDown(), display_SCNoiseReduction_gain()]).grid(row = 3, column=4)

btn8_DCOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="Dynamic compression On", bg = "powder blue",
              command=lambda:person.BtnClick_DCOn()).grid(row = 4, column=0)

btn10_FqcySchiftOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="       Fqcy shifting On       ", bg = "powder blue",
              command=lambda:[person.BtnClick_FqcyShifting_On(), display_fqcyshift_gain()]).grid(row = 5, column=0)

btn10_0_UpdateFqcySchift = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text=" Update Fqcy shifting ", bg = "powder blue",
              command=lambda:person.BtnClick_FqcyShifting_Update(var_fqcyshift)).grid(row = 5, column=2)

btn10_1_FqcySchiftGainUp = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda:[person.BtnClick_FqcyShifting_GainUp(), display_fqcyshift_gain()]).grid(row = 5, column=3)

btn10_2_FqcySchiftGainDown = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda:[person.BtnClick_FqcyShifting_GainDown(), display_fqcyshift_gain()]).grid(row = 5, column=4)

btn12_LowPFilterOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="      Low pass filter On      ", bg = "powder blue",
              command=lambda:[person.BtnClick_LowPassFilterOn(), display_LowPassFilter_gain()]).grid(row = 6, column=0)

btn12_1_LowPFilterGainUp = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda:[person.BtnClick_LowPassFilterGainUp(), display_LowPassFilter_gain()]).grid(row = 6, column=3)

btn12_2_LowPFilterGainDown = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda:[person.BtnClick_LowPassFilterGainDown(), display_LowPassFilter_gain()]).grid(row = 6, column=4)

btn13_HighPFilterOn = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial',text_button_size, 'bold'), text="      High pass filter On      ", bg = "powder blue",
              command=lambda:[person.BtnClick_HighPassFilterOn(), display_HighPassFilter_gain()]).grid(row = 7, column=0)

btn13_1_HighPFilterGainUp = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="+", bg = "powder blue",
              command=lambda:[person.BtnClick_HighPassFilterGainUp(), display_HighPassFilter_gain()]).grid(row = 7, column=3)

btn13_2_HighPFilterGainDown = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', text_button_size, 'bold'), text="-", bg = "powder blue",
              command=lambda:[person.BtnClick_HighPassFilterGainDown(), display_HighPassFilter_gain()]).grid(row = 7, column=4)

#fefefefe

#btn13_EntryFqcyShift= Button(f2, padx = 32, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="update fqcyshift", bg = "powder blue",
 #             command=lambda:btnClick_UpdateGain(input_text)).grid(row = 5, column=6)
#----------------------------------------------------------------------------------------------------------------------------
#end gui interface

root.mainloop()





