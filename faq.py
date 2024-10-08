import customtkinter as ctk
import sql_commands
def faq():
    root = ctk.CTk() 
    root.title("FAQ")
    root.state('normal')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.configure(fg_color='black')

    qa = sql_commands.faq_qa()

    main_label = ctk.CTkLabel(root, text="Frequent Questions and Answers", text_color='lightblue', font=("Algerian", 25, "bold"))
    main_label.pack(pady=25)

    for i, (question, answer) in enumerate(qa):
        question_label = ctk.CTkLabel(root, text=f"Question {i + 1}) {question}", font=("Comic Sans MS", 12, "bold"), text_color='white')
        question_label.pack(anchor="w", pady=(5, 0))

        answer_label = ctk.CTkLabel(root, text="Answer: " + answer, font=("Comic Sans MS", 12), text_color='white')
        answer_label.pack(anchor="w", pady=(0, 10))

    ctk.CTkButton(root,text="Back",command=root.destroy).place(x=10,y=10)
    
    root.mainloop()
