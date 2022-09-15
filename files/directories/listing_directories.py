import os

basepath: str = './'

def retrieving_directories():
    entries = os.listdir(basepath)
    print(f"Current directory files and directories:")
    for entry in entries:
        print(entry)


def scan_directories():
    with os.scandir(basepath) as entries:
        print(f"\nCurrent files:")
        for entry in entries:
            if entry.is_file():
                print(entry.name)


if __name__ == '__main__':
    retrieving_directories()
    scan_directories()
