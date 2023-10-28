# File Sorter
Getting more comfortable with Python, I decided to take upon a task that would take a lot of understanding of the language to execute it into existence. I chose a file sorter then as a way of streamlining the process of organizing my files easier on my desktop, I went further with it, designing a very very minimal user interface that did the job.


## How It Works
- It works with the simple principle of organizing files in a given folder with it's filetypes.
- The `fileExtensions.py` consists a map with each file type to a certain folder name.
- The main program looks for all singular scattered files in a given desktop location, ignoring all folders.
- And it proceeds to create folders for each depending on the map of the file extensions.
- Assuming the program has permission to move items in the given location, it will proceed to move the files to their designated folder.


## Requirements
- As the file was compiled into an executable which can be found in the Releases section, there are no requirements for it to be ran.
- However, if you want to compile and run the program yourself, you would require:
- Python3: As this project was built entirely with Python, Python3 is required with the latest version being recommended.
- The libraries used which need to be installed are `tkinter` and `customtkinter`, as these were used to make the user interface for the program.
- You can install them by:
- ```
  pip install tk
  pip install customtkinter
  ```
  
## Sorting Map:
- **Images:** `.jpg, .jpeg, .png, .gif, .bmp, .ico, .svp, .webp, .tif, .tiff, .eps, .ai, .psd`
- **Executable Files:** `.exe, .msi, .bat, .cmd, .ps1, .vbs`
- **Dynamic Link Library Files:** `.dll`
- **System Files:** `.sys`
- **Fonts:** `.ttf, .otf`
- **Archives:** `.zip, .tar, .7z, .cab, .gz, .tar, .zipx`
- **Documents:** `.pdf, .doc, .txt, .rtf, .xls, .xlsx, .ppt, .pptx, .csv`
- **Audio Files:** `.mp3, .wav, .ogg, .flac, .aac`
- **Video Files:** `.mp4, .avi, .wmv, .mov, .mpg, .mpeg`
- **Shortcut Files:** `.lnk`
- **Configuration Files:** `.ini, .cfg`
- **Log Files:** `.log`
- **Registry Entries:** `.reg`
- **Disk Images:** `.iso, .img`
- **Virtual Hard Disk Files:** `.vhd`
- **Data:** `.csv, .json, .xml`
- **Web Files:** `.html, .htm, .js, .php, .asp`
- **Scripts:** `.py, .bat, .ps1, .sh`
- **Database Files:** `.sql, .db, .mdb, .accdb`
- **Spreadsheets:** `.csv, .xml, .xlr`
- **Emails:** `.msg, .eml`
- **Contacts:** `.vcf`
- **Calendar:** `.ics`
- **Backup Files:** `.bak`
- **Temporary Files:** `.tmp`

## Future Enhancements
- Possible ideas for future improvements would be giving users the option to sort file types into their own folders with a setup process that would be done upon installation. Although, same effect can be achieved by editing the `fileExtensions.py` and configuring it to your own need and recompiling the program.
- Adding more file types.
