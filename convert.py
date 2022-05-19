import pdfkit
from pathlib import Path


def get_folder() -> str:
    return input("Which folder should be search for html files?: ")

def files_exists(workingdir: Path) -> bool:
    return bool(list(workingdir.rglob("*html")) != 0)
        
def folder_exists(workingdir: Path):
    return Path(workingdir).is_dir()

def create_folder(workingdir: str):
    try:
        if not folder_exists(workingdir):
            workingdir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: {e.strerror}")  
        
def convert(workingfolder: Path, exportfolder: Path):
    try:
        for file in list(workingfolder.rglob("*html")):
            oldfile = str(file)
            newfile = str(file.stem) + ".pdf"
            pdfkit.from_file(oldfile, exportfolder / newfile)
    except OSError as e:
        print(f"Error: {e.strerror}")

def main():
    workingdir = Path(get_folder())
    if files_exists(workingdir):
        exportfolder = workingdir / "convert_to_pdf"
        create_folder(exportfolder)
        convert(workingdir, exportfolder)
    else:
        print("Error: There are no .html files!")
        exit()
 
if __name__ == "__main__":
    main()