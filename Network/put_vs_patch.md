## PUT vs PATCH

자원을 수정하는 HTTP METHOD 에는 PUT 과 PATCH 두가지가 있습니다. 
어떤 차이가 있을까요 ?

표로 정리한다면 다음과 같이 표현 할 수 있습니다.

|비교 |PUT|PATCH|
|---|---|---|
|멱등성|보장|보장하지 않음 
|자원 교체|전체 자원의 교체|자원의 부분교체 

조금더 구체적으로 예시를 들어볼게요. 🤔   
우선 다음과같은 자원이 있다고 가정해봅시다.

```json
{
    "id" : int
    "name": String
    "age": int
}
```
```json
{
    "id" : 1
    "name": "지민"
    "age": 20
}
```
위의 자원에 대해 변경한다면 다음과 같은 일들이 일어날 겁니다.(Rest API라면)
### PUT 의 경우

>[!TIP]
`PUT` METHOD 는 자원의 전체 교체하기를 예상합니다. 

`PUT` METHOD를 통해 예시로 들었던 자원을 변경한다고 생각해볼게요 아마 요청주소는 다음과 같을겁니다. 

`PUT http://~~domain/person/1`
```json
// body
{
    "id" : 1
    "name" : "철수"
    "age" : 21
}

```
이 경우에 PUT METHOD 가 실행되고 id 1에대한 내용이 전체 변경이되는 걸 확인 할 수 있습니다.

만약 요청 body 에 자원이 누락되어 있다면 어떻게 변경되길 기대할까요 ?

`PUT http://~~domain/person/1`
```json
// body
{
    "id" : 1
    "age" : 21
}

```

만약 위와 같이 요청하게 된다면 자료의 name 값이 없기에 빈값에 대해서는 `null` `None` 등의 값이 없음을 명시하게 됩니다. 위와 같이 요청한경우 사용자는 ID 1에대해 다음과 같은값을 기대합니다.

```json
// GET http://~~domain/person/1
{
    "id" : 1
    "name" : NULL
    "age" : 21
}
```

### PATCH 의 경우 

> [!TIP]
PUT 경우와 다르게 PATCH의 경우 멱등성을 **반드시** 보장하진 않습니다. (서버 구조에따라 멱등성을 보장 할 수는 있습니다.)

PUT 의 부분교체 요청에 대해 PATCH의경우를 알아봅시다.

초기 데이터 형태는 다음과 같습니다.
```json
{
    "id" : int
    "name": String
    "age": int
}
```
```json
{
    "id" : 1
    "name": "지민"
    "age": 20
}
```

`PATCH http://~~domain/person/1` (PUT 예제에서 PATCH 로 변경합니다.)
```json
// body
{
    
    "id" : 1
    //"name" : NULL   해당 칼럼은 보내지 않음을 표현하기위해 주석처리합니다.
    "age" : 23
}
```
PATCH 요청에서 이름칼럼을 제외하고 AGE 칼럼에 대해서만 기존 20-> 23 으로 변경되었습니다. 이경우 `GET` 요청을 통해 본다면

```json
{
    "id" : 1
    "name": "지민"
    "age": 23
}
```

`age` 의 값만 변경되는걸 확인 할 수 있습니다.




### PATCH 가 멱등성을 보장하지 않는경우

>[!NOTE]
> 그럼 `PATCH` 도 멱등성을 보장하는것 아닌가요 ? 위의 예제에서 몇번을 보내도 결국 
age ="23" 로 변경된 값을 보장할텐데 말이에요 🤔

위의 예제만 보았을 때는 위와같은 의문이 들 수 있다.

그렇다면 PATCH 의 경우 멱등성이 보장되지않는 예시를 알아보자. 

기존 데이터 구조와 다르게 이번경우에는 다음과 같은 데이터를 사용한다.

```json
{
    "account" : String // UUID 뱅킹 고유번호
    "balance" : Number // 잔액
}
```

이제 은행계좌 정보를 갱신하는 PATCH 요청을 보낼수있는 URL 이 있다고 생각해보자.

은행 계좌에는 자원을 교체하기 위해 연산과정이 발생할 수 있음을 알아야한다. (입금,출금 등)
다음 과 같이 요청하는 주소가 있다고 가정해보자. (연산을위해 operator 파라미터를 추가해서 받는다. )

`PATCH http://domain/{account}operator=deposit&amount=1000` (amount 금액만큼 입금하는 url)

이 있을 때 해당 요청 마다 account 의 balance가 변하게 된다. 이렇게 된다면 같은 요청에대해서 같은 응답을 보장하는 `멱등성`을 보장하지 않게된다.

하지만 이경우는 추가적인 연산이 필요한 특수한 경우이며 모든경우에서 `멱등성`을 보장하지 않는건아니다. 다만 보장하지 못하는 경우가 있기에 PATCH 메소드는 `멱등성`을 보장하지 않는다. 

물론 서버 구성과 설계에따라 `멱등성`을 보장하도록 만들 수 있다.


## 참조 
- [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

