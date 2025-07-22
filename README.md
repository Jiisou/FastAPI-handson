실습 with [교재: FastAPI로 배우는 백엔드 프로그래밍 with 클린 아키텍처](https://product.kyobobook.co.kr/detail/S000214428277)

---

**How to execute**

```
uvicorn main:app --reload
```
> `--reload` 옵션은 파일 내용이 변경될 때 애플리케이션이 재시작되도록 하여 코드를 수정한 후 서버를 종료시키고 재실행시킬 필요가 없음, 개발 단계에서 사용하고 배포시에는 사용하지 않도록 하자.


- If you want to assign a port
```
uvicorn main:app --reload --port 8080
```