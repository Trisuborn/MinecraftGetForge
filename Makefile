# tools
PYUIC 	= pyuic5.exe

# MGF_MAIN
MGF_MAIN = mgf_main

all:
	$(PYUIC) -o ./mgf_qt_ui/ui_py/$(MGF_MAIN).py ./mgf_qt_ui/ui_xml/$(MGF_MAIN).ui
