#!/bin/sh

GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
CFLAGS="-I/opt/homebrew/opt/openssl/include"
LDFLAGS="-L/opt/homebrew/opt/openssl/lib"

brew --prefix protobuf
brew --prefix openssl
brew --prefix zlib

source venv/bin/activate
python -m pip install -r requirements.txt