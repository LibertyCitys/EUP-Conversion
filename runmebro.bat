@echo off
python -B -m converter.py
timeout /t 1 /nobreak >nul
