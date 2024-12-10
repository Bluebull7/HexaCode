# Use the official Node.js image for building
FROM node:20 as build

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN yarn build

# Use a lightweight web server to serve the static files
FROM nginx:alpine

# Copy the React build files to the Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port Nginx runs on
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
