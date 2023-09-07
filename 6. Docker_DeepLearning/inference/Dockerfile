FROM heohyoyeong/tensor-gpu:1.0.0

# WORKDIR /usr/src

# COPY ./requirements.txt .

# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install -r requirements.txt

COPY . .

# VOLUME /var/lib/data

ENTRYPOINT ["python","inference.py"]