FROM ubuntu
RUN apt update && apt install -y vim python3 python3-pip

RUN mkdir /usr/share/application
COPY sse_basic /usr/share/application

WORKDIR /usr/share/application
RUN pip install -r requirements.txt

WORKDIR /usr/share/application/api
ENV API_NINJA_KEY $API_NINJA_KEY

CMD ["flask", "run", "--host", "0.0.0.0"]
