## 핑고라는 Nginx를 대체할 수  있을까 ?

CLOUDFlARE 에서 자사에서 사용하는 Pingora를 오픈소스로 공개하였습니다. NGINX와 비슷한 로드밸런서와 리버스프록시 역할을 하는 러스트 프레임워크 핑고라는 NGINX를 대체할 수 있을까?


## 오픈소스 RUST 프레임워크 핑고라
![alt text](https://blog.cloudflare.com/content/images/2024/02/Rock-crab-pingora-open-source-mascot.png)
### 핑고라 (Pingora)

>[!NOTE]
> 핑고라는 CloudFlare에서 만든 RUST 기반의 오픈소스 프레임워크로 NGINX와 같이 리버스 프록시 로드벨런서등을 지원합니다. 2022년 처음으로 클라우드에서 사용하기 시작했으며 2024년 2월 오픈소스로 공개 되었습니다.

Pingora는 Cloudflare의 Rust 기반 비동기 다중 스레드 프레임워크로, 이를 통해 규모에 맞게 HTTP 프록시 서비스를 쉽게 구축할 수 있습니다.

### 🤔 왜 클라우드플레어는 NGINX 를 Pingora로 변경했는가

Cloudflare는 성장하기 시작했을 때 발생한 눈에 띄는 문제로 Nginx에서 전환해야했습니다. Nginx에 대한 현대적이고 빠르며 메모리 안전한 대안이 필요했습니다.

이떄 Cloudflare는 Nginx를 대체하는 자체 솔루션을 개발하기 시작했습니다.

Pingora로 대체한 이후 기존의 Nging대비 동일한 트래픽 로드에서 70% 더 적은 CPU 와 67% 더적은 메모리를 소비할 수 있었습니다. 또한 Pingora가 Nginx기반 서비스보다 http요청을 더 빠르게 처리 할 수있었습니다.

### 🤔 어떻게 Pingroa는 Nginx보다 더 빠를 수 있는가 
![Nginx](https://blog.cloudflare.com/content/images/2022/09/image2-4.png)

Nginx는 멀티 프로세스 + 싱글 스레드 방식으로 동작합니다. Nginx의 프로세스 아키텍쳐에서는 성능과 효율성을 저하시키는 운영상의 단점이 있습니다.

- Nginx에서는 각 요청이 단일 작업자에 의해서만 처리될 수 있습니다. 이로 인해 모든 CPU코어에 걸쳐 로드 불균형이 발생 하고 이로 인해 속도가 느려집니다.

아키텍쳐의 차이
- NGINX : 동기 방식, 단일 스레딩 아키텍처
- PINGORA : 비동기 방식, 멀티 스레딩 아키텍쳐

![Pingora](https://blog.cloudflare.com/content/images/2022/09/image3-3.png)
핑고라가 빠른이유

핑고라는 멀티 스레딩 아키텍쳐를 채택했습니다.

기존의 NGINX는 각 프로세스가 스레드 풀을 생성하고 연결을 재사용했습니다. 이는 각 프로세스가 유사한 연결을 사용하고있을때 재사용성을 떨어뜨리는 원인이 되었습니다. 하지만 핑고라에서는 기존의 멀티프로세스에서 멀티 스레딩 방식으로 변경함으로써 재사용성을 높였습니다.

이는 TCP 및 TLS 핸드셰이크에 소요되는 시간을 줄여줍니다.

## 그럼에도 아직은 NGINX 👀

CLOUD FLARE가 NGINX에서 PINGORA로 변경한 이유도 이해하고 새로운 오픈소스이자 경쟁자라니 .. 정말 멋진일이라고 생각한다. 하지만 그럼에도 핑고라는 아쉽다.
다음은 내가 생각하는 몇가지 아쉬운 이유이다.

- 핑고라는 오픈소스로 출시한지 얼마 되지않았다. 상대적으로 사용 레퍼런스가 적다
- 러스트 기반 프레임워크 워크로 NGINX처럼 직관적이고 간단한 설정이아닌 더 많은 정보를 제공한다. (초보자에겐 어렵다.)


<!-- Todo NGINX 에서 개선한 pingora 작성하기-->
## 참조
- [핑고라 깃허브](https://github.com/cloudflare/pingora)
- [NGINX_WORKER불균형](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)
- [핑고라를 구축한 방법](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet)