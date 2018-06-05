docker build -t python-test .
docker run -v "$(pwd)/src:/src" python-test
