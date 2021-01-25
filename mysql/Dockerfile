FROM mysql:5.7

EXPOSE 3306

VOLUME /var/lib/mysql
COPY ./my.cnf /etc/mysql/conf.d/my.cnf

# ENV MYSQL_DATABASE 'management'
# ENV MYSQL_USER 'user'
# ENV MYSQL_PASSWORD 'selfmanagement1234'
# ENV MYSQL_ALLOW_EMPTY_PASSWORD 'yes'

CMD ["mysqld"]