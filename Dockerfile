# 1. Start with a lightweight Python image
FROM python:3.14-slim

# 2. Set the working directory inside the container WORKDIR /app

# 3. Copy only the requirements file first (to cache dependencies)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of yout project files into the container
COPY . .

# 6. Set the entrypoint so the container acts like the CLI
ENTRYPOINT ["python", "main.py"]
