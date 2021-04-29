package main

import (
	"context"
	pb "keyem4251/try-grpc-microservice-inventory/pb"
	"log"
	"net"

	empty "github.com/golang/protobuf/ptypes/empty"

	"google.golang.org/grpc"
)

const (
	port = ":50052"
)

type server struct {
	pb.UnimplementedInventoryServer
}

func (s *server) List(ctx context.Context, in *empty.Empty) (*pb.BookList, error) {
	books := []*pb.Book{
		{Name: "Onepieace"},
		{Name: "Naruto"},
	}
	return &pb.BookList{Books: books}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterInventoryServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
