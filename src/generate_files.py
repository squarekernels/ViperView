import os 
import shutil

def generate_files(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")
    
    os.makedirs(dest_dir, exist_ok=True)

    for dir in os.listdir(source_dir):
        src_path = os.path.join(source_dir, dir)
        dst_path = os.path.join(dest_dir, dir)

        if os.path.isdir(src_path):
            # Recursively copy subdirectory (DFS)
            generate_files(src_path, dst_path)
        else:
            # Copy file
            shutil.copy2(src_path, dst_path)

generate_files(source_dir="src/", dest_dir="public/")

    
