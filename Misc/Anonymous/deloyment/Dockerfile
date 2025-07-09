FROM php:8.2-apache

RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libonig-dev \
    && docker-php-ext-install dom \
    && rm -rf /var/lib/apt/lists/*
    
RUN a2enmod rewrite

RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/2 /var/log/apache2/error.log

RUN mkdir -p /var/www/join /var/www/anonupload.cyberquest/uploads && \
    chown -R www-data:www-data /var/www && \
    chmod -R 755 /var/www && \
    chmod -R 777 /var/www/anonupload.cyberquest/uploads

COPY configs/000-default.conf /etc/apache2/sites-available/000-default.conf

COPY chall/join /var/www/join
COPY chall/anonupload/. /var/www/anonupload.cyberquest/

COPY flag.txt /fl444g_11d854d6a9c9341e8af155128bf74362.txt
RUN chmod 644 /fl444g_11d854d6a9c9341e8af155128bf74362.txt

RUN chown -R www-data:www-data /var/www/anonupload.cyberquest && \
    chmod -R 777 /var/www/anonupload.cyberquest/uploads

WORKDIR /var/www

CMD ["apache2-foreground"]
