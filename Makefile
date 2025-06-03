.PHONY: venv install test clean

# Default target
all: test

# Create virtual environment
venv:
	python3 -m venv .venv
	@echo "Virtual environment created. Activate with 'source .venv/bin/activate'"

# Install dependencies
install: venv
	.venv/bin/pip install requests

# Run tests
test: install
	.venv/bin/python -m unittest discover -s tests

# Clean up
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .venv