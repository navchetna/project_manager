FROM node:18

WORKDIR /app/frontend/

COPY package.json /app/frontend/

RUN ls

RUN npm install --legacy-peer-deps

COPY . .

EXPOSE 5173

CMD [ "npm", "run", "dev", "--", "--host" ]