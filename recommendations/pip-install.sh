#!/bin/sh

source venv/bin/activate

export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export CFLAGS="-I/opt/homebrew/opt/openssl/include"
export LDFLAGS="-L/opt/homebrew/opt/openssl/lib"

brew --prefix protobuf
brew --prefix openssl
brew --prefix zlib

python -m pip install --upgrade pip
python -m pip install -r requirements.txt