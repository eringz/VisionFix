# Use officaal Node.js image from Docker Hub
FROM node:20

WORKDIR /app

COPY ./frontend/package.json /app/package.json
COPY ./frontend/package-lock.json /app/package-lock.json

# Install dependencies 
RUN npm install

# Copy the rest of the application code into the container
COPY ./frontend /app/

# Expose the development server port
EXPOSE 3000

# Start the Next.js development serveer
CMD ["npm", "run", "dev"]

