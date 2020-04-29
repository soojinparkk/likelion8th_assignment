# REST API

## 1. REST API란?

REST는 Representational State Transfer라는 용어의 약자로,  2000년도에 로이 필딩 (Roy Fielding)의 박사학위 논문에서 최초로 소개됨. 로이 필딩은 HTTP의 주요 저자 중 한 사람으로 그 당시 웹(HTTP) 설계의 우수성에 비해 제대로 사용되어지지 못하는 모습에 안타까워하며 웹의 장점을 최대한 활용할 수 있는 아키텍처로써 REST를 발표함.

HTTP 기반으로 필요한 자원(DBMS, 이미지/동영상/문서와 같은 파일, 서비스 모두 포함)에 접근하는 방식을 정해놓음으로써 웹의 장점을 최대한 활용할 수 있는 아키텍처

## 2. REST 구성

- 자원(Resource) - URI
- 행위(Verb) - HTTP Method
- 메세지(Message)

### 2-1. URI(Uniform Resource Identifier)

리소스의 위치를 나타내는 일종의 식별자로, 리소스에 접근할 때 사용

서버에 있는 모든 리소스는 각 리소스당 클라이언트가 바로 접근할 수 있는 URI가 존재

- URI 설계 시 주의점
    1. URI 경로에는 소문자 사용
    2. 하이픈(-)은 URI 가독성을 높이는데 사용
    3. 밑줄(_)은 사용하지 않음
    4. 파일 확장자는 URI에 포함시키지 않음
    5. 마지막 문자로 슬래시(/)를 포함하지 않음

### 2-2. HTTP Method

리소스에 접근할 때 어떤 성격의 요청인지 알려줌

POST, GET, PUT, DELETE 4가지의 Method를 가지고 CRUD 가능

- POST: Create

    해당 URI를 요청하면 리소스를 생성

- GET: Select

    해당 리소스를 조회 → 해당 도큐먼트에 대한 자세한 정보를 가져옴

- PUT: Update

    해당 리소스를 수정

- DELETE: Delete

    해당 리소스를 삭제

같은 URI들에 대해서도 다른 요청을 하게끔 구별해주는 항목인 Endpoint 존재

REST는 각 개별 API를 상태 없이 수행

→ 해당 REST API를 다른 API와 함께 호출하다가 실패하였을 경우, 트렌젝션 복구를 위해 다시 실행해야 하는 경우 발생

→ idempotent한 메서드의 경우 반복적으로 다시 메서드를 수행해주면 됨

### 2-3. Message

HTTP Header와 Body, 응답상태코드로 구성되어 있음

Header와 Body에 포함된 메세지는 메세지를 처리하기 위한 충분한 정보에 해당

- Body: 리소스에 대한 정보 전달

    데이터 포맷: JSON, XML, 사용자 정의 포맷

- Header: HTTP body에 어떤 포맷으로 데이터가 담겨있는지 정의
- 응답상태코드: 응답상태코드를 통해 리소스 요청에 대한 응답 가능

## 3. REST 특징

- 클라이언트-서버 구조

    REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분됨

- 기존 웹 인프라 사용 가능

    HTTP를 그대로 사용하기 때문에 HTTP가 가진 캐싱 기능도 적용 가능함

    → 잘 관리되는 캐싱은 클라이언트-서버 간 상호작용을 부분적으로 또는 완전하게 제거하여 scalability와 성능을 향상시킴

- 무상태성

    서버에서 어떤 작업을 하기 위해 상태 정보를 기억할 필요가 없고, 들어온 요청에 대해 처리만 해주면 됨

- 중간 매체 사용 가능

    클라이언트와 서버가 분리되어 있기 때문에 중간에 프록시 서버, 암호화 계층 등 중간 매체를 사용할 수 있어 자유도가 높음

- 자체 표현 구조

    REST API 메세지만 보고도 쉽게 이해 가능함

- **REST 한계점**
    - 보안, 정책등에 대한 표준이 없기 때문에 관리가 어려움
    - HTTP 프로토콜만 사용 가능함
    - P2P 통신 모델을 가정했기 때문에 둘 이상을 대상으로 하는 분산 환경엔 유용하지 않음

---

---

## 4. REST API 설계

- URI는 정보의 자원을 표현
- 자원에 대한 행위는 HTTP 메소드로 표현

> 참고 자료

[https://ko.wikipedia.org/wiki/REST](https://ko.wikipedia.org/wiki/REST)

[https://medium.com/@dydrlaks/rest-api-3e424716bab](https://medium.com/@dydrlaks/rest-api-3e424716bab)

[https://meetup.toast.com/posts/92](https://meetup.toast.com/posts/92)

[https://brainbackdoor.tistory.com/53](https://brainbackdoor.tistory.com/53)