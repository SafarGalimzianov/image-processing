import os
import sys
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_file_association(extension):
    """Get the actual file association for a given extension"""
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, extension) as key:
            file_type, _ = winreg.QueryValueEx(key, "")
            return file_type
    except:
        return None

def main():
    # Check if the app is installed under admin permission
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, ' '.join(sys.argv), None, 1
        )
        sys.exit(0)

    exe_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'compress_image.exe'))
    
    # Get actual file associations
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    file_types = set()
    
    for ext in extensions:
        file_type = get_file_association(ext)
        if file_type:
            file_types.add(file_type)
    
    # Also add the common default types as fallback
    file_types.update(['jpegfile', 'pngfile', 'bmpfile', 'giffile'])
    
    success_count = 0
    for file_type in file_types:
        try:
            menu_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, fr"{file_type}\shell\Compress")
            winreg.SetValueEx(menu_key, "", 0, winreg.REG_SZ, "Compress image")
            winreg.SetValueEx(menu_key, "Icon", 0, winreg.REG_SZ, "imageres.dll,-5302")
            command_key = winreg.CreateKey(menu_key, "command")
            winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, f'"{exe_path}" "%1"')
            command_key.Close()
            menu_key.Close()
            success_count += 1
            print(f"Successfully added context menu for {file_type}")
        except Exception as e:
            print(f"Error occurred for {file_type}: {e}")

    # Also try adding to extensions directly as fallback
    for ext in extensions:
        try:
            menu_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, fr"{ext}\shell\Compress")
            winreg.SetValueEx(menu_key, "", 0, winreg.REG_SZ, "Compress image")
            winreg.SetValueEx(menu_key, "Icon", 0, winreg.REG_SZ, "imageres.dll,-5302")
            command_key = winreg.CreateKey(menu_key, "command")
            winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, f'"{exe_path}" "%1"')
            command_key.Close()
            menu_key.Close()
            success_count += 1
            print(f"Successfully added context menu for extension {ext}")
        except Exception as e:
            print(f"Error occurred for extension {ext}: {e}")

    if success_count > 0:
        message = f"Installation completed! Added {success_count} registry entries.\n\nPlease right-click on an image file and look for 'Compress image' option.\n\nIf you still don't see it, try:\n1. Restart Windows Explorer\n2. Reboot your computer"
    else:
        message = "Installation failed! No registry entries were created. Please run as Administrator and check for errors."
    
    ctypes.windll.user32.MessageBoxW(0, message, "Installation Result", 0)

if __name__ == "__main__":
    main()
