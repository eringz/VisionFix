from fastapi import FastAPI
from app.routers import user_router, product_router
from app.db.Database import Base, engine
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv() # Load environment from .env

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Logic: Create database tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    yield # The application runs while yielding
    # Shutdown Logic can go here if needed (e.g., cleanup tasks)
    print("Shutting down application...")

# Initialize the FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

# Include the routers
app.include_router(user_router)
app.include_router(product_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Vission API my guest Ron Santos!"}

# The following code block ensures the app runs correctly in a container
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


