## 레포지토리 별로 사용 이메일 설정하기

```bash
git config user.email # 현재 설정되어있는 이메일확인
git config --local user.email "exampleEmail@gmail.com" # 사용할 이메일 입력하기
git config --global push.autoSetupRemote true # 브랜치 작업 push 시 upstream 지정하지않고 자동 origin/{브랜치명} 되도록 설정
```


