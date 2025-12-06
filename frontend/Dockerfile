# Usamos Node imagen ligera
FROM node:20-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 5173

# --host es necesario para exponerlo fuera del contenedor
CMD ["npm", "run", "dev", "--", "--host"]