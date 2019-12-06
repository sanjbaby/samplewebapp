RUN pip install flask
RUN pip install pymysql 
CMD ["python","app.py"]
COPY app.py /app.py
COPY /templates/home.html /templates/home.html
