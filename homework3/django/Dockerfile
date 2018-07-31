FROM python:3.6.4

EXPOSE 8000

ADD /src /backend
RUN pip install -r /backend/requirements.txt

WORKDIR /src
CMD ["python", "/backend/manage.py", "runserver", "0.0.0.0:8000"]
