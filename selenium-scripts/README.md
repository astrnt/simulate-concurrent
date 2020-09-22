Build the Docker image (image name: 'rp'):
`docker build -t rp .`

Create the container and run the scripts inside the container:
`docker run --rm -v <your workspace>/selenium-test-basic:/app rp python /app/app.py`

Example:
`docker run --rm -v ~/Workspace/astronaut_research/simulate-concurrent/selenium-scripts:/app rp python /app/app.py`