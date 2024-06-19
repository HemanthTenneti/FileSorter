# File Sorter

Getting more comfortable with Python, I decided to take upon a task that would take a lot of understanding of the language to execute it into existence. I chose a file sorter then as a way of streamlining the process of organizing my files easier on my desktop, I went further with it, designing a very minimal user interface that did the job.

## How It Works

- It works with the simple principle of organizing files in a given folder with it's filetypes.
- The `fileExtensions.py` consists a map with each file type to a certain folder name.
- The main program looks for all singular scattered files in a given desktop location, ignoring all folders.
- And it proceeds to create folders for each depending on the map of the file extensions.
- Assuming the program has permission to move items in the given location, it will proceed to move the files to their designated folder.

## Latest Add
- Added the functionality to call it through command-line
- You can call it either through:
```
python "Path/To/PythonFile" "Path/To/Directory/To/Be/Sorted"
eg. python "C:/Users/test/FileSorter/fileSort.py" "C:/Users/test/Downloads"
```
- Or alternatively, with a slight setup process, you can run "FileSort" in any powershell terminal and it'll sort the CWD.

## Setup for FileSort PWSH Function
- 1. Create a fileSort.ps1 script in any folder with contents:
```
$cwd = Get-Location
python "Path/To/PyFile" $cwd
```
- 2. Open Powershell, type the command `notepad $PROFILE`
- 3. Add a function to the profile:
```
function fileSort {
    # Path to the recently created fileSort.ps1 script
    $scriptPath = "Path/To/fileSort.ps1/Script"
    
    & $scriptPath
}
```
- 4. After the setup, you can open powershell in any folder and run the command "FileSort" with which, it's going to sort all the files in the working directory

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

- **Images:** `.jpg, .jpeg, .png, .gif, .bmp, .ico, .svp, .webp, .tif, .tiff, .eps, .ai, .psd, .jfif`
- **Executable Files:** `.exe, .msi, .bat, .cmd, .ps1, .vbs`
- **Dynamic Link Library Files:** `.dll`
- **System Files:** `.sys`
- **Fonts:** `.ttf, .otf, .eot, .woff, .woff2`
- **Archives:** `.zip, .tar, .7z, .cab, .gz, .tar, .zipx`
- **Documents:** `.pdf, .doc, .txt, .rtf, .xls, .xlsx, .ppt, .pptx, .csv, .pub`
- **Audio Files:** `.mp3, .wav, .ogg, .flac, .aac`
- **Video Files:** `.mp4, .avi, .wmv, .mov, .mpg, .mpeg, .webm`
- **Shortcut Files:** `.lnk`
- **Configuration Files:** `.ini, .cfg`
- **Log Files:** `.log`
- **Registry Entries:** `.reg`
- **Disk Images:** `.iso, .img`
- **Virtual Hard Disk Files:** `.vhd`
- **Data:** `.csv, .json, .xml`
- **Web Files:** `.html, .htm, .js, .php, .asp`
- **Scripts:** `.py, .bat, .ps1, .sh, .c, .cpp`
- **Database Files:** `.sql, .db, .mdb, .accdb`
- **Spreadsheets:** `.csv, .xml, .xlr`
- **Emails:** `.msg, .eml`
- **Contacts:** `.vcf`
- **Calendar:** `.ics`
- **Backup Files:** `.bak`
- **Temporary Files:** `.tmp`
- **Notebook Files:** `.ipynb`
- **Java Files:** `.java`
- **Java Class Files:** `.class`

## Future Enhancements

- Possible ideas for future improvements would be giving users the option to sort file types into their own folders with a setup process that would be done upon installation. Although, same effect can be achieved by editing the `fileExtensions.py` and configuring it to your own need and recompiling the program.
- Adding more file types.
