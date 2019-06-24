import tkinter
import tkinter.messagebox


def main():
    flag = True


    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ("red", "111") if flag else ("blue", "000")
        label.config(text=msg, fg=color)


    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("meow", "quit??"):
            top.quit()


    top = tkinter.Tk()
    top.geometry("640x480")
    top.title("nmb")
    label = tkinter.Label(top, text="tkinter", font="Arial -32", fg="red")
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text="modify", command=change_label_text)
    button1.pack(side="left")
    button2 = tkinter.Button(panel, text="quit", command=confirm_to_quit)
    button2.pack(side="right")
    panel.pack(side="bottom")
    tkinter.mainloop()

main()
