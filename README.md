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
- thumnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Like/Dislike

- User:FK
- Video:FK
- Video:Like/Dislike (1:N)

4. Comment

- User:FK
- Video:FK
- like
- dislike

5. Subscription

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

- 1일차: Project settings (Docker => Django, Github => Github Actions(CI))
- 2일차:
    - Project Settings (PostgreSQL)
    - 연결 하는 부분 작업 (DB 컨테이너 준비될 때까지 Django 커맨드 명령을 통해서 DB 연결 재시도)

### 3일차: Custom User Model

    - 왜 커스텀 유저 모델을 사용하는가?
        - 장고의 유저 모델을 상속받아서 기존에 구현된 기능을 내가 직접 구현하지 않아도 되기 때문에
        - 장고의 공식 문서에서 강력히 추천한다.
    - drf-sepectacular
    
#### (1) User Model 생성
(오전)
```
docker-compose run --rm app sh -c 'django-admin startapp users'
```
- django 에게 알려준다. settings.py
- UserModel 생성
- makemigrations => test 코드 실행

(오후)
- custom UserModel migrate => 디버깅
- custome UserAdmin 생성
- Swagger_API(API docs) => drf-spectacular

#### (2) Test Code를 작성
#### (3) AbstractUserModel 상속
#### (4) Admin 세팅