FROM public.ecr.aws/lambda/python:3.11

# Copy application code
COPY app/ /var/task/app/

# Copy requirements and install
COPY requirements.txt /var/task/
RUN pip install --no-cache-dir -r requirements.txt

# Set handler
CMD ["app.main.handler"]
