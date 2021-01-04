FROM nginx:1.19.0

COPY . /etc/nginx/
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf

VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/var/log/nginx", "/var/www"]

WORKDIR /etc/nginx/

CMD ["nginx"]

EXPOSE 80