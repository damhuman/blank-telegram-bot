FROM nginx:1.19.2-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/certs
COPY localhost.crt /etc/nginx/certs
COPY localhost.key /etc/nginx/certs
COPY nginx.dev.conf /etc/nginx/conf.d