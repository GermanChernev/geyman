import threading
from socket import *
from customtkinter import *
from PIL import Image
#hi

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x700')
        img_file1 = Image.open("istockphoto-1434782845-612x612.jpg")
        img_file = Image.open("1640829007_5-abrakadabra-fun-p-zadnii-fon-dlya-telegramma-7.jpg")
        self.img_object = CTkImage(light_image=img_file, dark_image=img_file, size=(2000, 700))
        self.bg_label = CTkLabel(self, image=self.img_object, text="")
        self.bg_label.place(x=0, y=0)
        self.title("moggika")
        self.menu_frame = CTkFrame(self, width=30, height=200,fg_color="#1f1936")
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        self.is_show_menu = False
        self.speed_animate_menu = -5
        self.btn = CTkButton(self, text='▶️', command=self.toggle_show_menu, width=30,fg_color="#4B0082",text_color="white")
        self.btn.place(x=0, y=0)
        self.btn1 = CTkButton(self, text='⏩', command=self.toggle_show_menu1, width=30,fg_color="#4B0082",text_color="white")
        self.btn1.place(x=0, y=35)
        # main
        self.chat_field = CTkTextbox(self, font=('Comic Sans MS', 14, 'bold'), state='disable',fg_color="#4B0082",text_color="white")
        self.chat_field.place(x=0, y=50)
        self.message_entry = CTkEntry(self, font=('Comic Sans MS', 14, 'bold'), placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)
        self.send_button = CTkButton(self, text='>', width=50, height=40, command=self.send_message,fg_color="#4B0082",text_color="white")
        self.send_button.place(x=0, y=0)

        self.username = 'gg'
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('localhost', 1111))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
            self.sock.send(hello.encode('utf-8'))
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"Не вдалося підключитися до сервера: {e}",)

        self.adaptive_ui()

    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text='▶️',fg_color="#4B0082")
            self.show_menu()
            self.entry.pack_forget()
            self.label.pack_forget()
            self.chat.pack_forget()

        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text='◀️',fg_color="#4B0082")
            self.show_menu()
            # setting menu widgets
            self.label = CTkLabel(self.menu_frame, font=('Comic Sans MS', 14, 'bold'), text='Імʼя',text_color="white")
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame,font=('Comic Sans MS', 14, 'bold'),fg_color="#4B0082",text_color="white")
            self.entry.pack()
    def toggle_show_menu1(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text="⏩",fg_color="#4B0082",text_color="white")
            self.show_menu()
            self.entry.pack_forget()
            self.label.pack_forget()
            self.chat.pack_forget()




        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text="⏪",fg_color="#4B0082",text_color="white")
            self.show_menu()
            # setting menu widgets
            self.chat = CTkTextbox(self.menu_frame,height=300,width=300)
            text_emoji = "❤❌💬🚗🛹🚚🦽🚔🚎🚐🚖🚘🚜🚄🚋✈💺🚀🪒🌤🌝🌫🌪🌩🌨🌧🌦🌥☁⛅⛈🧯🧺🧹🧷🌑🌞⛵🚤⛴🛳🚢🚦🌍🪐🌌🌎🏴‍☠️🏰🏩🏡🗽🌇🌆♨🍸🍉🍑🍌🍍🍇🥭🍓🍅🍆🌽🍐🍏🌶🧽🛰❄⛄🍕🍔🍟🌭🍿🍞🥐🥪🥟🥠🍣🥫🥣🍤🍢🍩🍧🍨🎂🍻🥀☘🌱🌲🌾🌿🍁🍂🍃🍄🥑🥒🥬🥦🥔🧄🌹🏵🌸💐🥜🌰🥕🧅🌺🌻🌼🌷😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗🤨🤔🤩🤗🙂😚☺😙😐🤐😑😯😶😪🙄😫😏🥱😣😴😥😌😮😛🙃😕🤒😷🤬😡🤧🤭🧐🥳🤓🥺🤠🤡🤥🤫👿"
            self.chat.insert(END, '' + text_emoji + '\n')
            self.chat.pack()






    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
        if not self.menu_frame.winfo_width() >= 400 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width() >= 40 and not self.is_show_menu:
            self.after(10, self.show_menu)
            if self.label and self.entry:
                self.label.destroy()
                self.entry.destroy()

    def adaptive_ui(self):
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(width=self.winfo_width() - self.menu_frame.winfo_width(),
                                  height=self.winfo_height() - 40)
        self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - self.send_button.winfo_width())

        self.after(1, self.adaptive_ui)

    def add_message(self, text):
        self.chat_field.configure(state='normal')
        self.chat_field.insert(END, '' + text + '\n')
        self.chat_field.configure(state='disable')

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.add_message(f"{self.username}: {message}")
            data = f"TEXT@{self.username}@{message}\n"
            try:
                self.sock.sendall(data.encode())
            except:
                pass
        self.message_entry.delete(0, END)

    def recv_message(self):
        buffer = ""
        while True:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buffer += chunk.decode()

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.handle_line(line.strip())
            except:
                break
        self.sock.close()

    def handle_line(self, line):
        if not line:
            return
        parts = line.split("@", 3)
        msg_type = parts[0]

        if msg_type == "TEXT":
            if len(parts) >= 3:
                author = parts[1]
                message = parts[2]
                self.add_message(f"{author}: {message}")
        elif msg_type == "IMAGE":
            if len(parts) >= 4:
                author = parts[1]
                filename = parts[2]

                self.add_message(f"{author} надіслав(ла) зображення: {filename}")

        else:
            self.add_message(line)


win = MainWindow()
win.mainloop()
