FROM python:3.10.6
WORKDIR /app
COPY . /app/
RUN pip install -r /app/requirements.txt
CMD ["python", "main.py"]