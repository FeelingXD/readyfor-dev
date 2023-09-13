> "equals와 hashcode는 같이 재정의 되어야한다."

## 1. Java 에서 String은 왜 equals를 통해 값을 비교해야할까?

> Java를 처음 접했을때 적응 안되었던것들중 하나가 String을 비교할때는 <code>==</code> 등호 비교가아닌 <code>String.equals(str)</code> 메서드를 이용한 비교였다.

```java
String a =new String("동일성");
String b =new String("동일성");
System.out.println(a==b);// false
```

---

## 2. 동등성과 동일성 (identity and equality)

객체비교의 <code>==</code> 참조하는 메모리를 비교하게된다.(이글에서는 설명은 생략) 메모리가 같다면 이는 <code>동일성</code> 을 만족한다.

우리가 String 이나 기타 다른값을 비교할떄 문자열 값 자체의 비교를 원할것이다. 메모리가 다르더라도 값이 같은경우 즉 <code>동등</code> 한지 비교하고자 한다. 값의 일치여부를 동일성 이라한다

## 3. String의 equals는 어떤 구조일까?

Object class 에서 상속받은 equals 메소드를 String 은 다음과 같이 재정의 한다.

```java
//java 1.8에서 String 코드입니다.  이는 자바 버전에 따라 다를수도 있습니다. 😁
public boolean equals(Object anObject) {
      if (this == anObject) {
          return true;
      }
      if (anObject instanceof String) {
          String anotherString = (String)anObject;
          int n = value.length;
          if (n == anotherString.value.length) {
              char v1[] = value;
              char v2[] = anotherString.value;
              int i = 0;
              while (n-- != 0) {
                  if (v1[i] != v2[i])
                      return false;
                  i++;
              }
              return true;
          }
      }
      return false;
  }
```

코드를 짧게 분석해보자면 첫 if문에서는 동일성을 비교한다. 값빅교이전에 동일한 객체일경우는 항상 참이기때문이다.
두번째 if분기에서 instanceof 로 객체타입을 검사하고 String일 값을 char[] 배열로 순회하면서 동등성을 비교한다.

## 4.자바의 hashcode

자바 object는 각 고유의 hash코드를 가지며 이는 Object 클래스의 메서드를 오버라이딩해서 정의한다.

일반적으로 hashcode는 객체의 주소값을 변환하여 생성한 객체의 고유 정수값이 사용되며 두 객체가 동일 객체인지 비교 할 때 사용된다. (동일성)
hashcode를 사용하여 객체가 동일객체임을 비교하는데 단순값으로 비교하면 되므로 O(1) 시간복잡도로 비교할수있다.

### 4-1. hashcode는 어디서 사용될까?

HashMap,HashSet 등 JCF(Java Collection Framework) 에서 객체간의 동일성을 비교할때 사용된다.

### 4-2. hashcode를 정의하지 않았을떄 발생할수 있는 문제점.

```java
public class IDCard {
String owner;

@Override
public boolean equals(Object obj) {
    if (this==obj){
      return true;
    }
    if (obj instanceof IDCard){
      return this.owner.equals(((IDCard) obj).owner);
    }
    return false;
  }

}
```

테스트에 사용될 코드이다. 간단하게 IDCard라는 클래스를 생성했다. 이 클래스를 통해 equals와 hashcode에 관한 테스트 몇가지를 진행하려 한다.

```java
// 동등성테스트

 @Test
void equals_test(){
    //given
    IDCard a_card=new IDCard("지민");
    IDCard b_card=new IDCard("지민");
    //when
    assertEquals(a_card,b_card);
    //then
}

```

![](https://velog.velcdn.com/images/wlals425315/post/ac951fd5-420c-438a-a5e7-cca2e01f4289/image.png)

예상대로 잘통과한다.

```java
// set을 이용한 중복제거 테스트
@Test
void equals_noHashcode(){
    //given
  IDCard a_card=new IDCard("지민");
  IDCard b_card=new IDCard("지민");
    //when
  Set<IDCard> card_set=new HashSet<>();
  card_set.add(a_card);
  card_set.add(b_card);
  assertEquals(a_card,b_card);
  assertEquals(1,card_set.size());
}
```

equals로 비교했을때 같다(동등) 하기에 Set으로도 중복제거가 되어야 하는걸 생각햇다.
![](https://velog.velcdn.com/images/wlals425315/post/9b6d5077-dfa3-47e3-aa81-dc876233ba81/image.png)

#### 왜 같은값에대한 객체비교에서 중복제거를 하지못했을까?

간략하게 말하면 HashMap, HashSet 등은 객체의 hashcode를 이용해 먼저 객체를 비교하고 그후 equals 비교를 통해서 객체가 같은지여부를 판단한다. 즉 의사 코드는 다음과같다.

```java

 if (a.hashcode!=b.hashcode){
 	return false
 }
 else{
 	return a.equals(b)? true:false
 }

```

hashcode를 재정의 하지않을경우 상위 클래스인Object의 hash코드인 메모리값에의한 hashcode를 생성한다. 이경우 객체의 주소로 동일성을 체크하므로 동등성 비교이전에 hash코드에서 이미 같지않음이 판명나 다른값으로 판단한다.

### 4-3 예상동작이 되도록 hashcode또한 정의해주기

```java
public class IDCard2 extends IDCard{

public IDCard2(String owner) {
  super(owner);
}

@Override
public boolean equals(Object obj) {
  return super.equals(obj);
}

@Override
public int hashCode() {
  return this.owner.hashCode();
}
}
```

IDCard 클래스를 상속받는 IDCard2 클래스를 만들고 hashcode로는 String 인 owner를 사용함으로써 String.hashcode가 동작하도록했다.
![](https://velog.velcdn.com/images/wlals425315/post/5918cda2-4730-408e-8c65-d1f4acfb6014/image.png)
![](https://velog.velcdn.com/images/wlals425315/post/30736d99-28a1-4e88-b50d-2bcabcd072f3/image.png)

IDCard2를 사용한 객체는 각 owner의 이름이 같다면 같은 hashcode를 생성하도록 변경했다.이로 Set에서도 중복제거가 잘된 테스트를 결과를 확인할수 있었다.

### 결론

JCF(java colleciton framework)를 이용하기위해선 hashcode 재정의가 필수적이다. 만약 단순 객체만 사용할거라 hashcode 를 쓰지않는다면 정의하지않아도 당장의 코드상 문제를 일으키진 않겠지만 잠재적인 코드의 변칙성을 유발할것이다.

잠재적위험을 발견했는데 방치하는건 별로 좋지않다는 개인적인 생각이다.

추가적으로
Lombok 을 사용중이라면 @EqualsAndHashCode 어노테이션을 통해 간편하게 재정의할수있다.

---

## 참고한 글

- <a href="https://tecoble.techcourse.co.kr/post/2020-07-29-equals-and-hashCode/" target="_blank"> equals와 hashCode는 왜 같이 재정의해야 할까?</a>
- <a href="https://brunch.co.kr/@mystoryg/133" target="_blank"> 자바의 hashcode </a>

## 참고자료

- <a href="https://github.com/FeelingXD/java-playground/blob/main/src/test/java/org/example/equals_and_hashcode/IDCardTest.java" target="_blank"> 테스트코드</a>
