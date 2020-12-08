FROM python:3

WORKDIR /src/

ADD status.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

ENTRYPOINT ["./status.py"]
