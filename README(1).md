# YouTube 댓글 분석기

Streamlit과 YouTube Data API v3로 만든 멀티페이지 앱입니다.

## 기능

- 영상 정보 조회
- 썸네일 미리보기 및 저장
- 공개 댓글 수집
- 간단한 한국어·영어 키워드 감성 분석
- 자주 나온 단어와 댓글 좋아요 분포 확인
- 좋아요가 많은 댓글 정렬
- 분석 결과 CSV 저장

## 1. YouTube API 키 준비

Google Cloud Console에서 프로젝트를 만든 뒤 **YouTube Data API v3**를 사용 설정하고 API 키를 발급합니다.

## 2. 로컬 Secrets 설정

`.streamlit/secrets.toml.example`을 복사하여 `.streamlit/secrets.toml`을 만들고 다음처럼 입력합니다.

```toml
YOUTUBE_API_KEY = "본인의_API_키"
```

`secrets.toml`은 `.gitignore`에 포함되어 있으므로 GitHub에 올리지 마세요.

## 3. 설치와 실행

```bash
pip install -r requirements.txt
streamlit run main.py
```

## 4. Streamlit Community Cloud 배포

1. 이 프로젝트를 GitHub 저장소에 업로드합니다.
2. Streamlit Community Cloud에서 저장소와 `main.py`를 선택합니다.
3. 앱의 **Settings → Secrets**에 다음 내용을 저장합니다.

```toml
YOUTUBE_API_KEY = "본인의_API_키"
```

## 주의

- 댓글을 사용 중지한 영상, 비공개 영상, 삭제 영상은 댓글을 가져올 수 없습니다.
- API 할당량과 영상의 댓글 수에 따라 수집 가능한 양이 달라질 수 있습니다.
- 감성 분석은 가벼운 키워드 기반 분석이며 문맥을 완벽히 이해하는 AI 모델은 아닙니다.
