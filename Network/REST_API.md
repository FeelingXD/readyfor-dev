## REST_API

> 이 글에서는 HTTP_API 로도불리는 REST_API 에 대해 다룹니다. 학술적인 REST_API 보다 실제 사용되고 있는 REST_API 에 가까운 글을 작성합니다.


## API ?

우선 REST_API 를 알아보기전 API를 간단하게 알아보면 다음과 같다.

> [!Note]
> API (Aplication Programming interface,응용 프로그램 프로그래밍 인터페이스)
> API 는 응용프로그램에서 사용할 수 있도록 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 많드는 인터페이스 를 뜻한다. 혹은 상호작용하는데 규칙 으로도 불린다.

API 는 REST_API 처럼 HTTPS 프로토콜로 주고받는 API 뿐만아니라 특정언어나 운영체제 등에서도 API가 존재한다. 대표적으로 JAVA 에서 제공하는 패키지들(java.util,java.math 등)도 API로 볼 수 있으며
운영체제 에서도 LINUX API등 이 존재한다.

## REST 와 RESTFUL

>[!NOTE]
> REST   
`REpresetational State Transfer` 의 약자로,
자원을 이름(자원의 표현)으로 구분해 자원의 상태(정보)를 주고 받는 모든 것을 의미
자원(resource)의 표현(representation)에 의한 상태 전달을 뜻한다.
- 자원(정보) : API 를 제공하는 것들(문서,그림,데이터, 혹은 기능 들 까지)
- 표현(이름) : API가 제공하는 자원의 이름(DB의 유저라면 'users' 등으로 자원의 이름을 표시)
- 상태 전달(데이터 응답형태) : Client가 요청시점에 따른 자원의 상태를 전달. (대부분 JSON 등 문서형태로 주고 받는다.)

REST는 웹의 기존 기술과 HTTP 프로토콜을 최대한 활용하기에 웹의 장점을 최대한 활용할 수 있고 아키텍처 구조변경이 용이한 아키텍처이다.
REST는 네트워크 상에서 Client(요청자) 와 Server(제공자) 사이의 통신 방식중 하나이다.

### 그럼 REST는 어떻게 자원을 표시하고 응답을 요청할까 ?

REST 는 client 와 server 의 통신방식이다. 이는 http 프로토콜의 요청 전달 방식과 동일하다. 즉 http 프로토콜을 통해 데이터를 주고 받을 수 있는데. http 프로토콜에서 자원의 형태, 방식 들도 모두 표현할수있다.

- 자원의 CRUD(create,read,update,delete) 등은 http method 로 (POST,GET,PUT(PATCH), DELETE)   
- 자원의 표현은 요청을 보내는 SEVER의 endpoint인 URI(uniform Resource Identifier)로   
- 상태 전달은 http 요청에 따른 응답으로 (JSON,XML) 표현 할 수 있다. 

### 그럼 RESTful 하다는 건 뭔데 ?
여기까지 rest처럼 표현하는 방법에 대해 간략하게 알아보았다. rest 규칙을 지켜 일관성 있게하는것
이것이 restful 하다를 의미한다. 이중에서도 가장중요한건 `일관성` 이다.

>실제로도 RESTful하게 API를 작성하는 다양한 디자인 패턴이나 코드를 깔끔하게 작성하는 방법, 다양한 개발자들 사이에서 올바르게 협업하는 방법 등 표준으로 삼아도 무방할만큼 많은 좋은 기술들이 있지만 실제 ‘100%’ 사용되는 경우는 드물다고 합니다. 

### 어떻게 URI를 설계할 것인가.

- 슬래쉬(/) 를 이용하여 계층 관계를 표현한다. 가령 team 아래 member 의 구성이있다면 team/member 로 구상할 수 있을것이다.
- 여러 리소스들의 집합을 의미하는것은 복수형으로 각 리소스들은 단수를 사용
- 언더스코어(_) 보다는 -(하이픈) 을 사용해서 구분하기! (❌ room_mate, ✅ room-mate)
- URI에 파일의 확장자는 포함하지 않음 (❌ myhouse/room1.jpg -> ✅ myhose/room1)

### 그래서 결국 REST_API는..

여기까지 읽었다면 REST_API 이미지가 모호하지만 완성되어가고 있을것이다. 결국 RESTFUL을 준수하는 API의 형태이며 HTTP 로 실행되기에 HTTP 자원을 최대한 끌어다 쓰는 API가 REST_API 이다.
REST_API 의 저자인 ROY.D는 조금더 깊게 다루지만 실제로는 이정도를 다루게 된다.


## 참조
- [위키](https://namu.wiki/w/API)
- [그런 REST API 로 괜찮은가](https://www.youtube.com/watch?v=RP_f5dMoHFc)
- [restapi-restful](https://wallees.wordpress.com/2018/04/19/rest-api-restful/)