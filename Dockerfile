from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
COPY /templates/home.html /app/templates/home.html
