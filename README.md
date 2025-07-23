실습 with [교재: FastAPI로 배우는 백엔드 프로그래밍 with 클린 아키텍처](https://product.kyobobook.co.kr/detail/S000214428277)

---

# **How to execute**


###  포어트리를 이용한 가상 환경과 의존성 관리

```
$ poetry env list --full-path
/Users/myname/Library/Caches/pypoetry/virtualenvs/fastapi-ca-xxx...-py3.11 (Activated)

$ emulate bash -c '. /.../bin/activate/bin/activate'
```
> 포어트리는 Python 중심의 개발에서 고려되는 프로젝트 관리 및 패키징을 위한 가상 환경

### Run my server
```
uvicorn main:app --reload
```
> `--reload` 옵션은 파일 내용이 변경될 때 애플리케이션이 재시작되도록 하여 코드를 수정한 후 서버를 종료시키고 재실행시킬 필요가 없음, 개발 단계에서 사용하고 배포시에는 사용하지 않도록 하자.


- If you want to assign a port
```
uvicorn main:app --reload --port 8080
```
---
### Check API DOCs
```
http://127.0.0.1:8000/docs
```

---
# Docker & Database
독립된 개발 환경을 위해 도커를 이용해 MySQL을 실행함: `open -a Docker`
```
docker run --name mysql-local -p 3306:3306/tcp -e MYSQL_ROOT_PASSWORD=test -d mysql:8
```