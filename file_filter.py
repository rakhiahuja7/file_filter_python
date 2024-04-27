import shutil
import os
os.chdir(r'c:\Users\Lenovo\Desktop')
os.makedirs('JECRC',exist_ok=True)
os.chdir(r'C:\Users\Lenovo\Desktop\JECRC')
os.makedirs('image_folder' ,exist_ok=True)
os.makedirs('pdf_folder',exist_ok=True)
os.makedirs('text_folder' ,exist_ok=True)
for file in os.listdir(r'C:\Users\Lenovo\Desktop\JECRC'):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpg'):
        shutil.move(os.path.join(r'C:\Users\Lenovo\Desktop\JECRC',file),os.path.join(r'C:\Users\Lenovo\Desktop\JECRC','image_folder'))
    elif file.endswith('.pdf'):
        shutil.move(os.path.join(r'C:\Users\Lenovo\Desktop\JECRC',file),os.path.join(r'C:\Users\Lenovo\Desktop\JECRC','pdf_folder'))
    elif file.endswith('.txt') or file.endswith('.doc'):
        shutil.move(os.path.join(r'C:\Users\Lenovo\Desktop\JECRC',file),os.path.join(r'C:\Users\Lenovo\Desktop\JECRC','text_folder'))
