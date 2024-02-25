## 웹을 통해 검색하면 어떤일이 일어날까?(front)

> 이 글에서는 웹을 통해 검색하면 front 에서는 어떤일이 일어나는지에 대해 작성합니다. 👀

## 1. 웹 브라우저에 URL을 입력하고 Enter 키 입력

사용자가 https://wwww.naver.com 을 입력하면 프론트 부분에서는 어떤일이 일어날까 ?

이때 입력한 주소인 https://www.naver.com 을 분석하면 다음과 같다.

- https : `프로토콜` 로 어떤방법으로 통신할지에 대해 명시한다. 
- www.naver.com : 은 웹 사이트의 도메인으로 사람이 기억하기 쉬운 주소이며 특정 서버의 ip를 대신하여 나타 냅니다. 실제 연결시에는 해당 주소에 대한 ip주소를 알아야하며 DNS서버를 통해 해당 주소의 ip를 알아 냅니다. 
 
## 2. 웹 브라우저가 도메인명의 ip주소를 조회

사람이 기억하기 쉬운 주소로 되어있는 도메인명(여기서는 www.naver.com)은 사람이 기억하기 쉽지만 컴퓨터는 알수 없습니다. 컴퓨터가 알 수 있고 연결하기전에 도메인명에대한 실제 주소인 ip를 탐색하는 과정이 일어납니다.

웹 브라우저의 ip 주소 조회는 다음과 같이 일어납니다.

일반적으로 DNS(도메인 네임 서버)를 통해 도메인에 대한 ip를 획득하지만 DNS를 통해 질의하기 전에 여러단계의 걸쳐있는 DNS 캐쉬를 확인합니다.

DNS 캐쉬 는 다양한 곳에 걸쳐 존재합니다. `브라우저 캐쉬` `운영체제 캐쉬` `라우터 로컬 네트워크 캐쉬` 혹은 `ISP DNS캐쉬` 가 있을수 있습니다.

> 🤔 - 왜 바로 DNS 서버에 질의 하지않나요 ?   
> DNS 서버에 바로 질의하는 것 또한 리소스가 소모 됩니다. 예제로 검색한 www.naver.com 은 이미 충분히 많은사람들이 사용하고있고 DNS 서버 에 질의하는것또한 DNS 서버에 무리가 갈수있습니다. 그래서 다양한 범위에 걸쳐서 DNS 캐쉬를 남겨두고 DNS 캐쉬를 확인하는 방법으로 DNS 서버의 부하를 줄이고 응답속도를 개선합니다.

## 3. 웹 브라우저가 요청서버와읭 TCP 연결 시작

인터넷에 연결된 웹 브라우저 요청 패킷은 일반적으로 TCP/IP 라고 하는 전송 제어 프로토콜을 사용하여 라우터 장비, 인터넷 서비스 교환기를 통해 이동하며 요청 주소에 대해 연결을 수립합니다.

## 4. 웹 브라우저가 HTTP 요청을 서버로 전송

3 번과정에서 연결이 수립되면 웹 브라우저는 요청 서버에게 HTTP프로토콜을 사용하여 요청을 전달합니다. 

요청에는 다음과 같은 http 스팩이 포함됩니다.

- 1 개의 HTTP method
- 요청된 리소스를 가리키는 경로 
- 통신할 HTTP 버전

추가적으로 다음과 같은 스팩이 포함될 수 있습니다.

- 요청 서버에대한 쿠키
- header

URL 에 대한 요청은 다음과 같습니다. 일반적으로 웹서버를 통한 요청은 `GET` 메서드를 호출합니다.    
예제로는 `GET (www.naver.com)/ HTTPS/2(h2)`로 요청하게 됩니다. 

5. 서버가 요청에대한 응답을 전송
웹 서버는 요청을 받고 요청 라인, 헤더 및 본문정보를 기반으로 요청에 대한 처리를 시작합니다.
`GET (www.naver.com)/ HTTPS/2(h2)` 요청에 대해 서버는 해당 경로의 컨텐츠를 가져와 응답을 생성하여 클라이언트로 다시 전송합니다.

응답에는 다음이 포함 됩니다.

- 요청에대한 상태를 알려주는 상태라인 (http status code)
- 브라우저에 응답 처리 방법을 알려주는 응답 헤더
- 해당 경로에서 요청된 리소스 (HTML,CSS,JS, 이미지 파일과 같은 콘텐츠 , 데이터)

예제의 응답은 다음과 같습니다.
```HTML
<!--응답 헤더 -->
Cache-Control: no-cache, no-store, must-revalidate
Content-Encoding: gzip
Content-Type:text/html; charset=UTF-8
Date:Sun, 25 Feb 2024 05:00:09 GMT
... 생략
```
```HTML
<!-- 응답 -->
<!doctype html>
<html lang="ko" class="fzoom">
    <head>
        <meta charset="utf-8">
        <meta name="Referrer" content="origin">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=1190">
        <title>NAVER</title>
        <meta name="apple-mobile-web-app-title" content="NAVER"/>
        <meta name="robots" content="index,nofollow"/>
        <meta name="description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"/>
        <meta property="og:title" content="네이버">
        <meta property="og:url" content="https://www.naver.com/">
        ...
```

## 6. 브라우저의 콘텐츠 렌더링

브라우저는 요청에대한 서버의 응답을 받아 응답받은 리소스를 바탕으로 렌더링을 진행합니다. 브라우저는 요청에대한 응답헤더에서 `Content-Type` 을 확인하고 HTML 이 수신했음을 알게됩니다. 그리고 브라우저는 `Contet-Type` 으로 뭘해야하고 있는지 안다면 그에따라 행동합니다. HTML 의 경우 다음과 같이 진행됩니다.

### 6-1 브라우저 렌더링 동작   

1. 브라우저에서 요청해서 받은 html 파일을 읽기 시작하면서 파싱 하여서 DOM트리를 구축하게 됩니다.

>DOM(document object model) - DOM은 HTML 문서에 대한 인터페이스입니다. 즉 HTML 문서 형태와 비슷하지만 차이점들이 있습니다. 자바스크립트에서 수정될 수  있는 동적 모델입니다.

2. DOM트리 파싱을 완료하면 완성된 DOM트리와 HTML파싱 하면서 요청해 놓은 link태그, style태그를 결합시켜서 CSSOM트리를 생성합니다.

>CSSOM(css object model) - DOM + CSS = CSSOM

3. 마찬가지로 script태그를 만나면 javascript코드를 실행해줍니다.

4. 만들어진 DOM트리와  CSSOM트리가 합쳐져 렌더 트리를 생성하고 위치와 크기를 계산해줍니다.

5. 마지막으로 렌더 트리를 그리고 브라우저에서 보이게 됩니다.



> [!IMPORTANT]   
> 스크립트   
웹 모델은 동기식입니다. 작성자는 파서가 \<script\> 태그에 도달하는 즉시 스크립트가 파싱되고 실행되기를 기대합니다. 스크립트가 실행될 때까지 문서의 파싱이 중단됩니다. 스크립트가 외부에 있는 경우 먼저 네트워크에서 리소스를 가져와야 합니다. 이 작업도 동기식으로 수행되며 리소스를 가져올 때까지 파싱이 중단됩니다. 이 모델은 수년 동안 사용되었으며 HTML4 및 5 사양에도 지정되어 있습니다. 작성자는 'defer' 속성을 스크립트에 추가할 수 있습니다. 이 경우 문서 파싱이 중지되지 않고 문서가 파싱된 후 실행됩니다. HTML5는 스크립트를 비동기로 표시하는 옵션을 추가하여 다른 스레드에 의해 파싱되고 실행되도록 합니다.

## 참조
- [aws_ 웹브라우저에 검색하면 어떤일이 일어날까](https://aws.amazon.com/ko/blogs/korea/what-happens-when-you-type-a-url-into-your-browser/)

