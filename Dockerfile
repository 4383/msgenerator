FROM python:3-onbuild
WORKDIR /usr/src/app/sources
CMD [ "python", "main.py", "--cpf", "test" ]
