import pdfkit
from pathlib import Path

def get_folder() -> str:
    """
    Asks the user for the folder that should be searched for HTML files.
    Returns the folder path as a string.
    """
    return input("Which folder should be searched for HTML files?: ")


def files_exist(workingdir: Path) -> bool:
    """
    Checks if there are any HTML files in the specified directory.
    Returns True if HTML files exist, False otherwise.
    """
    return bool(list(workingdir.rglob("*html")))


def folder_exists(workingdir: Path) -> bool:
    """
    Checks if the specified folder exists.
    Returns True if the folder exists, False otherwise.
    """
    return Path(workingdir).is_dir()


def create_folder(workingdir: str):
    """
    Creates a folder at the specified path if it does not already exist.
    """
    try:
        if not folder_exists(workingdir):
            workingdir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: {e.strerror}")


def convert(workingfolder: Path, exportfolder: Path):
    """
    Converts all HTML files in the working folder to PDF files.
    The PDF files are saved in the export folder.
    """
    try:
        for file in list(workingfolder.rglob("*html")):
            oldfile = str(file)
            newfile = str(file.stem) + ".pdf"
            pdfkit.from_file(oldfile, exportfolder / newfile)
    except OSError as e:
        print(f"Error: {e.strerror}")


def main():
    """
    The main function that takes user input for a folder to search for HTML files,
    converts them to PDF, and saves the PDF files in a new folder.
    """
    workingdir = Path(get_folder())
    if files_exist(workingdir):
        exportfolder = workingdir / "convert_to_pdf"
        create_folder(exportfolder)
        convert(workingdir, exportfolder)
    else:
        print("Error: There are no .html files!")
        exit()

 
if __name__ == "__main__":
    main()