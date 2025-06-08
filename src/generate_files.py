import os
import shutil

def copy_files(src, dst):
    # Ensure source exists
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory '{src}' does not exist")

    # Create the destination directory
    os.makedirs(dst, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            # Recursively copy subdirectory (DFS)
            copy_files(src_path, dst_path)
        else:
            # Copy file
            shutil.copy2(src_path, dst_path)