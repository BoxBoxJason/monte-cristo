from fastapi import FastAPI
from routes.router import router

app = FastAPI()

# Include the graph router
app.include_router(router, prefix="/graph", tags=["Graph"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
