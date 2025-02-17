FROM nginx:1.19-alpine

RUN chown -R nginx:nginx /var/cache/nginx /etc/nginx /var/www/html

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

COPY . .

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
