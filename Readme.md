# SOAP and REST Calculator API

A dual-implementation calculator service demonstrating both SOAP and REST API architectures. Provides basic mathematical operations through separate endpoints.

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
git clone <repository-url>
cd SOAP-and-REST

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start REST API server (port 5000)
python rest_api.py

# Start SOAP API server (port 5001) 
python soap_api.py