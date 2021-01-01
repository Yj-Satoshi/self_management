FROM nginx:1.19.0

# RUN rm /etc/nginx/conf.d/default.conf
# COPY .nginx.conf /etc/nginx/conf.d/ && .nginx.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf

# VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/var/log/nginx", "/var/www"]

WORKDIR /etc/nginx/

CMD ["nginx"]

EXPOSE 80