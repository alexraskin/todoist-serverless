FROM public.ecr.aws/lambda/python:3.7

COPY lambda_function.py   ./
CMD ["lambda_function.lambda_handler"]