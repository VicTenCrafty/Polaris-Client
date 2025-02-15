import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import os


def create_rounded_image(image_path, size, radius):
    image = Image.open(image_path).resize(size)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(image, mask=mask)
    return output


def create_rounded_button(size, color, radius):
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=color)
    return ImageTk.PhotoImage(image)


class PolarisGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Polaris Client")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)

        # Canvas setup
        self.canvas = tk.Canvas(
            self.root,
            width=1280,
            height=720,
            bd=0,
            highlightthickness=0
        )
        self.canvas.place(x=0, y=0)

        # Background setup
        bg_path = os.path.join("resources", "images", "background.png")
        self.bg_image = Image.open(bg_path).resize((1280, 720))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        # Logo setup
        logo_path = os.path.join("resources", "images", "logo.png")
        rounded_logo = create_rounded_image(logo_path, (640, 256), 30)
        self.logo_image = ImageTk.PhotoImage(rounded_logo)
        self.canvas.create_image(640, 120, anchor="center", image=self.logo_image)

        # Create button images
        self.button_normal = create_rounded_button((200, 50), "#2FA572", 30)
        self.button_hover = create_rounded_button((200, 50), "#248C61", 30)

        # Create Play button on canvas
        self.play_button = self.canvas.create_image(640, 360, image=self.button_normal)
        self.play_text = self.canvas.create_text(640, 360, text="Play!", font=("Arial", 24, "bold"), fill="white")

        # Bind hover events for play button
        self.canvas.tag_bind(self.play_button, "<Enter>", self.on_play_hover)
        self.canvas.tag_bind(self.play_button, "<Leave>", self.on_play_leave)
        self.canvas.tag_bind(self.play_text, "<Enter>", self.on_play_hover)
        self.canvas.tag_bind(self.play_text, "<Leave>", self.on_play_leave)
        self.canvas.tag_bind(self.play_button, "<Button-1>", self.on_play_click)
        self.canvas.tag_bind(self.play_text, "<Button-1>", self.on_play_click)

        # Version selector using CTkOptionMenu
        self.version_selector = ctk.CTkOptionMenu(
            self.root,
            values=["Fabric 1.20.1", "Fabric 1.21"],
            width=200,
            height=30,
            fg_color="#2FA572",
            button_color="#248C61",
            button_hover_color="#1B6B49",
            dropdown_fg_color="#2FA572",
            dropdown_hover_color="#248C61",
            corner_radius=30,
            bg_color="transparent",
            text_color="white",
            font=("Arial", 12)
        )
        self.version_selector.place(relx=0.5, rely=0.6, anchor="center")
        self.version_selector.set("Select Version")

    def on_play_hover(self, event):
        self.canvas.itemconfig(self.play_button, image=self.button_hover)

    def on_play_leave(self, event):
        self.canvas.itemconfig(self.play_button, image=self.button_normal)

    def on_play_click(self, event):
        print("Play clicked!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PolarisGUI()
    app.run()
