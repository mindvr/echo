FROM python:3-slim

WORKDIR /app

COPY src/ /app/src/

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "src/echo.py"]