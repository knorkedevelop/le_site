FROM python:3.9.1

WORKDIR /code

COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN chmod u+x run.sh
EXPOSE 5000


CMD ["./run.sh"]