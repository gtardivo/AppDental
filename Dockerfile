# Date: 2021-09-01 11:00:00
FROM python:3.8.5-alpine3.12

ARG build_date
ARG vcs_ref
ARG versao
ARG BOM_PATH="/docker/bom"

LABEL \
    org.label-schema.maintainer="Guilherme Tardivo Pulzatto" \
    org.label-schema.url="https://github" \
    org.label-schema.name="" \
    org.label-schema.license="COPYRIGHT" \
    org.label-schema.version="$versao" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.dockerfile="${BOM_PATH}/Dockerfile"

ENV \
    VERSAO=$versao

RUN apk del python3 && \
    apk update && apk add --virtual .build-dependencies \
    --no-cache \
    build-base==0.5-r1 \
    linux-headers==4.19.36-r0 \
    pcre-dev==8.43-r0 \
    bash==5.0.0-r0 \
    git==2.22.0-r0 \
    openssh==8.1_p1-r0 \
    python3-dev==3.8.5-r0

ENV DJANGO_SUPERUSER_PASSWORD=e4545c16-0768-11ed-b939-0242ac120002
ENV DJANGO_SUPERUSER_EMAIL=guitardivo@hotmail.com.br
ENV DJANGO_SUPERUSER_USERNAME=guitardivo

WORKDIR /AppDental

COPY . /AppDental

RUN wget --quiet --output-document=/etc/pip.conf http://binarios.intranet.bb.com.br/artifactory/generic-bb-binarios-aic-local/publico/pip/pip.conf && \
    pip install --no-cache-dir --upgrade pip==22.3 && \
    pip install -e . --no-cache-dir && \
    chmod +x /AppDental/symbolic_link_python.sh && ./symbolic_link_python.sh && \
    python AppDental/manage.py migrate && \
    python AppDental/manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

EXPOSE 8000

CMD ["python", "AppDental/manage.py", "runserver", "0.0.0.0:8000"]
