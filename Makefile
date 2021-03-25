.PHONY:	upgrade_setuptools init init_dev test test_verbose my_dish settings help
.SILENT: my_dish

upgrade_setuptools:
	pip install --upgrade setuptools

init: upgrade_setuptools
	pip install --user --requirement requirements.txt

init_dev: upgrade_setuptools
	pip install --user --requirement requirements_dev.txt

test:
	python -m unittest discover --start-directory tests

test_verbose:
	python -m unittest discover --start-directory tests --verbose

my_dish:
	python ./src/shop_for_ingredients.py

settings:
	@echo "HOME             =" ${HOME}
	@echo "SHELL            =" ${SHELL}

help:
	@echo "Targets:"
	@echo "-----------------------------------------------------------------------------"
	@echo "  my_dish                     - executes the main program"
	@echo "-----------------------------------------------------------------------------"
	@echo "  init                        - pip install required packages"
	@echo "  init_dev                    - pip installs required development packages"
	@echo "-----------------------------------------------------------------------------"
	@echo "  init3                       - pip3 installs required packages using pip"
	@echo "  init_dev3                   - pip3 installs required development packages"
	@echo "-----------------------------------------------------------------------------"
	@echo "  test                        - runs test"
	@echo "  test_verbose                - runs test with verbose messaging"
	@echo "-----------------------------------------------------------------------------"
	@echo "  settings                    - outputs current settings"
	@echo "  help                        - outputs this info"
