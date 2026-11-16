# 1. Start vanaf een lichtgewicht en veilig Alpine Linux base-image
FROM alpine:3.20

# 2. Installeer lighttpd zonder cache en maak de webroot-map klaar
RUN apk add --no-cache lighttpd \
    && mkdir -p /var/www/html \
    && chown -R lighttpd:lighttpd /var/www/html /var/log/lighttpd

# 3. Kopieer je eigen configuratie en webpagina naar de juiste mappen
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY index.html /var/www/html/index.html

# 4. Draai de webserver als non-root gebruiker voor extra veiligheid
USER lighttpd

# 5. Geef aan dat de container luistert op poort 8080
EXPOSE 8080

# 6. Start lighttpd op de voorgrond (-D) zodat de container actief blijft
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]