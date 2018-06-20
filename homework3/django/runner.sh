docker build -t python-django .
docker run --rm --name python-django -p 8000:8000 -v "$(pwd)/src:/src" python-django
