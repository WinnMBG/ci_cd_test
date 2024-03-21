FROM ubuntu:latest

WORKDIR /home/user

RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip

RUN pip install flask

COPY app.py app.py

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "app.py", "run", "--host=0.0.0.0", "--port=5000"]

