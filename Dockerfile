FROM python:3.9.21-alpine3.21

WORKDIR /evo2-api

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]