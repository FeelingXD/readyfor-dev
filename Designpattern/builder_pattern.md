## 빌더 패턴 🔨

> 빌더패턴 은 디자인 패턴중 생성 패턴으로
> 생성 과정과 표현과정을 분리하고 다양한 구성의  
 `인스턴스` 를 만드는것을 목적으로합니다.  
> 


### 빌더 패턴의 개념

빌더 패턴은 복잡한 객체들을 `단계별`로 생성 할 수있도록 하는 패턴입니다.


#### 대표적으로 사용되는 생성 패턴들

1. 점층적 생성자 패턴
- 생성자를 매개변수에 개수만큼 구성하는 패턴을 의미합니다.
```java
class Person{
    private String name;
    private String nickname;
    private String email;
    
    public Person(String name){
        this(name,null,null);
    }

    public Person(String name, String nickname){
        this(name,nickname,null)
    }
    public Person(String name, String nickname, String email){
        this(name,nickname,email)
    }
}
```
- 매개변수가 많아질수록 그만큼 커스텀 생성자를 추가적으로 생성해야 합니다.
- 내부필드에 동일한 타입의 클래스가 존재할 경우 `모호`한 표현을 야기할 수 있습니다.

---

2. 자바빈즈 패턴
- 별도의 생성자 없이 빈 객체를 생성하고 인스턴스의 필드를 채워주는 형태의 패턴입니다.
위의 클래스 에서 만든 `Person` 클래스를 재활용 하겠습니다.
```java
class Person{
    private String name;
    // 기타 필요 필드들
    public Person()

    public setName(String name){
        this.name= name;
    }
    // 각 필요한 필드의 세터들
}

class main{
    public static void main(String args[]){
        Person person= new Person()
        person.setName("새로운 이름");
    }
}
```
- 불필요한 생성자를 추가적으로 작성하지 않아도 되어서 작성할 코드 량이 줄어듭니다.
- `필수` 적으로 사용되야하는 필드를 객체 생성 이후 초기화 하기에 실수 할 수 있습니다.
- 필드의 set이 열려있어 객체 필드가 변할 수 있습니다.


### 빌더패턴 알아보기 😊

```Java
class Person{

    private String name;
    private String nickname;
    // private 생성자를 지정하여 생성자 생성 방지
    private Person(){}
    public static builder(){
        return new PersonBuilder()
    }
}
// 생성을 빌더패턴에서 담당하게됩니다.
class PersonBuilder{

    public PersonBuilder name(String name){
        this.name= name;
        return this
    }

    public PersonBuilder nickname(String nickname){
        this.nickname= nickname
        return this
    }
    public Person build(PersonBuilder builder){
        Person person = new Person()
        // 각 person 필드설정
        person.name = builder.name
        return person
    } 
    // 최종적으로 build 메서드를 통해 Person객체를 생성합니다.
    public Person build(){
        return build(this)
    } 
}
```

실제 사용하는 곳에서는 다음과 같이 사용된다.

```java

public static void main(){
    Person person = Person.Builder()
    .name("이름")
    .build()
}
```

> 빌더패턴의 장점
- 명시적으로 어떤필드에 어떤 값이 들어갈지 개발자가 파악하기 용이합니다.
- 실제 사용하는 객체에서 Setter와 생성자를 사용하지 않으므로써 객체가 변경되거나 생성시 실수가 줄어듭니다.

> 단점
- 필수값으로 생성해야하는 필드들을 누락할 위험이 있습니다.