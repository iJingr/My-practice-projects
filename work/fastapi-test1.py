from imp import reload

from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get('/')
async def read_root() -> Dict:
    return {'message' : 'Hello World!'}

@app.get('/info')
async def get_info() -> Dict:
    return {
        "name": "Your Name",
        "role": "Student",
        "language": "Python 3.10"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
