from tkinter import *

#Pencere Oluşturma
window = Tk()
window.title("BMI Calculator")
window.config(background="light cyan" , padx=40 , pady=40)

#Fonksiyon

def bmiResult():
    weight = weightEntry.get()
    height = heightEntry.get()
    result = ""
    if weight == "" or height == "":
        result = ("Please enter values")
    

    try:
            bmi = round(float(weight)/ (float(height) / 100) ** 2)
           
            if bmi < 18.5:
                result = (f"Your BMI is {bmi}, you are underweight")
            elif bmi < 25:
                result =(f"Your BMI is {bmi}, you have a normal weight")
            elif bmi < 30:    
                result =(f"Your BMI is {bmi}, you are slightly overweight")
            elif bmi < 35:
                result =(f"Your BMI is {bmi}, you are obese")
            elif bmi > 35:
                result = (f"Your BMI is {bmi}, you are clinically obese")

            bmiLabel.config(text=result)
    
    except:
        bmiLabel.config(text="Please enter valid numbers for weight and height")
    
            
#Label

weightLabel = Label(text="Please enter your weight as kg")
weightLabel.config(background="light cyan" , foreground="black")
weightLabel.pack()
weightEntry = Entry()
weightEntry.config(background="white" , foreground="black")
weightEntry.pack()

heightLabel = Label(text="Please enter your height as cm")
heightLabel.config(background="light cyan" , foreground="black")
heightLabel.pack()
heightEntry = Entry()
heightEntry.config(background="white" , foreground="black")
heightEntry.pack()

theButton = Button(text="Calculate", command=bmiResult , width=10)
theButton.pack()

bmiLabel = Label()
bmiLabel.config(background="light cyan" , foreground="black")
bmiLabel.pack()



window.mainloop()






















































