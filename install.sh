#!/bin/bash

# Install dependencies
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt

echo "Installation complete. Run the tool using: python3 seeker.py"