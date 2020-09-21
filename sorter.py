import os
import shutil

os.chdir("/Users/shakurduale/Downloads")

for f in os.listdir():
    name, ext = os.path.splitext(f)

    if ext == '.jpg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/jpg/{f}')

    elif ext == '.png':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/png/{f}')

    elif ext == '.jpeg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/jpeg/{f}')

    elif ext == '.gif':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Pictures/gifs/{f}')

    elif ext == '.py':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Python/{f}')

    elif f == '__pycache__':
        shutil.rmtree(f"/Users/shakurduale/Downloads/{f}")

    elif ext == '.textClipping':
        os.remove(f"/Users/shakurduale/Downloads/{f}")

    elif ext == '.docx' or ext == '.pdf' or ext == '.doc' or ext == '.dotx':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Docs_and_pdfs/{f}')

    elif ext == '.html' or ext == '.css' or ext == '.htm':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/web/{f}')

    elif ext == '.zip':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/zip_files/{f}')

    elif ext == '.ppt' or ext == '.pub' or ext == '.pptx' or ext == '.xls' or ext == '.xlsx':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Office/{f}')

    elif ext == '.json':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/JSON/{f}')

    elif ext == '.ipynb':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Jupyter_Notebook/{f}')

    elif ext == '.txt' or ext == '.csv':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/text_file/{f}')

    elif ext == '.pkg' or ext == '.dmg':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Package/{f}')

    elif ext == '.sb3':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Scratch/{f}')

    elif ext == '.java':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Java/{f}')

    elif ext == '.whl':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Python/Python_Wheel/{f}')

    elif ext == '.mdj':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/UML/{f}')

    elif os.path.isdir(f"/Users/shakurduale/Downloads/{f}"):
        if len(os.listdir(f"/Users/shakurduale/Downloads/{f}")) == 0:
            shutil.rmtree(f"/Users/shakurduale/Downloads/{f}")
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Folders/{f}')

    elif ext == '.app':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Apps/{f}')

    elif ext == '.exe':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Executables/{f}')

    elif ext == '.ovpn':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/OpenVPN/{f}')

    elif ext == '.download':
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/download_extension/{f}')

    elif len(ext) == 0:
        shutil.move(f'/Users/shakurduale/Downloads/{f}', f'/Users/shakurduale/Documents/Other/{f}')
