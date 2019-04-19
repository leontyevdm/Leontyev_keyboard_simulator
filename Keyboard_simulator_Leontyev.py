from tkinter import *
import time


level = input("Введите желаемый уровень сложности - целое число от 1 до 5: ")
file_name = "level" + level + ".txt"
task_file = open(file_name, "r", encoding='utf-8')
task_text = task_file.read()
task_file.close()

root = Tk()
root.geometry("1720x880")
start_button = Button(root, text="Start")
start_button.pack()


def keyboard_simulator():
    start_button.destroy()
    root.title("Клавиатурный тренажер")
    task_text_label = Label(bg="white", fg="black",
                            font=18, width=200)
    task_text_label["text"] = task_text
    task_text_label.place(relx = 0, rely = 0)
    task_length = len(task_text)
    printed_text = Label(bg="white", fg="green",
                         font=18, width=200, height=10)
    user_length = 0
    mistakes = 0
    required_letter = task_text[0]
    printed = ""
    printed_text['text'] = printed
    printed_text.place(relx = 0, rely = 0.2)
    root.update()
    start_time = time.perf_counter()
    required_letter = task_text[user_length]
    stat_label = Label(bg="white", fg="red", font=18, width=200, height = 10)
    stat_label.place(relx = 0, rely = 0.8)
    root.update()
    ended = 0
    flag = 0
    def getchar(event):
        nonlocal printed_text, stat_label, user_length, ended
        nonlocal required_letter, mistakes, start_time, flag
        time_ = int((time.perf_counter() - start_time)*100)/100
        if event.char == required_letter:
            printed_text["text"] += event.char
            if user_length < task_length - 1:
                user_length += 1
                required_letter = task_text[user_length]
            else:
                task_text_label.destroy()
                printed_text.destroy()
                statistics_string = ("Level: " + level + " Ошибок: "
                                     + str(mistakes) + " Время: " + str(time_)
                                     + " секунд." + " Скорость: " 
                                     + str(int(task_length*100/time_)/100)
                                     + " символов в секунду" + "\n")
                statistics = open("statistics.txt", "a")
                statistics.write(statistics_string)
                statistics.close()
                ended = 1
        elif (ended == 0):
            try:
                if ord(event.char) >= 32 :
                    mistakes += 1
            except TypeError:
                pass
        if (flag == 0):
            stat_label['text'] = ("Ошибок: "
                + str(mistakes) + " Время: " + str(time_) + " секунд"
                + " Скорость: " + str(int(user_length*100/time_)/100)
                + " символов в секунду")
            if (ended == 1):
                flag = 1;
    root.bind('<Key>', getchar)


start_button.config(command=keyboard_simulator)
root.mainloop()
