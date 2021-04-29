FROM golang:1.16-buster

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY auth/ /service/auth/
WORKDIR /service/auth

SHELL ["/bin/bash", "-c"]
RUN apt update && apt install -y protobuf-compiler

RUN go mod download
RUN go get google.golang.org/protobuf/cmd/protoc-gen-go \
         google.golang.org/grpc/cmd/protoc-gen-go-grpc
RUN ./pb_gen.sh

RUN go build -o main main.go

EXPOSE 50052

ENTRYPOINT [ "./main" ]
