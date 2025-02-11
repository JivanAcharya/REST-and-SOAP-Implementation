# SOAP and REST Calculator API
An implementation of both SOAP and REST API architectures with a simple calculator. Provides basic mathematical operations through separate endpoints along with request and response preview.
  ![Screenshot from 2025-02-11 17-21-43](https://github.com/user-attachments/assets/e5fef002-a9d9-42e6-b897-b6d55b01d582)![Screenshot from 2025-02-11 17-29-39](https://github.com/user-attachments/assets/1f28c4e4-543b-468e-bfd7-a8688eb17fa6)

## Features
- REST API (FastAPI)
- SOAP API (Spyne/Flask) 
- Basic math operations (add, subtract, multiply, divide)
- Request/Response preview

## Prerequisites
- Python 3.11+
- Virtual environment

## Quick Start
```bash
# Clone repository
git clone https://github.com/JivanAcharya/REST-and-SOAP-Implementation.git
cd REST-and-SOAP-Implementation

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start REST API server (port 5000)
python rest_api.py

# Start SOAP API server (port 5001) 
python soap_api.py
