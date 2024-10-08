# 스프링 이벤트
> 이글에서는 스프링에서 이벤트 액션을 다루는 방법과 스프링 이벤트에 대해서 다룹니다.


## 1. 언제 이벤트가 필요할까 ?

### 1-1 예시

최근 나오는 자동차들은 성능이좋아 후진할떄 네비게이션 대신 후방 카메라 정보를 보여준다 이를 코드로 표현하면 어떨까 ?

```Java

void 후진기어변경(){
    네비를후방카메라로변경()
    // 기어를 후진으로변경 ->
    기어를 후진으로변경()
}
```

이러한 방식으로 동작할것이다. 만약 후진기어로 변경했을때 후방카메라 외 안전거리 확보여부를 판별하는 센서도 킨다고 가정해보자 🤔

그렇다면 대략적으로 다음과 같이 코드가 변할것이다.
```Java
void 후진기어변경(){
    네비를 후방카메라로변경()
    안전거리 센서 시작()
    // 기어를 후진으로변경 ->
    기어를 후진으로 변경하는로직
}
```


이렇게 된다면 한 메서드가 담당하는 코드가 커지고 유지보수하기 복잡해진다.

### 1-2. 어떻게 처리할 수 있을까 ?

위의 예제로 돌아와서 `언제`, 그리고 `어느떄`  특정 행위가 실행되어야하는가 다시생각해본다면 예제에서는 `후진기어로 변경` 시 특정행동이 실행됨을 인지할 수 있다.

그렇다면 `후진기어` 변경하는 메서드(함수) 는 후진기어변경만 담당하게하고 , `후진기어` 액션이 일어났다 라는 이벤트를 발행하고  해당 이벤트가 발행하면 동작해야하는 부가적인 일들을 다른 클래스와 함수에서 하도록한다.

예제코드는 다음과 같이 변경할 수 있을것이다.
```Java
void 후진기어변경(){
    
    // 후진기어변경 로직 실행 ->
    ..

    후진기어변경 이벤트 발행()
}

void 후진기어 변경 이벤트 발행(){
    후방카메라전환()
    감지센서 작동()
}

void 후방카메라전환(){

}

void 감지센서 작동(){

}
```

이로써 후진기어변경은 후진기어 변경외 해당 이벤트를 알리는 작업이 추가되었으며 그외 후방카메라 전환 감지센서 작동은 다른곳에서 처리할 수있도록 변경되었다.

이렇듯 이벤트 기반으로 처리하면 다음과 같은 이점들이있다.
- 높은 확장성 : 위의예제에서 후진기어 변경 시 해야하는 일이 늘어나도 이벤트 발행시 처리해야할 로직에 추가하는것으로 간단히 책임을 나눌 수 있다.
- 느슨한 결합 : 변경전 예제 에서는 후진기어 변경시 너무 많은 행위가 추가되어 함수의 책임이 커서 결합도가 높았다. 이를 분리하여 느슨한 결합을 추구할 수 있었다.


## 스프링에서 이벤트 처리

스프링 에서도 이벤트기반으로 처리해야하는 경우들이 생긴다. 물론 스프링에서 이벤트기반 처리를 지원해주기에 따로 의존성을 추가하거나 할 필요없이 간단하게 설정할 수있다.

>![NOTE]
- 이글에서는 4.2 이상의 스프링 버전을 기준으로 글을 작성합니다. 이전버전에 대해서 적용되지 않을 수 있습니다.
- 

## 참고한글
- [Spring Events](https://www.baeldung.com/spring-events)