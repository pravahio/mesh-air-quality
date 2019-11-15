all: py js

py: *.proto
	mkdir -p build/py
	pip install grpcio-tools
	protoc -I=. --python_out=build/py air-quality.proto

js: *.proto
	mkdir -p build/js
	protoc -I=. --js_out=import_style=commonjs:build/js air-quality.proto

clean: 
	rm -rf build

.PHONY: py js clean

export:
	export PYTHONPATH=/Users/abhishek/Documents/SoketLabs/projects/protocols/mesh-air-quality/py:/Users/abhishek/Documents/SoketLabs/projects/cross-lang-mesh-rpc/py