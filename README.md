# python (자료구조, 백준, 클린코드)

## ⚙파이썬 환경설정
1. 파이썬 설치

Stable Release Version ex) 3.8

https://www.python.org/

2. pipenv 설치
```bash
# Windows
pip install pipenv

# Mac
brew install pipenv
```

3. 프로젝트 디렉토리에 가상환경 생성
```bash
# 프로젝트 디렉토리 생성
mkdir {dev_directory_name}
cd {dev_directory_name}

# 파이썬 가상환경 생성
pipenv --python 3.8
```

4. 패키지 설치
```bash
# 가상환경 내 전역 패키지
pipenv install {Packge_name}

# 개발용 패키지 설치
pipenv isntall {Packge_name} --dev

# Pipfile 내 모든 패키지 설치
pipenv install
pipenv isntall --dev

# 패키지 의존성 트리
pipenv graph

# 패키지 보안 취약점 점검
pipenv check
```

4. 가상환경 사용
```bash
pipenv shell
```

5. 가상환경 종료
```bash
exit
```
- 가상환경 제거
```bash
pipenv --rm
```