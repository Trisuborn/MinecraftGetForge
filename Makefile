
# tools
ifeq ($(OS),Windows_NT)
	PYUIC 		= pyuic5.exe
	PYINSTALL	= pyinstaller.exe
	RD 			= rd
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

ifeq ($(OS),Windows_NT)
MAIN_EXE = main.exe
MGF_EXE  = MinecraftGetForge.exe
else
MAIN_EXE = main
MGF_EXE  = MinecraftGetForge
endif

all: $(MGF_EXE)
$(MGF_EXE): uic pack cp
uic:
	$(PYUIC) -o ./mgf_qt_ui/ui_py/$(MGF_MAIN).py ./mgf_qt_ui/ui_xml/$(MGF_MAIN).ui
pack:
	$(PYINSTALL) $(PYINSTALL_FLAGS) $(PYINSTALL_FILES)
cp:
	cp ./dist/$(MAIN_EXE) ./$(MGF_EXE)

clean:
ifeq ($(OS),Windows_NT)
	$(RM) /q /f main.spec *.exe
	$(RD) /q /s dist build
else
	$(RM) -rf ./out/* ./dist ./build ./main.spec ./__pycache__ ./mgf_qt_ui/ui_py/mgf_main.py
endif
