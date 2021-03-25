.PHONY:	init init_dev init init3 test settings help

init:
	pip install --upgrade setuptools
	pip install --user -r requirements.txt

init_dev:	init
	pip install --user -r requirements_dev.txt

init3:
	pip3 install --upgrade setuptools
	pip3 install --user -r requirements.txt

init_dev3:	init3
	pip3 install --user -r requirements_dev.txt

test:
	python -m unittest discover -s tests
# py.test tests

settings:
	@echo "HOME             =" ${HOME}
	@echo "SHELL            =" ${SHELL}

help:
	@echo "Targets:"
	@echo "  init           - pip install required packages"
	@echo "  init_dev       - pip installs required development packages"
	@echo "  init           - pip3 installs required packages using pip"
	@echo "  init_dev       - pip3 installs required development packages"
	@echo "  test           - runs test"
	@echo "  settings       - outputs current settings"
	@echo "  help           - outputs this info"
