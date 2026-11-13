FROM python:3.14-slim

WORKDIR /app

COPY *.py inventory.json /app/

CMD ["python", "inventory_manager.py"]