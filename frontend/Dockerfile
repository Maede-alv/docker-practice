# Step 1: Use Node.js official image to build the app
FROM node:16 AS build

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the package.json and package-lock.json to install dependencies
COPY ./package*.json ./

# Step 4: Install dependencies inside the container
RUN npm install

# Step 5: Copy the rest of the frontend files to the container
COPY . .

# Step 6: Build the React app
RUN npm run build

# Step 7: Use nginx to serve the built app
FROM nginx:alpine

# Step 8: Copy the built React app from the build stage to nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 to serve the app
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
