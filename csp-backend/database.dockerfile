FROM postgres:14.1-bullseye
RUN 
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]