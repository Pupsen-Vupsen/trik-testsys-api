FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
ENV PYTHONPATH="$PYTHONPATH:/api"
CMD [ "python3", "api/app.py" ]
