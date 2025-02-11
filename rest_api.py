from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Define request model
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

rest_api = FastAPI()

# Enable CORS
rest_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@rest_api.post("/calculate")
async def calculate(request: CalculationRequest):  
    if request.operation == 'add':
        result = request.num1 + request.num2
    elif request.operation == 'subtract':
        result = request.num1 - request.num2
    elif request.operation == 'multiply':
        result = request.num1 * request.num2
    elif request.operation == 'divide':
        if request.num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = request.num1 / request.num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(rest_api, host="0.0.0.0", port=5000, reload=True)
