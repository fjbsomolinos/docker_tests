FROM python:3

ENV PORT 80
WORKDIR /usr/src/app

ADD main.py data/hitos.json requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /usr/src/app/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt
EXPOSE $PORT

CMD hug -p $PORT -f main.py 
