from app import app
import uvicorn


def start():
    uvicorn.run(app, host= '0.0.0.0', port=8000)


if __name__ == "__main__":
    start()