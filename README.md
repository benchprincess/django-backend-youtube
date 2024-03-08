# 유튜브 백엔드 구현

## 1. REST API

### (1) 모델 구조

1. User (Custom)

- email
- password
- nickname
- is_business(boolean): personal, business

2. Video

- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Like/Dislike (Reaction)

- User:FK
- Video:FK
  Video:Like/Dislike (1:N)

4. Comment

- User:FK
- Video:FK
- like
- dislike
- content

5. Subcription (채널 구독)

- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Notification

- User:FK
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)

- User:FK (nickname)

## 수업 진행

- 1일차:
  - Project Settings (Docker => Django, Github => Github Actions(CI))
- 2일차:

  - Project Settings (PostgreSQL)
  - 연결 하는 부분 작업 (DB 컨테이너가 준비될 때까지 Django 커맨드 명령을 통해서 DB 연결 재시도) - wait_for_db

## 3일차: Custom User Model

왜 커스텀 유저 모델을 사용하는가? - 장고의 유저 모델을 상속받아서 기존에 구현된 기능을 내가 직접 구현하지 않아도 되기 때문에. - 장고의 공식 문서에서 강력히 추천한다.
drf-sepectacular

##### (1) User Model 생성

(오전)

- docker-compose run --rm app sh -c 'django-admin startapp users'
- django에게 알려준다. settings.py
- UserModel 생성
- makemigrations => test코드 실행

(오후)

- custom UserModel migrate => 디버깅
- custom UserAdmin 생성
- Swagger-API(API docs) => drf-spetacular
- docker-compose run --rm app sh -c 'python manage.py makemigrations'
- docker-compose run --rm app sh -c 'python manage.py migrate'
- docker-compose up

##### (2) Test Code를 작성

##### (3) AbstractUserModel을 상속

##### (4) Admin 세팅

## 4일차: REST API -> Video 관련 API

(1) startapp을 통해서 각 모델별 app폴더 생성
1.Common
2.Videos
3.Comments
4.Reactions (좋아요,싫어요)
5.Subcriptions
6.Notifications

- docker-compose run --rm app sh -c 'python manage.py startapp common'
- docker-compose run --rm app sh -c 'python manage.py startapp videos'
- docker-compose run --rm app sh -c 'python manage.py startapp comments'
- docker-compose run --rm app sh -c 'python manage.py startapp reactions'
- docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
- docker-compose run --rm app sh -c 'python manage.py startapp notifications'

(2) Model정의

(3) settings.py의 INSTALLED_APPS에 등록

(4) DB migration

- docker-compose run --rm app sh -c 'python manage.py makemigrations'
- docker-compose run --rm app sh -c 'python manage.py migrate'

(5) Video API create
VideoList
api/v1/videos

- GET: 전체 비디오 목록 조회
- POST: 새로운 비디오 생성
- DELETE, PUT: X

VideoDetail
api/v1/videos/{video_id}

- GET: 특정 비디오 상세 조회
- POST: X
- PUT: 특정 비디오 정보 업데이트(수정)
- DELETE: 특정 비디오 삭제

urls.py 등록

(6)
(7)
api/v1/video
(1) 좋아요, 싫어요 데이터가 보이게끔 하는 게
(2) 전체 영상 데이터를 내려줄 때, 좋아요 싫어요 개수가 보이게 해줌

like/dislike count

- Reaction Model
- Video Model

(8) Chatting - SocketIO
- api/v1/char/msg
  - [POST]: 채팅 메시지 생성
- api/v1/chat/room
  - [POST]: 채팅방 생성
  - [GET]: 내가 접속해 있는 전체 채팅방 조회
- api/v1/chat/room/{room_id}
  - [GET]: 채팅방 조회
- wss:127.0.0.0.1:8000/ws/chat/{room_id}

1. Chat 모델 생성 startapp chat
- docker-compose run --rm app sh -c 'python manage.py startapp chat'

2. Django SocketIO 설치 -> Channels Library (pip install channels)
requiremnets.txt에 아래 문구 추가
channels>=4.0.0,<4.0.1

docker-compose build

- 채팅 소켓 연결
- 배포

(9) Deployment
- IAM 유저 생성
- EC2 instance 생성 (Amazone Linux) -> 프리티어
- EC2 SSH 접속 -> Finger Print
- AWS EC2
- git, docker-compose 설치 & build