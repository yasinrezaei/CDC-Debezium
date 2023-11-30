#!/bin/bash

cd /app/config_and_test

#Install python requirements
echo 'Install python requirements'
pip install -r requirements.txt


# Run config and test files
python3 config.py
python3 fake_data_generator.py

sleep 5
python3 stream_processor.py


# wait for all background processes to finish!
wait



