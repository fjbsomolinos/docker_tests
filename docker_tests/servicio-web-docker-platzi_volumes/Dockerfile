FROM python:3

WORKDIR /usr/src/app

ADD main.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /usr/src/app/Hitos
RUN mkdir /usr/src/data
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt

CMD [ "hug", "-p 8000", "-f", "main.py" ]

EXPOSE 8000
