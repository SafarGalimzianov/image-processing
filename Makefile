b:
	pyinstaller --onefile releases\image_processing_rls_ver.py
	if exist del image_processing_rls_ver.exe
	move ".\dist\image_processing_rls_ver" ".\"
	rmdir /s /q build dist
	del *.spec
