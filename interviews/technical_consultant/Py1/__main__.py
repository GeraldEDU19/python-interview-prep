import os

# def foo(srcFileFullPath, destFileFullPath):
#     try:
#          if os.path.exists(destFileFullPath):
#              raise Exception("file %s already exist at destination %s" % (srcFileFullPath, destFileFullPath))
         
#          #copy the file. If possible, include code
#     except Exception:
#         raise
    
#     try:
#         os.remove(destFileFullPath)
#     except Exception:
#         raise


def copy_file_v1(src_file_path, dest_file_path, overwrite=False):
    """
    Copy a file using os library
    
    Args:
        src_file_path: The path to the source file.
        dest_file_path: The path to the destination file.
        overwrite (bool): Whether to overwrite the destination file if it exists.
        
        
    Raises:
        FileNotFoundError: If the file does not exist.
        FileExistsError: If the destination file already exists and overwrite is False.
        OSError: If the file cannot be copied for any other reason.
    """
    
    if not os.path.exists(src_file_path):
        raise FileNotFoundError(f"Source file does not exist. {src_file_path}")
    
    if not os.path.isfile(src_file_path):
        raise ValueError(f"Source path is not a file. {src_file_path}")
    
    
    dest_dir = os.path.dirname(dest_file_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    if os.path.exists(dest_file_path) and not overwrite:
        raise FileExistsError(f"Destination file already exists. {dest_file_path}")
    
    try:
        with open(src_file_path, 'r') as src_file:
            content = src_file.read()

        with open(dest_file_path, 'w') as dest_file:
            dest_file.write(content)
            
        src_stat = os.stat(src_file_path)
        os.utime(dest_file_path, (src_stat.st_atime, src_stat.st_mtime))
        
    except OSError as e:
        if os.path.exists(dest_file_path):
            try:
                os.remove(dest_file_path)
            except OSError as e:
                pass
        raise OSError(f"Failed to copy file: {e}")
    
def copy_file_v2(srcFileFullPath, destFileFullPath):
    """
    Copy file following the original foo structure bud fixed and functional
    
    Args:
        srcFileFullPath: Source file path
        destFileFullPath: Destination file path
    """    
    try: 
        if os.path.exists(destFileFullPath):
            raise Exception("File %s already exists at destination %s" % (srcFileFullPath, destFileFullPath))
        
        with open(srcFileFullPath, 'rb') as src_file:
            content = src_file.read()
            
        with open(destFileFullPath, 'wb') as dest_file:
            dest_file.write(content)
            
        src_stat = os.stat(srcFileFullPath)
        os.utime(destFileFullPath, (src_stat.st_atime, src_stat.st_mtime))
        
    except Exception:
        if os.path.exists(destFileFullPath):
            try:
                os.remove(destFileFullPath)
            except Exception:
                pass
        raise


if __name__ == "__main__":
    try:
        # Test original structure version
        copy_file_v2(
            "c:/test/source.txt",
            "c:/test/destination_v2.txt"
        )
        print("Copy v2 successful!")
        
        # Test improved version
        copy_file_v1(
            "c:/test/source.txt",
            "c:/test/destination.txt",
            overwrite=False
        )
        print("Copy v1 successful!")
        
    except (FileNotFoundError, FileExistsError, OSError, ValueError, Exception) as e:
        print(f"Error occurred: {e}")