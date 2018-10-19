FROM arm32v7/python:3.7-stretch

# install vim <3
RUN apt-get update && apt-get install -y vim 

# Timezone stuff
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# force stdout and stderror to be unbuffered
ENV PYTHONUNBUFFERED 1

# prepare code folder
RUN mkdir /code
WORKDIR /code

# install needed modules
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
