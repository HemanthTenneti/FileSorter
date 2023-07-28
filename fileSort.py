import shutil
import os
from time import sleep
from fileExtensions import commonFileTypes
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("240x190")
window.title("File Sorter")
window.resizable(False, False)


def createFolder(parent_dir):
    global dir_list
    dir_list = os.listdir(parent_dir)
    for fileTypes in dir_list:
        fileExt = fileTypes.split(".")[-1]
        if (
            fileExt.lower() in commonFileTypes
            and os.path.exists(parent_dir + "/" + commonFileTypes[fileExt]) == False
        ):
            os.mkdir(parent_dir + "/" + commonFileTypes[fileExt])


def sortFiles(parent_dir):
    for fileTypes in dir_list:
        fileExt = fileTypes.split(".")[-1]
        if fileExt.lower() in commonFileTypes:
            shutil.move(
                f"{parent_dir}/{fileTypes}",
                f"{parent_dir}/{commonFileTypes[fileExt]}/{fileTypes}",
            )


def sortButton():
    if directory not in [None, ""]:
        createFolder(directory)
        sleep(0.5)
        sortFiles(directory)
        messagebox.showinfo(
            "Finished sorting", "The files in your chosen directory have been sorted"
        )
    else:
        messagebox.showwarning(
            "Something's wrong",
            "I can feel it. It was an error, you didn't specify a path.",
        )


directory = None


def directorySelectButton():
    global directory
    directory = filedialog.askdirectory(title="Select a directory")


dirButton = ctk.CTkButton(
    master=window, command=lambda: directorySelectButton(), text="Choose directory"
)
sortFilesButton = ctk.CTkButton(
    master=window, command=lambda: sortButton(), text="Sort the files"
)
dirButton.pack(pady=30, padx=10)
sortFilesButton.pack(pady=30, padx=20)


window.mainloop()
