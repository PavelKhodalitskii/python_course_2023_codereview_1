from python:3.10.12

RUN apt-get update

WORKDIR ..
RUN python3 -m venv venv
RUN source venv/bin/activate
ADD python_course_2023_codereview_1 .
RUN pip install --no-cache -r python_course_2023_codereview_1/requirements.txt

WORKDIR python_course_2023_codereview_1
EXPOSE 8000

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate
    python3 manage.py runserver 8000