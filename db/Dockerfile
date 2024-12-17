FROM postgres:15-alpine

# Set the environment variables for the database
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB test
# ... other configurations

#COPY init.sql /docker-entrypoint-initdb.d/init.sql

# Expose the port
EXPOSE 5432

# Define the command to start the database
CMD ["postgres"]
