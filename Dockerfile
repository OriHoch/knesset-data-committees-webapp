FROM python:3.6.2-alpine

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5050

ENV WORKERS 4
ENV PORT 5050

ENTRYPOINT ["sh"]
CMD ["-c", "gunicorn -w ${WORKERS} -b :${PORT} main:app"]
