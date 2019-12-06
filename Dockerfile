WORKDIR /app
COPY . /app
COPY /templates/home.html /app/templates/home.html
RUN pip3 --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
COPY /templates/home.html /app/templates/home.html
