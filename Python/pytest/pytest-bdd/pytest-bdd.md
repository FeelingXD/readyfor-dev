### Pytest BDD


### BDD(Behavior-Driven-Developemnt ) ?

행동 주도 개발(Behavior-Driven Development, BDD)은 개발자와 비즈니스 이해관계자 간의 협업을 강화하고 소프트웨어의 품질을 높이는 데 초점을 맞춘 접근 방식입니다.

행동 주도 개발은 TDD(Test-Driven Development)의 파생으로 비즈니스 요구사항을 자연어 (개발자가 아니더라도 이해할수 있도록) 표현하고 개발과 테스트를 진행하는 방법입니다.

### BDD 와 Gherkin

Gherkin은 **비즈니스 읽기 가능한 도메인 특화 언어(DSL)**로, 소프트웨어의 동작을 자연어에 가까운 형태로 기술할 수 있게 해주는 언어입니다. 주로 **BDD(Behavior Driven Development)**와 함께 사용됩니다.

#### 기본구조 

```Gherkin
Feature: 
    Background: <선행작업 혹은 환경>
    Scenario: <시나리오 이름>
        Given: <주어진 데이터 혹은 조건>
        when: <특정 상황>
        then: <발생할 결과>
```