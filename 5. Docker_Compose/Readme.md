# Docker Compose란?

<hr/>

Docker compose란 여러개의 여러 개의 컨테이너로부터 이루어진 서비스를 구축, 실행하는 순서를 자동으로 하여, 관리하기 위한 도구입니다.

이러한 Docker Compose를 사용하기 위해서는 각 컨테이너에 대한 Dockerfile과 Docker-compose.yml 파일이 필요합니다.

먼저 아래와 같이 2개의 Dockerfile을 준비합니다.

1번 backend의 Dockerfile 
~~~
    FROM node:alpine

    WORKDIR /app

    COPY ./package.json ./

    RUN npm install

    COPY . .

    CMD ["npm","run","start"]
~~~

2번 frontend의 Dockerfile 
~~~
    FROM node:16-alpine as builder

    WORKDIR /app

    COPY package.json ./

    RUN npm install

    COPY ./ ./

    RUN npm run build

    FROM nginx
    EXPOSE 3000
    COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
    COPY --from=builder /app/build /usr/share/nginx/html
~~~

이제 각각의 도커파일을 한번에 컨테어너로 관리할 수 있는 Docker-compose.yml을 작성해 보겠습니다.

아래와 같이 다양한 설정들을 Docker-compose.yml에 작성해주면 미리 작성한 Dockerfile과 연동하여 자동으로 컨테이너들을 관리해줍니다.
~~~
    version: "2.4"   <= docker compose의 버전
    services:
        frontend:
            image: "heohyoyeong/docker-frontend" <= docker hub에서 사전에 제작한 image를 호출해서 사용
            volumes:  <= docker volume에 대한 명령어도 작성
                - /app/node_modules
                - ./frontend:/app
            stdin_open: true

        backend:
            image: "heohyoyeong/docker-backend"
            container_name: app_backend <= 컨테이너에 대한 이름 명시
            volumes:
                - /app/node_modules
                - ./backend:/app
            environment:  <= 사용할 환경변수에 대한 설정
                MYSQL_HOST: docker-fullstack-mysql.cqxxqploz0kp.us-west-2.rds.amazonaws.com
                MYSQL_USER: root 
                MYSQL_ROOT_PASSWORD: heohyoyeong1993
                MYSQL_DATABASE: myapp
                MYSQL_PORT: 3306   
~~~

