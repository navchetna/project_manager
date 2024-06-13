FROM node:18-alpine 

WORKDIR /app/prisma

COPY ./schema.prisma .

RUN npm install prisma --save-dev

RUN npm init -y

RUN npx prisma generate

CMD ["sh", "-c", "npx prisma db push --schema='./schema.prisma' && npx prisma studio" ]
