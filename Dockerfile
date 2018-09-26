FROM python:3.7.0
COPY requirements /requirements
COPY src /src
CMD ["pip", "install -e ."]
