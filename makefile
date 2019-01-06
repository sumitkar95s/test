SHELL = /bin/sh
INTERPRETER = python
FILE = Invoker.py
restApi:
	make install_packages
	make update_code
	make execute
	make clean
install_packages:
	pip install -r packages.txt
execute:
	${INTERPRETER} ${FILE}
clean:
	-rm -f *.pyc
update_code:
	git pull
