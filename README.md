# Hackathon Django 풀스택 스타터

프론트엔드(Django 템플릿)와 백엔드(Django REST Framework)를 한 번에 개발할 수 있도록 구성된 기본 템플릿입니다.

## 구성 요소
- Django 5.x
- Django REST Framework & drf-spectacular (OpenAPI 문서)
- django-cors-headers (외부 프론트엔드 연동)
- django-environ (환경 변수 관리)
- Whitenoise (정적 파일 서비스)
- Debug Toolbar (개발 편의)

## 시작하기
1. 가상환경 생성 및 활성화
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. 필요한 라이브러리 설치
   ```powershell
   pip install -r requirements.txt
   ```

3. 환경 변수 설정  
   `env.example` 파일을 복사하여 `.env` 파일로 저장하고 값을 원하는 대로 수정합니다.
   ```powershell
   copy env.example .env
   ```

4. 데이터베이스 마이그레이션
   ```powershell
   python manage.py migrate
   ```

5. 관리자 계정 생성(선택)
   ```powershell
   python manage.py createsuperuser
   ```

6. 개발 서버 실행
   ```powershell
   python manage.py runserver
   ```

7. 테스트 실행
   ```powershell
   python manage.py test
   ```

## 프로젝트 구조
```
├── api/                # REST API 앱 (예시 모델/시리얼라이저/테스트 포함)
├── frontend/           # Django 템플릿 기반 프론트엔드 앱
├── config/             # 프로젝트 전역 설정
├── static/             # 정적 파일 (CSS/JS 등)
├── templates/          # 베이스 및 프론트엔드 템플릿
├── manage.py
├── requirements.txt
├── env.example
└── README.md
```

## 추가 Tip
- 외부 프론트엔드(React/Vue 등)와 연동 시 `CORS_ALLOWED_ORIGINS` 값을 업데이트하세요.
- PostgreSQL 사용 시 `.env`에 `DATABASE_URL` 값을 입력하면 자동으로 연결됩니다.
- 배포 환경에서는 `DEBUG=False`, `ALLOWED_HOSTS`, `SECRET_KEY`를 반드시 재설정하세요.

