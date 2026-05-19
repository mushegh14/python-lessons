import argparse
import shutil
from pathlib import Path


def create_folders(folder):
    documents_folder = folder / "documents"
    documents_folder.mkdir(exist_ok=True)

    pdfs_folder = folder / "pdfs"
    pdfs_folder.mkdir(exist_ok=True)

    images_folder = folder / "images"
    images_folder.mkdir(exist_ok=True)

    archives_folder = folder / "archives"
    archives_folder.mkdir(exist_ok=True)

    others_folder = folder / "others"
    others_folder.mkdir(exist_ok=True)


def get_category(file):
    extension = file.suffix.lower()

    categories = {
        "documents": {".doc", ".docx", ".txt", ".xls", ".xlsx"},
        "pdfs": {".pdf"},
        "images": {".jpg", ".jpeg", ".png", ".gif"},
        "archives": {".zip", ".rar", ".tar"},
    }

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "others"


def move_files(folder):
    documents_count = 0
    pdfs_count = 0
    images_count = 0
    archives_count = 0
    others_count = 0

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item)
            new_place = folder / category / item.name

            shutil.move(str(item), str(new_place))

            if category == "documents":
                documents_count += 1

            elif category == "pdfs":
                pdfs_count += 1

            elif category == "images":
                images_count += 1

            elif category == "archives":
                archives_count += 1

            else:
                others_count += 1

            print(item.name, "->", new_place)

    print()
    print("texapoxavac fayler․")
    print("- documents:", documents_count)
    print("- pdfs:", pdfs_count)
    print("- images:", images_count)
    print("- archives:", archives_count)
    print("- others:", others_count)


def main():
    parser = argparse.ArgumentParser(description="File organizer program")

    parser.add_argument(
        "-f",
        "--folder",
        required=True,
        metavar="add_folder",
        help="Folder path that should be organized"
    )

    args = parser.parse_args()

    folder = Path(args.folder)

    if not folder.exists():
        print("eror ays foldern gyutyun chuni")
        return

    if not folder.is_dir():
        print("error sa folder che")
        return

    print("folder chist e:", folder)

    create_folders(folder)

    print("foldernern stxcvac en ")
    print()

    move_files(folder)


main()