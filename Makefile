build:
	mkdir -p build
	javac -d build src/*.java

run: build
	java -cp build HelloWorld

clean:
	rm -rf build
