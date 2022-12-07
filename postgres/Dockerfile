FROM postgres:12

# proxy information
#ENV proxy_host genproxy.corp.amdocs.com
#ENV proxy_port 8080

# system configuration
#ENV http_proxy http://$proxy_host:$proxy_port
#ENV https_proxy $http_proxy
#ENV HTTP_PROXY $http_proxy
#ENV HTTPS_PROXY $http_proxy

#POSTGRES SETUP
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_HOST_AUTH_METHOD trust
ENV POSTGRES_DB flask_mega

EXPOSE 5432
