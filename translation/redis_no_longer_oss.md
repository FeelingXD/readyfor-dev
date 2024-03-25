## Redis는 더이상 OSS(Open Source Software)가 아닌가? 😅

![redis_git_pr](https://opengraph.githubassets.com/a0082d00fbc4277a7a1ec7b1c70a113778c5bb8403ff5f657037fc5fdbfeb2da/redis/redis/issues/12590)

> 최근 레디스의 라이센스 약관이 변경 되었다.   
과연 무엇이 변경되었고 레디스는 여전히 OSS 일까? 🙄

## Redis 의 약관변경

Redis 는 [#12590pr](https://github.com/redis/redis/issues/12590) 에서 다음과 같이 OSS 라이센스 약관을 변경 하였다.

기존 BSD 라이선스에서  Redis Source Available License (RSALv2) 과 Server Side Public License (SSPLv1) 의 듀얼 라이선스로 변경되었습니다.

```
BSD -> RSAL and SSPL 😂
```

### BSD ? RSAL ? SSPL?

> 다양한 라이선스가 있지만 짧게 이번 레디스 라이선스 와 관련된 라이선스들을 알아보자.

#### BSD

>[!Note]
BSD 허가서(BSD licenses)는 자유 소프트웨어 저작권의 한 가지이다. BSD 계열 소프트웨어를 포함한 많은 프로그램에서 사용한다.   
>BSD(Berkeley Software Distribution) 라이선스는 소프트웨어 라이선스라고도 할 수 없을 만큼 미약하여, 해당 소프트웨어는 아무나 개작할 수 있고, 수정한 것을 제한 없이 배포할 수 있다. 다만 수정본의 재배포는 의무적인 사항이 아니므로 BSD 라이선스를 갖는 프로그램은 공개하지 않아도 되는 상용 소프트웨어에서도 사용할 수 있다.

기존 라이센스였던 BSD 는 오픈된 레디스 소스를 활용하여 변경하여 상용된 소프트웨어를 팔거나 서비스를 제공할 수 있었다.

#### RSAL(RSALv2) SSPL

>[!Note]
 SSPL 및 RSAL 라이선스는 오픈 소스가 아니며 클라우드 서비스 제공을 위한 제품의 무료 사용을 금지하는 추가 제한 사항이 있습니다.그리고. SSPL 라이센스는 AGPLv3 Copyleft 라이센스를 기반으로 하고 RSAL 라이센스는 허용된 BSD 라이센스를 기반으로 하지만 두 라이센스 모두 비슷한 목적을 가지고 있습니다.   
RSAL 라이선스는 상업적인 경우나 관리되는 유료 서비스를 제외하고 애플리케이션에서 코드의 사용, 수정, 배포 및 통합을 허용합니다(내부 서비스에는 무료 사용이 허용되지만 Redis에 대한 액세스를 제공하는 유료 서비스에는 제한이 적용됩니다). 반면, SSPL 라이선스는 카피레프트 원칙에 따라 애플리케이션 자체의 코드뿐만 아니라 클라우드 서비스를 제공하는 데 관련된 모든 구성 요소의 소스 코드도 동일한 라이선스 하에 제공되도록 요구합니다.


## 레디스는 왜 라이선스를 변경 했을까?

AWS , AZURE 등에서 기존 redis를 사용하여 만든 사용서비스인 Amazon ElastiCache for Redis, Azure Cache for Redis 등의 형태로 redis를 가공하여 클라우드 서비스를 제공합니다. 하지만 이는 redis의 사업모델 에 영향을 주며 redis가 오픈소스이기에 MS(Micro Soft)와 Amazon 은 Redis의 코드를 가공해 더 나은 제품을 만들어 서비스를 제공 하지만 Redis의 발전에 기여하지는 않았습니다. (흔히 말하는 Cherry-Picking 되는일이 발생 했습니다.) 즉 Redis가 OSS(오픈소스) 와 Enterprise(기업용 모델) 로 분리하고 OSS 를 공개하고 Enterprise모델을 사업을 운영했는데 MS 와 Amazon 에서 OSS 모델을 가져가 개선하여 서비스해 Enterprise 모델 사업에 문제가되었다.

그리하여 Redis OSS모델 또한 라이센스를 변경함으로서 견제하게 되었는데 기존 오픈소스 사용자들 또한 라이선스 변경으로 인해 피해를 보는것 아니냐는 반응이다.

## 생각 

레디스는 어쨌든 라이선스 변경으로 인해 명목상 불완전한 OSS 가 되었다. Redis를 사용하는 사업자라면 비즈니스상 사용하고있는 Redis를 다른 DB로 변경을 고민해야할지도 모른다. 그렇다고 레디스의 라이선스 변경이 잘못되었다! 라고 비난하기도 어려운 것 같다.
Redis OSS 는 .. 아쉽지만 우리가 아는 OSS 로 남기는 쉽지 않을것 같다.