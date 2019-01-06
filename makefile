SHELL = /bin/sh
INTERPRETER = python
FILE = Invoker.py
restApi:
	make install_packages
	make execute
	make clean
	make update_code
install_packages:
	pip install -r packages.txt
execute:
	${INTERPRETER} ${FILE}
clean:
	-rm -f *.
update_code:
	git pull
