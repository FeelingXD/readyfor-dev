## Stream

> 이 글에서는 Java 8 에서 추가된 Java 의 Stream 에 대해서 다룹니다.

## 스트림 ? 🤔

Java 오라클 공식문서에서 다음과 같이 Stream 을 설명합니다.

> [!NOTE]
> A sequence of elements supporting sequential and parallel aggregate operations.

> [!NOTE]
> `순차 및 병렬적인 집계연산을 지원하는 연속 된 요소` 라고 표현하고 있습니다.

배열, 집합등 특정 집단의 연속적인 데이터의 흐름 으로 생각하면 좋을것 같습니다.

### 스트림은 어떻게 동작할까?

스트림은 다음과 같은 프로세스를 따른다

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbmDKDCIdFWj4U-MNKUjP-Ssn5OnLdFHKLj_ihk94ZOFzfY1q7XYvkmcRKSR3Jb47u-MU&usqp=CAU" width="100%">

#### 생성 (Create Stream)

스트림을 생성할 데이터 풀에서 스트림을 만드는과정이다 데이터풀은 Arraylist, set등 데이터 집합등이 될수 있다.

#### 가공 (Intermediate Operation)

스트림에서 데이터를 어떻게 가공할지 결정한다. 간단한 예시를 들어보면 특정 조건을 만족하는 filter, 데이터 가공을 하는 map , 데이터 를 정렬하는 sorted 등이 있다.

> [!TIP]
> 스트림 가공은 `중간 연산`으로 불리기도하는데 중간연산의 결과값은 스트림을 받아 해당 연산을 수행하는 새로운 스트림 인스턴스를 반환한다.

#### 소비 (Terminal Operation)

스트림 가공단계를 마치고 이제 새로 만들어진 데이터흐름을 정리하는 단계 이다. 데이터의 흐름에서 조건을 만족하거나 모두 만족하는지 체크하는 (AnyMatch, allMatch) , 스트림을 수집하여 다른형태로 가공하는 collect 등이 이곳에 포함 됩니다.

> [!WARNING]
> 스트림은 일회성으로만 사용됩니다. 즉 기존스트림에서 `소비` 연산이 발생하면 해당스트림은 다시 사용할 수 없습니다. 필요시에 새로운 스트림을 만들어서 사용해야합니다.

## 예제로 배우는 Java의 스트림

```Java
// https://school.programmers.co.kr/learn/courses/30/lessons/181910
// 문자열뒤의 n개의 글자
/**
 * 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로
 * 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
 * */
import java.util.stream.*;
class Solution {
    public String solution(String my_string, int n) {
        return my_string.chars().skip(my_string.length()-n)
            .mapToObj(ch ->  String.valueOf((char)ch))
            .collect(Collectors.joining());
    }
}
```

1. my_string.chars() 는 String 의 값인 char[] 의 int값의 스트림을 반환한다 ->Intstream
2. Stream.skip(n) 스트림의 n 개만큼 스킵한다.
3. mapToobj(ch -> String.valuOf()) 기존의 IntStream은 정수형만 가질수 있으므로 maptoObj를 통해 charstream 을 가지도록 변경해준다.
4. 마지막으로 collect를 joining으로 문자로 묶어 String 으로 반환한다..

## 개인적인 생각

Java 8 에서 Stream ,람다등 함수형 패러다임의 도입은 좋은 시도라고 생각한다.
Java가 유연하게발전하고있지만 여전히 다른언어에 비해 조금 경직되어있다고 개인적으로 생각된다.(컴파일언어 특징 인것 같다.)

추가적으로 평소 알고리즘 문제를 풀때 Python을 자주사용해서 스트림이 매우 익숙하지만 자바메서드를 자주사용안하다보니 손에 안익는것같다. 조금씩 계속 해야겠다.

## 참고

- [우아한테크\_stream](https://www.youtube.com/watch?v=rbm87IFpwvQ)
- [오라클\_stream](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html)
