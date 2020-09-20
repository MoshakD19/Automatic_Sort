import os
import shutil

os.chdir("/Users/shakurduale/Downloads")

# print(os.getcwd())

for f in os.listdir():
    name, ext = os.path.splitext(f)
    print(name, ext)
    if ext == '.jpg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/jpg/{f}')
        print(f'moved {f}')
    elif ext == '.png':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/png/{f}')
        print(f'moved {f}')
    elif ext == '.jpeg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/jpeg/{f}')
        print(f'moved {f}')
    elif ext == '.py':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Python/{f}')
        print(f'moved {f}')
    elif ext == '.docx' or ext == '.pdf' or ext == '.doc':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Docs_and_pdfs/{f}')
        print(f'moved {f}')
    elif ext == '.html' or ext == '.css' or ext == '.htm':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/web/{f}')
        print(f'moved {f}')
    elif ext == '.zip':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/zip_files/{f}')
        print(f'moved {f}')
    elif ext == '.ppt' or ext == '.pub' or ext == '.pptx' or ext == '.xls' or ext == '.xlsx':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Office/{f}')
        print(f'moved {f}')
    elif ext == '.json':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/JSON/{f}')
        print(f'moved {f}')
    elif ext == '.ipynb':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Jupyter_Notebook/{f}')
        print(f'moved {f}')
    elif ext == '.txt' or ext == '.csv':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/text_file/{f}')
        print(f'moved {f}')
    elif ext == '.pkg' or ext == '.dmg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Package/{f}')
        print(f'moved {f}')
    elif ext == '.sb3':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Scratch/{f}')
        print(f'moved {f}')
    elif ext == '.java':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Java/{f}')
        print(f'moved {f}')
    elif ext == '.whl':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Python/Python_Wheel/{f}')
        print(f'moved {f}')
    elif ext == '.mdj':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/UML/{f}')
        print(f'moved {f}')
    elif len(ext) == 0:
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Other/{f}')
        print(f'moved {f}')
    elif ext == '.app':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Apps/{f}')
        print(f'moved {f}')
    elif ext == '.exe':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Executables/{f}')
        print(f'moved {f}')
    elif ext == '.ovpn':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/OpenVPN/{f}')
        print(f'moved {f}')
    elif ext == '.download':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/download_extension/{f}')
        print(f'moved {f}')
