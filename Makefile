# tools
PYUIC 		= pyuic5.exe
PYINSTALL	= pyinstaller.exe

RM 			= rm
MV 			= mv

# Flags
PYINSTALL_FLAGS = -Fw

# FILES
PYINSTALL_FILES  = main.py
PYINSTALL_FILES += ./mgf_qt_ui/ui_py/$(MGF_MAIN).py

# MGF_MAIN
MGF_MAIN = mgf_main

uic:
	$(PYUIC) -o ./mgf_qt_ui/ui_py/$(MGF_MAIN).py ./mgf_qt_ui/ui_xml/$(MGF_MAIN).ui

pack:
	$(PYINSTALL) $(PYINSTALL_FLAGS) $(PYINSTALL_FILES)

clean:
	rm -rf ./dist ./build ./main.spec ./__pycache__

