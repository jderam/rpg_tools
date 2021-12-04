SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

wheel:
	@python setup.py sdist bdist_wheel

install:
	@pip install dist/rpg_tools-*-py3-none-any.whl --force-reinstall
