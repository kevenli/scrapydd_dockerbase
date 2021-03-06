FROM python:3.8.1-alpine3.11

WORKDIR /scrapydd
RUN apk add libffi-dev \
    openssl-dev gcc libc-dev make libxml2-dev libxslt-dev \
    tzdata jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
ADD . /scrapydd_src
RUN pip install -r /scrapydd_src/requirements.txt