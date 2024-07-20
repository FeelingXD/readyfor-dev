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
## apply


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

## let

## run

## also

## with




## 더 읽어볼글 😉

- [kotlin-scope-function](https://kotlinlang.org/docs/scope-functions.html)