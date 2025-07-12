import os, datetime

pathUser = input("Enter your desktop username:")

dict = {"imgFolder": 0,
"textFolder": 0,
"audioFolder": 0,
"videoFolder": 0,
"pdfFolder": 0,
"compressedFolder": 0,
"executableFolder": 0,
"officeFolder": 0,
"presentationFolder": 0,
"webFolder": 0,
"dataFolder": 0,
"vectorFolder": 0,
"pythonFolder": 0,
"csvFolder": 0,
"markdownFolder": 0,
"otherFolder": 0
}

log_map = {
    "imgFolder": "images",
    "textFolder": "docs",
    "audioFolder": "audio",
    "videoFolder": "videos",
    "pdfFolder": "docs",
    "compressedFolder": "zips",
    "executableFolder": "executables",
    "officeFolder": "docs",
    "presentationFolder": "docs",
    "webFolder": "web",
    "dataFolder": "data",
    "vectorFolder": "vector",
    "pythonFolder": "python",
    "csvFolder": "csv",
    "markdownFolder": "docs",
    "otherFolder": "other"
}
moved_files = {v: [] for v in log_map.values()}

# Create directories for organizing files

def organize_files():
    os.chdir(f"C:\\Users\\{pathUser}\\Downloads")
    for file in os.listdir():
        if not os.path.isfile(file):
            continue
        if file.endswith('.txt'):
            if not os.path.exists("TextFiles"):
                os.makedirs("TextFiles")
            os.rename(file, f"TextFiles\\{file}")
            dict["textFolder"] += 1
            moved_files["docs"].append(f"{file} → docs/{file}")
        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif'):
            if not os.path.exists("ImageFiles"):
                os.makedirs("ImageFiles")
            os.rename(file, f"ImageFiles\\{file}")
            dict["imgFolder"] += 1
            moved_files["images"].append(f"{file} → images/{file}")
        elif file.endswith('.mp3'):
            if not os.path.exists("AudioFiles"):
                os.makedirs("AudioFiles")
            os.rename(file, f"AudioFiles\\{file}")
            dict["audioFolder"] += 1
            moved_files["audio"].append(f"{file} → audio/{file}")
        elif file.endswith('.mp4'):
            if not os.path.exists("VideoFiles"):
                os.makedirs("VideoFiles")
            os.rename(file, f"VideoFiles\\{file}")
            dict["videoFolder"] += 1
            moved_files["videos"].append(f"{file} → videos/{file}")
        elif file.endswith('.pdf'):
            if not os.path.exists("PDFs"):
                os.makedirs("PDFs")
            os.rename(file, f"PDFs\\{file}")
            dict["pdfFolder"] += 1
            moved_files["docs"].append(f"{file} → docs/{file}")
        elif file.endswith('.zip') or file.endswith('.rar'):
            if not os.path.exists("CompressedFiles"):
                os.makedirs("CompressedFiles")
            os.rename(file, f"CompressedFiles\\{file}")
            dict["compressedFolder"] += 1
            moved_files["zips"].append(f"{file} → zips/{file}")
        elif file.endswith('.exe'):
            if not os.path.exists("ExecutableFiles"):
                os.makedirs("ExecutableFiles")
            os.rename(file, f"ExecutableFiles\\{file}")
            dict["executableFolder"] += 1
            moved_files["executables"].append(f"{file} → executables/{file}")
        elif file.endswith('.docx') or file.endswith('.xlsx'):
            if not os.path.exists("OfficeFiles"):
                os.makedirs("OfficeFiles")
            os.rename(file, f"OfficeFiles\\{file}")
            dict["officeFolder"] += 1
            moved_files["docs"].append(f"{file} → docs/{file}")
        elif file.endswith('.pptx'):
            if not os.path.exists("PresentationFiles"):
                os.makedirs("PresentationFiles")
            os.rename(file, f"PresentationFiles\\{file}")
            dict["presentationFolder"] += 1
            moved_files["docs"].append(f"{file} → docs/{file}")
        elif file.endswith('.html') or file.endswith('.css') or file.endswith('.js'):
            if not os.path.exists("WebFiles"):
                os.makedirs("WebFiles")
            os.rename(file, f"WebFiles\\{file}")
            dict["webFolder"] += 1
            moved_files["web"].append(f"{file} → web/{file}")
        elif file.endswith('.json') or file.endswith('.xml'):
            if not os.path.exists("DataFiles"):
                os.makedirs("DataFiles")
            os.rename(file, f"DataFiles\\{file}")
            dict["dataFolder"] += 1
            moved_files["data"].append(f"{file} → data/{file}")
        elif file.endswith('.svg'):
            if not os.path.exists("VectorFiles"):
                os.makedirs("VectorFiles")
            os.rename(file, f"VectorFiles\\{file}")
            dict["vectorFolder"] += 1
            moved_files["vector"].append(f"{file} → vector/{file}")
        elif file.endswith('.py'):
            if not os.path.exists("PythonFiles"):
                os.makedirs("PythonFiles")
            os.rename(file, f"PythonFiles\\{file}")
            dict["pythonFolder"] += 1
            moved_files["python"].append(f"{file} → python/{file}")
        elif file.endswith('.csv'):
            if not os.path.exists("CSVFiles"):
                os.makedirs("CSVFiles")
            os.rename(file, f"CSVFiles\\{file}")
            dict["csvFolder"] += 1
            moved_files["csv"].append(f"{file} → csv/{file}")
        elif file.endswith('.md'):
            if not os.path.exists("MarkdownFiles"):
                os.makedirs("MarkdownFiles")
            os.rename(file, f"MarkdownFiles\\{file}")
            dict["markdownFolder"] += 1
            moved_files["docs"].append(f"{file} → docs/{file}")
        else:
            if not os.path.exists("OtherFiles"):
                os.makedirs("OtherFiles")
            os.rename(file, f"OtherFiles\\{file}")
            dict["otherFolder"] += 1
            moved_files["other"].append(f"{file} → other/{file}")
organize_files()
print(f"✅ {len(os.listdir())} files organized successfully.")
for key in dict:
    if dict[key] > 0:
        print(f"📂 Created {dict[key]} folders for {key.replace('Folder', '')} files.")

today_str = datetime.datetime.now().strftime("%Y-%m-%d")
log_filename = os.path.join(f"C:\\Users\\{pathUser}\\downloads-organizer", f"log_{today_str}.txt")  # Change this line
downloads_path = f"C:\\Users\\{pathUser}\\Downloads"
total_files = sum(dict.values())
folders_created = sum(1 for v in dict.values() if v > 0)

with open(log_filename, "w", encoding="utf-8") as log:
    log.write(f"🗓️  Log Date: {today_str}  |  Folder Scanned: {downloads_path}\n\n")
    log.write("📊 Summary:\n")
    log.write(f"  - Total files scanned: {total_files}\n")
    log.write(f"  - Total folders created: {folders_created}\n\n")
    log.write("📦 Files Moved:\n")
    for folder, files in moved_files.items():
        if files:
            log.write(f"  - {folder}/: {len(files)} files\n")
    log.write("\n✅ File Actions:\n")
    for folder, files in moved_files.items():
        for entry in files:
            log.write(f"  - {entry}\n")
    log.write("\nOrganizing complete! Check your Downloads folder for organized files.\n")

sum = 0
for values in dict.values():
    sum = sum + values
print(f"📦 Moved: \n  - {sum} files")

print("Organizing complete! Check your Downloads folder for organized files.")
print(f"📃 Logs available in {log_filename}.txt ")



        