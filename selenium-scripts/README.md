Run the Selenium standalone chrome as a daemon service

`docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome`

---

Build the Docker image (image name: 'selchrompy'):

`docker build -t selchrompy .`

Create the container and run the scripts inside the container:

`docker run --rm -v <your workspace>/selenium-test-basic:/app selchrompy python /app/app.py`

Example:

`docker run --rm -v ~/Workspace/astronaut_research/simulate-concurrent/selenium-scripts:/app selchrompy python /app/app.py`

---

<!-- 
need to figure out how to run as a docker compose
`docker-compose up --build --abort-on-container-exit` 
-->