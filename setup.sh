#!/bin/bash

# Print a message to indicate the start of the setup process
echo "Starting setup..."

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Print a message to indicate the end of the setup process
echo "Setup completed."