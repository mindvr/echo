# echo

A simple HTTP echo server that returns information about the received requests.

## Running with Docker

### Build the Docker image
```bash
docker build -t echo-server .
```

### Run the container
```bash
docker run -p 8080:8080 --rm echo-server
```

The server will be accessible at http://localhost:8080

## Running without Docker

```bash
python src/echo.py
```

The server will be accessible at http://localhost:8080
