cmd = python
dir_hw = src
dir_check = tools

all:
	
lab01:
	$(cmd) ./$(dir_check)/chk_$@.py

