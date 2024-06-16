import uvicorn

THIS_SERVICE_PATH = "0.0.0.0"
THIS_SERVICE_PORT = "9020"


def start():

    try:
        uvicorn.run(
            "yolo.service:app",
            host=THIS_SERVICE_PATH,
            port=int(THIS_SERVICE_PORT),
            reload=False)
    finally:
        print("stopping server:app...")


if __name__ == '__main__':
    start()
