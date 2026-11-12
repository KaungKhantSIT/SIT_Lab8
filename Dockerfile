FROM python:3.11-slim

WORKDIR /app

COPY inventory.py product.py shipping.py inventory_manager.py inventory.json /app/

CMD ["python", "inventory_manager.py"]