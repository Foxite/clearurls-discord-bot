FROM python:3.10
WORKDIR /app
RUN useradd -m app && chown app:app /app
USER app:app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test.py .
COPY main.py .
RUN python test.py
RUN rm -rf /home/app/.cache
CMD ["python", "main.py"]
