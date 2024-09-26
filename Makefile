# Makefile for setting up and running the latency simulation project

# Set the name for the virtual environment
VENV_NAME=venv

# Create virtual environment and install dependencies
.PHONY: setup
setup:
	python3 -m venv $(VENV_NAME)
	./$(VENV_NAME)/bin/pip install --upgrade pip
	./$(VENV_NAME)/bin/pip install -r requirements.txt

# Run the latency simulation script
.PHONY: run
run:
	./$(VENV_NAME)/bin/python latency_simulation.py

# Clean up the virtual environment and results
.PHONY: clean
clean:
	rm -rf $(VENV_NAME) results
