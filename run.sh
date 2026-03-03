#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Setup done! Fill in .env dulu, lalu jalankan: python seller.py"
