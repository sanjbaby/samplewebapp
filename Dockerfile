from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt 
CMD ["python","app.py"]
COPY app.py /app.py
COPY /templates/home.html /templates/home.html
