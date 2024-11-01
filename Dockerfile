FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

ADD odbcinst.ini /etc/

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends curl gnupg unixodbc unixodbc-dev tdsodbc freetds-common freetds-bin freetds-dev \
    postgresql python3-scipy python3-numpy python3-pandas && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools msodbcsql17 && \
    # Añadir mssql-tools al PATH de forma global
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> /etc/bash.bashrc && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> /etc/environment && \
    # Limpiar caché de apt para reducir tamaño de imagen
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir mssql-django
RUN mkdir /code

COPY . /code/
COPY ./requirements.txt /code/

WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080