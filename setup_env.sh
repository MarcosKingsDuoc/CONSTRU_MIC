#!/bin/bash

# Name of the virtual environment
VENV_DIR="venv"

# Create the virtual environment
python3 -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install the dependencies from the requirements.txt file
pip install -r requirements.txt

echo "Virtual environment created and dependencies installed. Virtual environment is active."