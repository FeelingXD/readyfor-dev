## 코틀린 스코프함수 

코틀린에서는 표준으로 제공하는 표준  스코프함수를 제공한다. 

스코프 함수는 특정 객체의 컨텍스트 내에서 특정 동작 을 실행하기 위한 목적만을 가진 함수다.

이 스코프 내에서는 객체의 이름을 통해 일일히 참조할 필요 없이 객체를 접근하고 핸들링할수있다.

코틀린에서 제공하는 스코프 함수는 총 5가지로, [apply, run, with, else, let] 이 있으며 각기 다른 목적으로 사용된다.

코틀린 공식 홈페이지에서는 이러한 기본함수들을 다음과 같이 설명하고있다.

>[!NOTE]   
Basically, these functions all perform the same action: execute a block of code on an object. What's different is how this object becomes available inside the block and what the result of the whole expression is.

>[!NOTE]
기본적으로 이 기능들은 같은 동작을한다 . 객체에대한 블럭코드 를 실행한다. 
다른점이라면 블록내에서 객체를 사용할 수 있는방법과 코드표현식의 결과아더,
## 1. apply


코틀린에서 `apply` 는 다음과 같이 정의되어있다
```kotlin
// 함수블럭을 가지는 스코프함수이며 반환값을 가지지않음  
inline fun <T> T.apply(block: T.() -> Unit): T
```

```kotlin
data class SampleClass(
    val title: String? =null,
    val contents: String? =null,
){
    fun initWithStub(){
        this.title ="stub"
        this.contents ="stub" 
    }
}

fun main{
    var a = SamepleClass(title= "제목" contents= "내용")   

    var b = SampleClass()
    .apply{
        initWithstub()
    }
    println(a)
    println(b)
}
```
`apply` 스코프 함수를 통해 생성자로 할수있는 프로퍼티 초기화 뿐만 아니라
추가적인 작업을 초기화 시점에 할 수 있다.

## 2. let

## 3. run

run 은 두가지 사용법이 있다.

1. 원본객체의 확장함수

접근자는 this 로 사용한다.
```kotlin
@kotlin.internal.InlineOnly
public inline fun <T,R> T.run(block: T.()->R):R{
    contract{
        callsInPlace(block,InvocationKind.EXACTLY_ONCE)
    }
    return block()
}
```

해당 함수의 동작을 수행 한 후 함수의 반환값을 반환한다. `let`과 대비되는 점은 접근자가 `let`은 it 으로 `run` 은 `this` 로 접근자를 받는다.

2. 단순 run block

## 4. also

## 5. with

with는 다른 스코프 함수들과 다르게 확장 함수형이 아닌 일반 함수처럼 사용된다.

```kotlin
 // 확장함수 let 의경우

변수.let{it -> 행위}
//  with 는 다음과 같이 사용된다.
with(yourObj){
     // ~ 행위
} 
```

이러한 특성때문에 `with` 는 파라미터가 non-null 이여야 정상적으로 작동된다.

다른 스코프 함수들은 확장 함수의 형태이기에 null 일경우 엘비스연산 `?:`  혹은 safe call (?.~) 등을 통해 `null` 의 경우 동작을 지정할 수 있지만 with는 자체적으로 null 검사를 할 수 없다.

## it ? this ? 어떻게 접근자를 구분할까

이는 스코프 함수가 어떻게 이루어 져 있는지를 확인하면 알수있지만 .. 사실 하나하나 다보는 사람이 없으므로. 나는 다음과 같은 방법으로 인식하고 있다.


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FGxnKZ%2FbtrUzl3TT1k%2FsQtKns06V9sBau5K6R06mK%2Fimg.png)



## 사실 ..

어떤걸 사용하더라도 이렇게 써야한다. 저렇게 써야한다. 라는 기준보다. 컴파일시 ~한 방법으로 변환되고 실제성능은 이렇다. 또 실제 읽는 사람들로 하여금 ~때 가독성이 좋다. 의 기준이 되었으면 싶다.

## 관련이미지
![kotlinScope](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIUpME%2Fbtq2MORQCUb%2Fp9qQC8KTJUxWuFAm4ErAn0%2Fimg.png)



## 더 읽어볼글 😉

- [kotlin-scope-function](https://kotlinlang.org/docs/scope-functions.html)