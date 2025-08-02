#!/bin/bash

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Download SpaCy model
python -m spacy download en_core_web_sm
