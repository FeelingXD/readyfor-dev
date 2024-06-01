# 😸 Git 브랜치 전략

> Git 을 통해 협업을 하게된다면 브랜치를 통해 작업을하고 병합 하는 과정을 겪게될것이다. 다양한 git 브랜치 전략에 대해 알아보자.


## GIT FLOW - 깃 플로우


![](https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png)

### GIT FLOW - 간략한 설명
Git-flow에는 5가지 종류의 브랜치가 존재합니다. 항상 유지되는 메인 브랜치들(master, develop)과 일정 기간 동안만 유지되는 보조 브랜치들(feature, release, hotfix)이 있습니다.

- master : 제품으로 출시될 수 있는 브랜치
- develop : 다음 출시 버전을 개발하는 브랜치
- feature : 기능을 개발하는 브랜치
- release : 이번 출시 버전을 준비하는 브랜치
- hotfix : 출시 버전에서 발생한 버그를 수정 하는 브랜치

#### 문제점 
GIT - flow 는 웹앱(web apps) 기반으로 작성하지 않았고 오히려 이전략이 불편 할 수있습니다. 다음과 같은 문제점들이 있습니다.
- 브랜치가 오래유지됨
- 브랜치 관리가 복잡함


## GITHUB FLOW - 깃 허브 플로우
![](https://velog.velcdn.com/images/gmlstjq123/post/04588f97-e776-4829-a519-58f7c93b6c4a/image.png)

### GIHUB FLOW -간략한 설명

깃플로우는 정석적이지만 많고 복잡한 브랜치 사용으로 상시 배포해야하는 환경에서는 익숙치 않았습니다. 이에 GITHUB FLOW는 간단한 브랜치 전략을 제공합니다.

- master : 제품 브랜치
- feature : 기능단위 의 브랜치

 어떻게보면 TBD(Trunk based development)으로도 보일 수 있습니다. 
 심플한 브랜치 전략으로 더 상시 더자주 배포할 수 있게되었습니다.

 #### 문제점 
 - 기능 A, B 가 병합되어야하는데 기능 A 가 B에 의존하고있다면 이는 A를 MAIN 머지를 대기해야하는 일이 발생하게됩니다.
 - 트렁크기반 의 장점인 빠른 병합의 장점이 오히려 몇달동안 개발해야 할 기능이 생긴다면 미루어지는 일이 생기게 됩니다. 
 - 바로바로 main 에 병합되므로 충분히 테스트되지 못한 코드가 병합되어 배포되는 경우가 생길 수 있습니다.

## GITLAB FLOW - 깃 랩 플로우
![](https://velog.velcdn.com/images/jhchoi94/post/a13f7205-2995-4a7c-b726-a6c9babb2e89/image.png)
### GITLAB FLOW - 간략한 설명

GITLAB FLOW 는 GIT FLOW 의 복잡함과 GITHUB FLOW의 단순함 그사이의 절충하는 FLOW이다.

사용되는 브랜치
- master(develop) : 다른 브랜치 전략의 develop 브랜치에 해당합니다. master로부터 feature 브랜치로 작업하고 다시 머지됩니다. 
- feature : 기능단위의 작업이 진행되는 브랜치입니다.
- pre-production : 실제 배포전 테스트 하는 브랜치 입니다.
- production(main,maintanance) : 실제 서비스를 하는 브랜치 입니다.

## SIM GIT FLOW - SIMPLE GIT FLOW  
![](https://lh7-us.googleusercontent.com/X0Od7FS9iLJyDPfaSERK6FrmPZ6O-WWNvGfwZWShA18Ktj1B6FLJTCTsazN2Oa6fQoSG1OUeq0hkGfO7lIW59yEQg0NO-XW382gIpsru-QYvr_R8q9_zWj_Yf_BDvK4_HESuWLhI8NvgYGQAG6hkBYQ)


### SIM GIT FLOW - 간략한 설명
다른 브랜치 전략들은 모두 feature가 순서대로 반영되어야하는 문제점이 있었습니다.

`feature` -> `dev` 혹은 `master` 에 병합하고 `production` 으로 배포됨 

이는 기능단위의 통합테스트를 목적으로는 장점이 되지만 항상 feature 등이 순서대로 반영되어야했습니다. simgit 은 각 독립적인 `feature`들이 빠르게 realease 되는 방법을 제공합니다.

- master : 실제 서비스가 되는 브랜치
- release : 배포 대기를 위한 브랜치
- feature : 여러가지 단위의 기능이 작성되고 작성된 기능은 바로 release로 머지하여 배포준비를 합니다.

## 참고한 글

- [우린 Git-flow를 사용하고 있어요](https://techblog.woowahan.com/2553/)
- [잦은 배포를 언제나 안정적이고 쉽게- SimGit flow 기반 Git 브랜치 전략 개선기](https://blog.3o3.co.kr/231101-insight/)
- 