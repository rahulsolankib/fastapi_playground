# Debugging and live reloading with docker-compose

## Steps

1. Run the app with debugging enabled using this command 
    ```
    python3 --Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    Note: This will just enable it, you also need to run debugger client in vscode to attach it to debug port exposed by the container.

2. Code to attach a debugger client in vscode.
    ```
    {
        "name": "Python Debugger: FastAPI Container Debug",
        "type": "debugpy",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": 5678
        },
        "pathMappings": [
            {
                "localRoot": "${workspaceFolder}/app",
                "remoteRoot": "/app"
            }
        ],
        "justMyCode": true
    }
    ```
3. 


