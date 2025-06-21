## 파이썬 코드 가이드(PEPs 8)

> 이 글에서는 파이썬 코드 가이드로 유명한 PEPs 8에 대해 다룹니다.

## PEPs 가 뭐지? 🤔

파이썬 공식 문서에서는 다음과 같이 설명 되어 있습니다.

> [!NOTE]
> ✨ Python Enhancement Proposals (PEPs)  
> This PEP contains the index of all Python Enhancement Proposals, known as PEPs. PEP numbers are assigned by the PEP editors, and once assigned are never changed. The version control history of the PEP texts represent their historical record.

PEP은 Python enhancement Proposal의 약자로 각 첫글자를 따서 PEP으로 불립니다.
의미 그대로, 파이썬을 개선고자하는 제안서 입니다. PEP n 에 따라서 각 주제를 부여 받고 파이썬 코드를 개선시키는 방향에 대해서 토론합니다. 이글에서는 PEP8, `파이썬 코드스타일`에 대한 글을 작성합니다.

## PEP 8 – Style Guide for Python Code

> PEP 8 에서는 파이썬에서 권장하는 코드 스타일에 대해 말합니다.

### ⚠️ 일관성을 해치지 마세요.(A Foolish Consistency is the Hobgoblin of Little Minds)

> A Foolish Consistency is the Hobgoblin of Little Minds 문장을 직역하면 `줏대없는 일관성은 속좁은 홉고블린과 같다.` 라는 문장이 된다.
> PEP 8 를 말하기 이전 Guido(파이썬 창시자)는 다음 가이드로 인해 프로젝트 자체의 일관성을 해치는것은 좋지 않다는걸 말합니다.

다음 제공될 지침은 코드의 가독성을 향상시키고 광범위한 파이썬 코드에서 일관성을 유지하기 위한 것입니다. PEP20 에서도 설명하지만 `가독성이 중요합니다.`

### 코드 가이드.

#### 띄어쓰기

각 띄어쓰기 레벨은 스페이스를 4번 사용 합니다.

파이썬에서는 indent(간격)이 타 언어의 괄호를 대신합니다. 이를 통해 코드 스코프가 구분될 수 있도록 작성해야 합니다.

```python

```

## 참고

[Python 공식문서](https://peps.python.org/pep-0008/)
