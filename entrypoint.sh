#!/usr/bin/env bash
sleep 20
python database_manager.py db upgrade
python run.py
