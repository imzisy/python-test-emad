FROM python:3
WORKDIR /usr/src/app
COPY . .
ADD start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]
