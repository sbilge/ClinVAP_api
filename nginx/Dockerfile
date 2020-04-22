FROM nginx

LABEL author="bilge.sueruen@uni-tuebingen.de" \
    description="Docker image to start web server for flask application"


# remove efault configuration
RUN rm /etc/nginx/conf.d/default.conf

# replace with custom configuration
COPY nginx.conf /etc/nginx/conf.d/