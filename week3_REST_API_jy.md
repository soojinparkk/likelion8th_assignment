# REST API

---

REST API 란?

 :  REST를 통해 서비스 API를 구현한 것

- REST 란
    - REpresentational State Transfer의 약자
    - HTTP기반으로 필요한 자원에 접근하는 방식을 정해놓은 아키텍쳐
- API 란

    응용 프로그램에서 사용할 수 있도록 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스

---

구성요소

- 자원(resource) : URI
- 행위(verb) : HTTP METHOD
- 표현(representations)

---

특징

- Uniform Interface(일관된 인터페이스)
- Stateless(무상태성)
- Cacheable(캐시 가능)
- Client-Server Architecture (서버-클라이언트 구조)
- Self-Descriptiveness(자체 표현)
- Layered System(계층 구조)

---

REST API 중심 규칙

- URI는 정보의 자원을 표현해야 한다.

    (리소스명은 동사보다는 명사를 사용)

- 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE 등)로 표현

---

URI 설계 규칙

- 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.
- 마지막 문자로 슬래시(/)를 포함하지 않는다.
- URI 경로에는 소문자가 적합하다.
- ‘_’(언더바)보다는 ‘-’(하이픈)을 권장한다.
- 파일 확장자는 URI에 포함시키지 않는다.