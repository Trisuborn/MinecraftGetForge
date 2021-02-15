
# tools
ifeq ($(OS),Windows_NT)
	PYUIC 		= pyuic5.exe
	PYINSTALL	= pyinstaller.exe
	RM 			= del
else
	PYUIC 		= pyuic5
	PYINSTALL	= pyinstaller
	RM 			= rm
endif


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
ifeq ($(OS),Windows_NT)
	$(RM) /q /f /s dist
	$(RM) /q /f /s __pycache__
	$(RM) /q /f /s build
	$(RM) /q /f /s main.spec
	$(RM) .\mgf_qt_ui\ui_py\mgf_main.py
else
	$(RM) -rf ./dist ./build ./main.spec ./__pycache__ ./mgf_qt_ui/ui_py/mgf_main.py
endif
