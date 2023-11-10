import shutil
import os
from time import sleep
import customtkinter as ctk
from fileExtensions import commonFileTypes
from tkinter import filedialog
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("240x175")
window.title("File Sorter")
window.resizable(False, False)


def createFolder(parent_dir):
    global dir_list
    dir_list = os.listdir(parent_dir)
    for fileTypes in dir_list:
        if not os.path.isdir(parent_dir + "\\" + fileTypes):
            fileExt = fileTypes.split(".")[-1].lower()
            if (
                fileExt.lower() in commonFileTypes
                and os.path.exists(parent_dir + "/" + commonFileTypes[fileExt]) == False
            ):
                os.mkdir(parent_dir + "/" + commonFileTypes[fileExt])


def sortFiles(parent_dir):
    for fileTypes in dir_list:
        if not os.path.isdir(parent_dir + "\\" + fileTypes):
            fileExt = fileTypes.split(".")[-1].lower()
            if fileExt.lower() in commonFileTypes:
                shutil.move(
                    f"{parent_dir}/{fileTypes}",
                    f"{parent_dir}/{commonFileTypes[fileExt]}/{fileTypes}",
                )


def sortButton():
    global directory
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
            "I can feel it. It was an error, you didn't specify a path",
        )
        
def exploreFolder(directory):
    if directory == None:
        messagebox.showwarning("Error", 'No folder selected')
    elif os.path.isdir(directory):
        os.startfile(directory)
    else:
        messagebox.showwarning("Error", 'Not a folder')

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
explorerButton = ctk.CTkButton(
    master=window, command=lambda: exploreFolder(directory), text="Open Folder"
)
dirButton.pack(pady=15, padx=15)
sortFilesButton.pack(pady=15, padx=15)
explorerButton.pack(pady=15, padx=15)


window.mainloop()
