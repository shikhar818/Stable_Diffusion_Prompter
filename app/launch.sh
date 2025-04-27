#!/bin/bash

echo "Activating the environment";

source  "$(conda info --base)/etc/profile.d/conda.sh"

conda activate ./env
echo "launching your app";
streamlit run interface.py
