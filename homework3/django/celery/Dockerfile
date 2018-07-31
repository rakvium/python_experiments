FROM python:3.6.4

ADD ./ /code

WORKDIR /code
RUN pip install -r /code/requirements.txt

# add alias for ls -la
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

CMD ["celery", "worker", "-A", "app:app", "-l", "info", "-c", "4"]
