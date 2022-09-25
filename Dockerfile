FROM python:3

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD ["python3","src/app.py"]