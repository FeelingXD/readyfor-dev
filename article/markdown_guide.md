# 마크다운 가이드 🎨

> 이 글에서는 마크다운 문법에대해 설명합니다.
> 이글은 github markdown style 기반으로 작성 되어 있습니다.
> markdown을 이용하는 서비스에 따라 아래 문법이 지원되지 않을 수 있습니다.

## 마크다운 시작하기 👍

마크다운을 시작하는데 별도의 프로그램이 필요하지 않습니다. 메모장, 웹 어디서든 가능 하니까요! 하지만 VSC 같은 IDE 하면 작성된 마크다운을 미리볼수 있답니다.

## 마크다운 문법

### 헤더

- 제목 과 부제

```
This is title
============  (1개 이상 입력시 적용됨)

This is subtitle
------------ (1개 이상 입력시 적용됨)
```

# This is title

## This is subtitle

- 글머리 (Html 의 글머리 태그)

```
(# 의갯수로 크기를 지정하며 많아질수록 크기가 줄어드며 최대 6개까지 지원합니다.)
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
```

# This is a H1

## This is a H2

### This is a H3

#### This is a H4

##### This is a H5

###### This is a H6

---

### 표현

- 글의 표현

```
   **bold text** (굵게)
   __BOLD TEXT__ (굵게)
   *italicized text* (이테릭체, 기울이기)
   `Code` (코드표현, 강조)
   ~~취소하기~~ (취소선 ~~ 로감싸준다)
```

**bold text** (굵게)  
**BOLD TEXT** (굵게)  
_italicized text_ (이테릭체, 기울이기)  
`Code` (인라인 코드, 강조)  
~~취소하기~~ (취소선)

### 리스트

- 순서 리스트

```
  다음과 같이 표현
  1. 1번 원소
  2. 2번 원소
  3. 3번 원소
```

1. 1번 원소
2. 2번 원소
3. 3번 원소

- 순서가 없는 리스트

```
github에서는 -, * , + 를 지원하며 (기본적으로 '-')
다음과 같이 표현 할수있음

- 강아지
    - 고양이
        - 토끼

혼용해서 사용할수도 있다.

* 심리학
    -  철학
        + 인문학
```

- 강아지
  - 고양이
    - 토끼

* 심리학
  - 철학
    - 인문학

### 코드 표현

#### 인라인코드

```
    `(백틱) 으로 감싸서 표현
    `var B` = 1
```

`var B` = 1

#### 코드블럭

기본적으로 \```(백틱 3개로 감싸는것으로 코드블럭을 표현할 수 있다.)

추가적으로 탭 혹은 4개의공백으로 시작할수있다.

````
    1. ```(백틱 3개)으로 감싸는 방법
    ```
        first way to write codeblock
    ```

    2. 공백으로 시작하는방법

        this is secont way to write codeblock

````

1.  `(백틱)으로 감싸는 방법

    ```
        first way to write codeblock
    ```

2.  공백으로 시작하는방법

        this is secont way to write codeblock

> 코드블럭 의 하이라이트 기능

````
    다음과같이 코드블럭의 코드를 강조표현할 수 있다.
    ```(사용 언어 기본적으로 는 plain text로 표현된다.)
        ~~~ 코드
    ```
    ```python
        # 파이썬 문법으로 하이라이트 됩니다.
        print("Hello MarkDown!")
    ```
````

```(사용 언어 기본적으로 는 plain text로 표현된다.)
        ~~~ 코드
```

```python
    #파이썬 문법으로 하이라이트 됩니다.
    print("Hello MarkDown!")
```

### 링크 표현

마크다운을 사용해서 html 의 \<a> 태그처럼 웹링크나 이미지를 가져올수있다.

```
    # 웹링크
    [구글](google.co.kr) 로 이동하기.

    # 이미지 표시(웹링크와 유사하지만 괄호앞에 !를 붙여준다)
    ![SAMPLE_IMG](https://velog.velcdn.com/images/wnet500/post/cca8765f-0b17-40bb-b79d-b02e54643138/velog_%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF.002.jpeg)

    # 태그를 감싸 인라인으로 표현할수도있다.
    인라인 표현
    네이버 주소 : <http://naver.com>

    # 상대 참조
    변수를 사용하는것처럼 상대참조 할수있다. (반복적으로 사용한다면 훨씬 편한다. 다만 붙여서 쓸경우 인식이 안될수있어 줄바꿈 하는걸 권장합니다.)
    [구글][GoogleLink]

    [GoogleLink]: http://google.co.kr 구글링크

```

[구글](google.co.kr) 로 이동하기.

![SAMPLE_IMG](https://velog.velcdn.com/images/wnet500/post/cca8765f-0b17-40bb-b79d-b02e54643138/velog_%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF.002.jpeg)

네이버 주소 : <http://naver.com>

변수를 사용하는 것 처럼 상대참조 할수있다.

[구글][GoogleLink]

[GoogleLink]: http://google.co.kr

### 인용구(QuoteBlock)

```
    # 인용구는 '>' 키워드로 시작할수 있으며 중첩 인용구도가능 합니다.

    > 인용구 테스트입니다.

    >
    > > 중첩인용구는 다음과같이 표기됩니다.
```

---

> 인용구 테스트입니다.

---

> 외부 인용구 입니다.
>
> > 중첩인용구는 다음과같이 표기됩니다.

### 맺음말 및 참고한글들

> 마크다운을 지원한다면 공유되는 기능들을 모아서 작성 했습니다. 😅
> github 마크다운은 지원하나 안되는곳이 있을 수 있습니다.
> 마크다운은 누구나 쉽고 기타 에디터 서비스를 이용하지 않더라도 글쓰기 를 쉽게만들어주는 강력한 마크업 입니다. 😂 티스토리에서도 지원하나 몇가지 아쉬운점은 개선됬으면 싶습니다.

#### 참고문헌

- [마크다운 사용법](https://gist.github.com/ihoneymon/652be052a0727ad59601)
- [markdown guide](https://www.markdownguide.org/)
