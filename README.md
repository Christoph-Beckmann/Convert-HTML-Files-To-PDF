# HTML-to-PDF Converter

This program is a simple command-line tool that searches for HTML files in a specified folder and converts them into PDF files. The PDF files are saved in a new folder within the original directory.

## Table of Contents

- [Functionality](#functionality)
- [Installation](#installation)
- [Usage](#usage)
- [Function Overview](#function-overview)

## Functionality

The HTML-to-PDF Converter allows you to:

- Specify a folder to search for HTML files
- Automatically detect HTML files within the specified folder
- Convert the HTML files to PDF format
- Save the PDF files in a new folder within the original directory

## Installation

1. Clone the repository from GitHub: `git clone https://github.com/Christoph-Beckmann/html-to-pdf-converter.git`
2. Navigate to the project folder and install the required dependencies using the requirements.txt file: 
```sh
cd html-to-pdf-converter
pip install -r requirements.txt
```

## Usage

Run the program using the following command: `python3 main.py`


You will be prompted to enter the folder where the HTML files are located. The program will search for HTML files, convert them to PDF, and save them in a new folder named "convert_to_pdf" within the original directory.

## Function Overview

- `get_folder()`: Asks the user for the folder to search for HTML files
- `files_exist(workingdir: Path)`: Checks if there are any HTML files in the specified directory
- `folder_exists(workingdir: Path)`: Checks if the specified folder exists
- `create_folder(workingdir: str)`: Creates a folder at the specified path if it does not already exist
- `convert(workingfolder: Path, exportfolder: Path)`: Converts all HTML files in the working folder to PDF files and saves them in the export folder
- `main()`: The main function that takes user input, searches for HTML files, converts them to PDF, and saves the PDF files in a new folder
