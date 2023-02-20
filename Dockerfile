FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /cargo_app
COPY requirements.txt ./cargo_app/
RUN pip install --upgrade pip && pip install -r cargo_app/requirements.txt
COPY . ./cargo_app/