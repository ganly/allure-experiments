FROM openjdk:8-jdk-slim
LABEL maintainer="Steve Ganly"


ARG RELEASE=2.12.1
ARG ALLURE_REPO=https://dl.bintray.com/qameta/maven/io/qameta/allure/allure-commandline

RUN apt-get update -y
RUN apt-get install wget unzip -y


RUN wget --no-verbose -O /tmp/allure.zip $ALLURE_REPO/$RELEASE/allure-commandline-$RELEASE.zip \
  && unzip /tmp/allure.zip -d / \
  && rm -rf /tmp/allure.zip \
  && ln -s /allure-$RELEASE /allure \
  && ln -s /allure-$RELEASE/bin/allure /bin/allure
