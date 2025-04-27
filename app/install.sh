#!/bin/bash
echo "Setting Up Environment";
conda create --prefix ./env python=3.11  -y
echo "Activating the Environment";
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ./env
echo "Installing the required packages";
pip install -r requirements.txt
