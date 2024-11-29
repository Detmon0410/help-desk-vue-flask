# Step 1: Use the official Node.js image as a base
FROM node:16

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json into the working directory
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the entire project into the working directory
COPY . .

# Step 6: Expose the development server port (default is 5173 for Vite or 8080 for Vue CLI)
EXPOSE 8080

# Step 7: Run the development server
CMD ["npm", "run", "serve"]
