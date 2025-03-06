FROM python:3.10-bookworm
WORKDIR /hema-docker

RUN python3 -m pip install --upgrade pip
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt


COPY . .

CMD ["python", "-m", "flask", "--app", "predict.py",  "run", "--host=0.0.0.0"]
