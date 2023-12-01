from python:3.10.12

RUN apt-get update

WORKDIR usr/src/code_review_1
COPY . .

RUN python3 -m venv venv
RUN pip install --no-cache -r requirements.txt

ENV PYTHONUNBUFFERED=1
# WORKDIR python_course_2023_codereview_1
EXPOSE 8000

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py runserver 0.0.0.0:8000