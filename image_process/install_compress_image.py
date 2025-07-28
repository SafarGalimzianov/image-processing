import os
import sys
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    # Check if the app is installed under admin permission
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, ' '.join(sys.argv), None, 1
        )
        sys.exit(0)

    exe_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'compress_image.exe'))
    types = ['jpegfile', 'pngfile', 'bmpfile', 'giffile']
    for t in types:
        try:
            menu_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, fr"{t}\shell\Compress")
            winreg.SetValueEx(menu_key, "", 0, winreg.REG_SZ, "Compress image")
            winreg.SetValueEx(menu_key, "Icon", 0, winreg.REG_SZ, "imageres.dll,-5302")
            command_key = winreg.CreateKey(menu_key, "command")
            winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, f'"{exe_path}" "%1"')
            command_key.Close()
            menu_key.Close()
        except Exception as e:
            print(f"Error occured for {t}: {e}")

    ctypes.windll.user32.MessageBoxW(0, "Installation is complete!\n\
                                     Please right-click and choose 'Compress image'\n\
                                     to replace the current image with compressed one.\
                                     Please right-click and choose 'Compress image and save it...\n\
                                     to compress image and save it where you like", "Done!", 0)

if __name__ == "__main__":
    main()
