pyinstaller [name].py #export to one-folder

pyinstaller [name].py -n hacker #set file name => hacker.exe

pyinstaller [name].py -F #export to one-file

pyinstaller [name].py --distpath "C:\Users\eric5\OneDrive" #set export address at C:\Users\eric5\OneDrive

pyinstaller [name].py -w #run without console

pyinstaller [name].py --add-data="C:\Users\eric5\AppData\Local\Programs\Python\Python310\Lib\site-packages\mediapipe\modules;mediapipe/modules"
#Mediapipe modules can't be read by pyinstaller,so we add it manually.
