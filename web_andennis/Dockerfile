FROM nginx:1.25.1

RUN rm -rf /etc/nginx/conf.d/*

RUN mkdir -p /var/www/andennis/html
COPY index.html /var/www/andennis/html/index.html
COPY nginx_srv_andennis.conf /etc/nginx/conf.d/andennis.conf

STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]