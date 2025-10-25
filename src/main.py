import os
import shutil

SOURCE_DIR = '/mnt/c/Users/Asus/Downloads' 
DESTINATION_DIR = '/mnt/c/Users/Asus/Documents/Automated_Files' 

def normalize_path(path):
    return os.path.expanduser(path)

def organize_files(source, destination):
    source = normalize_path(source)
    destination = normalize_path(destination)
    
    try:
        os.makedirs(destination, exist_ok=True)
    except Exception as e:
        print(f"Error creating destination directory: {e}")
        return

    try:
        file_list = os.listdir(source)
    except FileNotFoundError:
        print(f"Error: Source directory not found: {source}")
        return
    except Exception as e:
        print(f"Error accessing source directory: {e}")
        return

    for filename in file_list:
        source_path = os.path.join(source, filename)
        
        if os.path.isfile(source_path):
            _, extension = os.path.splitext(filename)
            extension = extension.lower().strip('.')
            
            if not extension:
                target_folder = os.path.join(destination, 'Others')
            else:
                target_folder = os.path.join(destination, extension.upper() + '_Files')
            
            os.makedirs(target_folder, exist_ok=True)
            
            dest_path = os.path.join(target_folder, filename)
            
            try:
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename} -> {target_folder.replace(normalize_path('/mnt/c/Users/Asus'), 'C:\\Users\\Asus')}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == '__main__':
    print("Starting file organization...")
    organize_files(SOURCE_DIR, DESTINATION_DIR)
    print("File organization complete.")