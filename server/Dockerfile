FROM python:3.10

WORKDIR /app/backend

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 3010

CMD [ "uvicorn", "main:app","--host", "0.0.0.0", "--port", "3010","--reload"]