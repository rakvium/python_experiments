docker build -t python-test .
docker run --rm --name python-test -v "$(pwd)/src:/src" python-test
