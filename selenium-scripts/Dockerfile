FROM python:rc

# blocker
# still trying to run chromedriver inside the container

# RUN apt-get update && apt-get install -y \
#         firefox-esr \
#         chromium \
#         chromium-browser \
#         xvfb \
#         xsel \
#         unzip \
#         libncurses5 \
#         libxml2-dev \
#         libxslt-dev \
#         libz-dev \
#         libglib2.0-0 \
#         libnss3 \
#         libfontconfig1 \
#         xclip

# # GeckoDriver v0.19.1
# RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz" -O /tmp/geckodriver.tgz \
#     && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
#     && rm /tmp/geckodriver.tgz

# # chromeDriver v2.35
# RUN wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/bin/ \
#     && rm /tmp/chromedriver.zip

# # xvfb - X server display
# ADD xvfb-chromium /usr/bin/xvfb-chromium
# RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
#     && chmod 777 /usr/bin/xvfb-chromium

# # create symlinks to chromedriver and geckodriver (to the PATH)
# RUN ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
#     && chmod 777 /usr/bin/geckodriver \
#     && chmod 777 /usr/bin/chromium-browser

COPY . /app

WORKDIR /app

RUN python -m pip install \
        selenium
