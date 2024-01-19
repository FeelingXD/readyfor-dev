> Java 9 이후로 GC(Garbage Collector) 의 표준이 된 G1GC에 대해 작성하는 글 입니다.

## G1GC: Garbage 1(first) Garbage Collector

G1GC 는 이름에서 알수 있듯 가바지 수집이 최우선이 되는 가비지 컬렉터입니다. Java9 부터 Java 진영의 표준 GC 모델이 되었으며 다읍과 같은 특징이 있습니다.

- 쓰레기로 가득찬 heap 영역을 집중적으로 수집
- 큰메모리를 가진 멀티 프로세서 시스템에 사용하기 위해 개발된 GC이다.
- G1GC는 일시정지시간(STW)을 최소하 하면서, 가능한 처리량도 확보하는것이 G1GC의 목표이다.
- G1 은 통계를 계산해가면서 GC 작업량을 조절한다.

다음 상황일때 G1GC를 사용하는데 도움이됩니다.

- HEAP의 50% 이상 라이브 데이터일때
- GC가 너무 오래걸릴때

## G1GC 의 영역

G1GC의 힙 레이아웃은 기존에 있던 다른 가비지 콜렉터와 차이가있다.  
G1GC는 전체 HEAP을 체스판, 바둑판 처럼 여러 영역 으로 나누어 관리한다.  
각 체스판은 다음과 같은 영역들로 나뉜다.

![G1GC_HEAP](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQj1gp%2FbtsDDYp41RZ%2FFr5CB0Dz8ABmm8VJfZBdu1%2Fimg.png)

영역은 다음과 같은 역할을 한다.

- EDEN : 새로운 객체가 할당되면 이곳에 생성한다.
- SURVIVOR : 기존 S1,S0 등 두 부분으로 존재하던 이전의 가비지컬렉터에서 G1GC에서는 하나로 관리되며 HEAP 영역에 연속되지않게 있음 EDEN 영역에서 살아남은 객체들이 이곳으로 이동된다..
- OLD : SURVIVOR 영역에서 몇번이상(임계값) 살아남은 객체가 이곳으로 이동한다.
- HUMONGOUS : REGION의 50% 이상의 큰 객체 는 일반영역에 맞지않아 HUMONGOUS 라는 영역에 배치되며 일반적인 REGION보다 클수있습니다. 해당영역은 별도로 관리된다. (다른 REGION 과 다르게 연속된 공간을 사용하고, 만약 메모리상 자투리공간이 남더라도 사용하지않는다.)
- AVAILABE: 아직 사용되지 않은 REGION을 뜻 한다.

## G1GC 의 사이클

![G1GC_CYCLE](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FoigWL%2FbtsDDdguVnu%2FZTktRNNDTW0njaegVljt2K%2Fimg.png)

G1GC는 다음과 같은 사이클을 순회한다.  
파랑원 은 Minor GC 를 의미하고  
주황원 은 Major GC 를  
붉은원 은 MIXED GC 를 의미한다.  
각 원의 크기만큼 STW(STOP THE WORLD) 가 발생 한 것이다.

1.  Young-only phase: Old gen occupancy exceeds threshold 이전단계로 Old 영역이 임계값 이전이라면 MINOR GC가 실행된다.
2.  Young-only phase with InitialMark : YoungGC와 동시에 일어나는
3.  space-reclamation : Concurrent Marking Cycle이 일어난 후 Young/Old 영역의 Evacuation을 진행하는 페이즈이다. G1GC는 PauseTime을 적게 가져가기 위해 MixedCollection이 짧게 여러번 일어난다.

## YOUNG GC (MINOR GC)

기존 GC와는 다른구조를 띈다 이전 GC에서는 연속적인 메모리구조를 보이지만 G1GC에서는 체스판 배열(비연속된 구조) 를 띄운다.

![MINOR_GC_1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcJNqUv%2FbtsDJmbZsd3%2FqwdTvFLzcuJUT0rhXRgfP1%2Fimg.png)

EDEN 영역에서 살아있는객체들이 SURVIVOR 영역으로 EVACUATION(이동 혹은 복사) 된다 만약 여러번 살아남은객체이면서 임계값에 도달했다면 몇몇 객체는 OLD 영역으로 이동한다(승격)

이과정에서 어플리케이션이 멈추는 STW가 발생한다.

![MINOR_GC_2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkLsw5%2FbtsDDcPWn4r%2FDlnJNeZwzmaliNQbKg3XCk%2Fimg.png)

살아남은 객체가 이동되고 필요없어진 공간은 비우면서 COMPACTION(압축) 된다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbOcOut%2FbtsDEjBlgcc%2FTVFSjwZUCxNIAMeSARNkc1%2Fimg.png)

## OLD GC (MAJOR GC)

![OLD_GC_SEQ](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWAdUa%2FbtsDIv8t3md%2F8QjliDvKJrK7bYbifvrXeK%2Fimg.png)

OLD GC는 다음 단계를 따른다. STW 는 STOP THE WORLD 의 약자로 어플리케이션이 중지되는 단계를 표시했다.

1.  초기 마킹 (Initial mark,STW) : OLD 영역 에 존재하는 객체들이 참조하는 SURVIVOR REGION을 찾음
2.  ROOT공간 탐색(Root region Scanning) : 1.에서 찾은 SURVIVOR REGION 에대한 GC대상 스캔작업을 진행
3.  동시 마킹(Concurrent Marking) : 힙 전체의 REGION 에대해서 스캔작업을 진행하며 GC대상이없는 REGION은 이후 단계에서 제외된다.
4.  재마킹 (Remark,STW) : 최종적으로 GC대상에서 제외될 객체를 선별한다.
5.  비우기 (CleanUp,STW) : 살아있는 객체가 가장 적은 지역(REGION) 의 미사용객체 를 제거하고 GC 과정에서 완전히 비워진 REGION 을 FREELIST로 등록한다. 위의 그림에서는 avilable 지역상태로만든다.
6.  복사 (Copyping,STW) : CleanUp 에서 살아남은 객체들을 새로운 region에 복사하고 compaction을 진행함

## 참고한글

---

[G1GC gabage collector](https://blog.leaphop.co.kr/blogs/42)  
[Oracle G1GC 레퍼런스](https://www.oracle.com/technical-resources/articles/java/g1gc.html)  
[Java's G1](https://www.youtube.com/watch?v=2PIBF92iOvQ)  
[G1 TUTORIAL](https://www.oracle.com/technetwork/tutorials/tutorials-1876574.html)
