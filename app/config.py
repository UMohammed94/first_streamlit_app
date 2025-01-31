import os
from pathlib import Path

current_dir = Path.cwd()
parent_dir = current_dir.parent
raw_csv_dir = current_dir / 'output_files'


required_dirs=[raw_csv_dir]

def create_directories(dirs: list) -> None:
    print(f"checking if required dirs exist")
    for dir_path in dirs:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
    print(f"all required dirs exist.")

create_directories(required_dirs)

print(required_dirs)