FROM arm32v7/python:3.7-stretch

RUN pip3 install paho-mqtt

# Timezone stuff
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#CMD ["python3", "ble.py"]
CMD ["tail", "-f", "/dev/null"]
