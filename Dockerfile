FROM postgres:alpine

COPY init.sql /docker-entrypoint-initdb.d
COPY insert.sql /docker-entrypoint-initdb.d