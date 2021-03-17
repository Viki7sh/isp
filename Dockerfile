FROM python:3.8

ENV TARGET /usr/src/app/

RUN mkdir -p "${TARGET}" 

WORKDIR "${TARGET}"

COPY lab1.py "${TARGET}"

CMD ["python3","lab1.py"]
