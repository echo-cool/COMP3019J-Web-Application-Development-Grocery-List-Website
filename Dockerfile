# This file is a template, and might need editing before it works on your project.
FROM python:3.9

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        sqlite3 \
#    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN #pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

# Run Flask
EXPOSE 5000
CMD ["python", "run.py"]

# For some other command
# CMD ["python", "app.py"]
