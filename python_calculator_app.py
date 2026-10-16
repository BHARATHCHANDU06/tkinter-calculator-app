import tkinter as tk
window=tk.Tk()
window.title("Calculator")
window.geometry("600x600")
window.resizable(False,False)

expression=""
#-------------FUNCTIONS--------------
def button_click(value):
    global expression
    expression+=str(value)
    display.delete(0,tk.END)
    display.insert(tk.END,expression)
def clear():
    global expression
    expression=""
    display.delete(0,tk.END)
def backspace():
    global expression
    expression=expression[:-1]
    display.delete(0,tk.END)
    display.insert(tk.END,expression)
def calculate():
    global expression
    try:
        result=eval(expression)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
        expression=str(result)
    except ZeroDivisionError:
        display.delete(0,tk.END)
        display.insert(tk.END,"Cannot divide by 0")
        expression=""
    except:
        display.delete(0,tk.END)
        display.insert(tk.END,"Error")
        expression=""
#---------------DISPLAY---------------
display=tk.Entry(
    window,
    font=("Arial",25),
    justify="right",
    bd=10
)
display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipady=10
    )
#----------BUTTONS--------------
clear_button=tk.Button (
    window,text="c",
    font=("Arial",18),
    width=5,
    height=2,
    command=clear)
clear_button.grid(row=1,column=0,padx=5,pady=5)

back_button=tk.Button(
    window,
    text="⌫",
    font=("Arial",18),
    width=5,
    height=2,
    command=backspace)
back_button.grid(row=1,column=1,padx=5,pady=5)

divide_button=tk.Button(
    window,
    text="/",
    font=("Arial",18),
    width=5,
    height=2,
    command=lambda:button_click("/"))
divide_button.grid(row=1,column=2,padx=5,pady=5)

multiply_button=tk.Button(
    window,
    text="x",
    font=("Arial",18),
    width=5,
    height=2,
    command=lambda:button_click("*"))
multiply_button.grid(row=1,column=3,padx=5,pady=5)

button7=tk.Button(window,text="7",font=("Arial",18),width=5,height=2,command=lambda:button_click(7))
button7.grid(row=2,column=0,padx=5,pady=5)

button8=tk.Button(window,text="8",font=("Arial",18),width=5,height=2,command=lambda:button_click(8))
button8.grid(row=2,column=1,padx=5,pady=5)

button9=tk.Button(window,text="9",font=("Arial",18),width=5,height=2,command=lambda:button_click(9))
button9.grid(row=2,column=2,padx=5,pady=5)

minus_button=tk.Button(window,text="-",font=("Arial", 18),width=5,height=2,command=lambda: button_click("-"))
minus_button.grid(row=2,column=3,padx=5,pady=5)

button4=tk.Button(window,text="4",font=("Arial",18),width=5,height=2,command=lambda:button_click(4))
button4.grid(row=3,column=0,padx=5,pady=5)

button5=tk.Button(window,text="5",font=("Arial",18),width=5,height=2,command=lambda:button_click(5))
button5.grid(row=3,column=1,padx=5,pady=5)

button6=tk.Button(window,text="6",font=("Arial", 18),width=5,height=2,command=lambda:button_click(6))
button6.grid(row=3,column=2,padx=5,pady=5)

plus_button = tk.Button(window,text="+",font=("Arial", 18),width=5,height=2,command=lambda: button_click("+"))
plus_button.grid(row=3, column=3, padx=5, pady=5)

button1=tk.Button(window,text="1",font=("Arial", 18),width=5,height=2,command=lambda:button_click(1))
button1.grid(row=4,column=0,padx=5,pady=5)

button2=tk.Button(window,text="2",font=("Arial", 18),width=5,height=2,command=lambda:button_click(2))
button2.grid(row=4,column=1,padx=5,pady=5)

button3=tk.Button(window,text="3",font=("Arial", 18),width=5,height=2,command=lambda:button_click(3))
button3.grid(row=4,column=2,padx=5,pady=5)

percentage_button = tk.Button(window,text="%",font=("Arial", 18),width=5,height=2,command=lambda:button_click("%"))
percentage_button.grid(row=4, column=3, padx=5, pady=5)

button00=tk.Button(window,text="00",font=("Arial",18),width=5,height=2,command=lambda:button_click(00))
button00.grid(row=5,column=0, padx=5, pady=5)

decimal_button = tk.Button(window,text=".",font=("Arial", 18),width=5,height=2,command=lambda: button_click("."))
decimal_button.grid(row=5, column=1, padx=5, pady=5)

button0=tk.Button(window,text="0",font=("Arial",18),width=5,height=2,command=lambda:button_click(0))
button0.grid(row=5,column=2, padx=5, pady=5)

equal_button = tk.Button(window,text="=",font=("Arial", 18),width=5,height=2,command=calculate)
equal_button.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()