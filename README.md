# Overview
네이버 웹툰 어플리케이션 주요 기능의 요구사항을 분석하여 만든 webtoon API 입니다

# Features
- 웹툰은 요일별 연재작 목록으로 조회할 수 있다 
- 웹툰은 제목 또는 작가명으로 필터링할 수 있다
- 웹툰 회차 목록에서는 최신 등록한 날짜 순으로 정렬한다
<br/>

- 웹툰 회차별 댓글 목록을 조회할 수 있다
- 댓글은 댓글을 등록한 사람고 연결되어 있다
- 인증된 사용자만이 댓글을 등록할 수 있다
- 해당 댓글을 등록한 사람만 삭제할 수 있다
- 인증되지 않은 요청에는 '읽기 전용' 권한으로 동작한다
<br/>

- 관심 웹툰은 관심 웹툰을 등록한 사람과 연결되어 있다
- 인증된 사용자만이 관심 웹툰을 등록할 수 있다
- 관심 웹툰을 등록한 사용자만이 관심 목록을 삭제할 수 있다
- 인증되지 않은 요청에느 모든 권한이 없다

# Tech Stack
- Language : python 3.9.4
- web framework : Django 3.2, Djangorestframework 3.12.4
- database : PostgreSQL 
- API : Restful API
- Docs : Swagger
- web server : Nginx 1.18.0
- web application server : gunicorn 20.1.0
- Hosting : AWS EC2

# 개발 환경 및 개발 기간
- OS : MacOS
- IDE : Visual Studio Code 1.55.1
- 개발기간 : 2021-05-03 ~ 2021-05-07

# API List 
![스크린샷 2021-05-27 오후 6 27 08](https://user-images.githubusercontent.com/80886445/119802235-58cf4b80-bf19-11eb-82b4-94c6144dfb4b.png)

# DB ERD 
![webtoon_db_visualized_v1](https://user-images.githubusercontent.com/80886445/119801643-e0688a80-bf18-11eb-90a9-a5c89bfc2316.png)


(추후 업데이트 예정)
