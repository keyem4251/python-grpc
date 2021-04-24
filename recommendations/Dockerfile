FROM python:3.9-buster

RUN mkdir /service
COPY protobufs /service/protobufs
COPY recommendations /service/recommendations
WORKDIR /service/recommendations
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN ./pb_gen.sh

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
