FROM node:latest

WORKDIR /usr/app/

COPY ./package.json ./yarn.lock /usr/app/
COPY ./src/ /usr/app/src/
RUN yarn install
RUN yarn build

#CMD ["ls", "./build"]
CMD ["node", "./build/main.js"]
