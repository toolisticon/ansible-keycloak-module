SRC_FILES = $(wildcard library/*.py)
TESTS = $(wildcard tests/test_*.py)
END2END_TESTS = $(wildcard tests/e2e_*.py)

default: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  help           to show this message"
	@echo "  lint           to run flake8 and pylint"
	@echo "  test           to run unit tests"

lint:
	pycodestyle --ignore=E402,E722 --max-line-length=160 library tests module_utils


.PHONY: test

build:
	@- $(foreach SRC_FILE,$(SRC_FILES), \
		python -m compileall $(SRC_FILE); \
		)

test:
	@- $(foreach TEST,$(TESTS), \
		echo === Running test: $(TEST); \
		pytest $(TEST)  --junitxml=build/reports/TESTS.xml; \
		)

end2end_test:
	@- $(foreach TEST,$(END2END_TESTS), \
		echo === Running end2end test: $(TEST); \
		python $(TEST); \
		)
