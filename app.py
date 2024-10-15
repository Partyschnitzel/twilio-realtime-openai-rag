import logging
import uvicorn
import os
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from routers.stream import stream_router

# Load environment variables from a .env file
load_dotenv()

# Get the PORT value from environment variables, defaulting to 5000 if not found
PORT = int(os.getenv("PORT", 5000))

app = FastAPI()

router = APIRouter()

# Include the router from the 'stream' module, which handles specific routes
router.include_router(stream_router)

app.include_router(router)

if __name__ == "__main__":
    try:
        # Start the Uvicorn server with the FastAPI app, running on the specified port
        uvicorn.run(app, host="0.0.0.0", port=PORT)
    except Exception as error:
        # Log the error in case the server fails to start
        logging.error(f"Error: {error}")
        raise error
