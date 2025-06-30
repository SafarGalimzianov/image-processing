# Image Processing Tools for Windows

A lightweight Windows 11 tool that adds image compression functionality directly to the Windows context menu. Compress JPEG, PNG, BMP, and GIF images with a simple right-click.

## Features

- **Context Menu Integration**: Right-click on any supported image file to compress it
- **Multiple Format Support**: Works with JPEG, PNG, BMP, and GIF files
- **In-Place Compression**: Automatically replaces the original image with the compressed version
- **Optimized Compression**: Uses format-specific optimization parameters
- **One-Click Installation**: Automated installer with Windows registry integration

## Supported Formats

| Format | Compression Method |
|--------|-------------------|
| JPEG/JPG | Quality: 60%, Optimize: True |
| PNG | Optimize: True |
| GIF | Optimize: True |
| BMP | Standard compression |

## Installation

1. **Build the executable** (requires PyInstaller):
   ```bash
   pip install pyinstaller pillow
   pyinstaller install_compress_image.spec
   ```

2. **Run the installer** as Administrator:
   - Navigate to the `dist` folder after building
   - Run `install_compress_image.exe` as Administrator
   - The installer will automatically add the context menu entries

3. **Verify installation**:
   - Right-click on any image file
   - You should see "Compress image" option in the context menu

## Usage

1. Right-click on any supported image file (JPEG, PNG, BMP, GIF)
2. Select "Compress image" from the context menu
3. The image will be compressed and replaced with the optimized version

## Technical Details

### Core Components

- [`compress_image.py`](compress_image.py): Main compression logic using PIL/Pillow
- [`install_compress_image.py`](install_compress_image.py): Windows registry installer
- [`install_compress_image.spec`](install_compress_image.spec): PyInstaller configuration

### Dependencies

- **PIL (Pillow)**: Image processing library
- **winreg**: Windows registry manipulation
- **ctypes**: Windows API access for admin privileges

### Registry Keys Modified

The installer creates context menu entries in:
```
HKEY_CLASSES_ROOT\{filetype}\shell\Compress\command
```

For file types: `jpegfile`, `pngfile`, `bmpfile`, `giffile`

## Requirements

- Windows 11 (or Windows 10)
- Administrator privileges for installation
- Python 3.6+ (for building from source)
- PIL/Pillow library

## Building from Source

1. **Install dependencies**:
   ```bash
   pip install pillow pyinstaller
   ```

2. **Build the compression tool**:
   ```bash
   pyinstaller --onefile compress_image.py
   ```

3. **Build the installer**:
   ```bash
   pyinstaller install_compress_image.spec
   ```

4. **Run installation**:
   ```bash
   # Run as Administrator
   dist/install_compress_image.exe
   ```

## Security Note

The installer requires Administrator privileges to modify the Windows registry and add context menu entries. This is necessary for system-wide integration.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on Windows 11
5. Submit a pull request

## Troubleshooting

### Installation Issues
- Ensure you're running the installer as Administrator
- Check that Windows Defender isn't blocking the executable
- Verify Python and PIL are properly installed

### Compression Issues
- Ensure the image file isn't corrupted
- Check that the file format is supported
- Verify the file isn't in use by another application

## Future Enhancements

- [ ] Save compressed image with different name option
- [ ] Customizable compression quality settings
- [ ] Support for additional image formats (WebP, TIFF)
- [ ] Batch compression for multiple files
- [ ] Image rotation and other transformations
