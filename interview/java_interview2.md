# 문서중앙화 업체

## 필기시험

> 약 10 문제 가량 출제 된것으로 기억한다. 일부분 기억나는 내용을 정리한다.


1. Java Class의 초기화 변수 문제
```Java
class Main{

    public static String aValue = "b";
    public String bValue = "b";

    static{
        aValue+='a';
    }
    {
        aValue+='b';
        bValue+='b';
    }
    public Main(){
        aValue+='d';
        bValue+='d';
    }
    public static void main(String[] args){
        Main main=new Main();
        main.append();
        System.out.println(main.aValue);
        System.out.println(main.bValue);
        
    }

    public void append(){
        this.aValue+='c';
        this.bValue+='c';
    }

}
```

> [!Note]
> 클래스의 변수 초기화는 변수에 할당 된값 -> static 초기화 블럭 -> instance 초기화 블럭 순서가 실행된다.

2. Java Exception 처리
```Java
try{
    // 1 
}catch() // 2 
finally
{
 // 3
}
/**
 * 각 상황이 주어졌을때 어떤순서로 실행되나? 
 *
 * 1. 정상실행시
 * 2. try에서 exception 발생시
 * 3. catch 내부에서 throw 할 시
 * 4. catch 와 finally 내부에서 throw 할 시
 */
void exception_seq1(){
        log.info("seq1");
        try{// case 1
            log.info("try");
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    void exception_seq2(){ // try 쓰루시
        log.info("seq2");
        try{//case2
            log.info("try");
            throw new RuntimeException();
        }catch (Exception e){
            log.info("catch");
            e.printStackTrace();
        }finally{
            log.info("finally");
        }
    }
    void exception_seq3(){
        log.info("seq3");
        try{// case3
            log.info("try");
            throw new RuntimeException();
        }catch (Exception e){
            log.info("catch");
            throw new RuntimeException();
        }finally{
            log.info("finally");
        }
    }
    void exception_seq4(){
        log.info("seq4");
        try{// case4
            log.info("try");
        }catch (Exception e){
            log.info("catch");
            e.printStackTrace();
        }finally{
            log.info("finally");
            throw new RuntimeException();
        }
    }
 
```
3. 소수합 문제 
```Java
@Test
    void sum_prime_number(){
        //given
        var ans =0;
        for(int i=1;i<=1000;i++){
            if (isPrime(i))
                ans+=i;
        }
        log.info(String.valueOf(ans));
        //when

        //then
    }
    public boolean isPrime(int n){
        if (n==1)
            return false;
        for(int i=2;i<n;i++){
            if (n%i==0)
                return false;
        }
        return true;
    }
```
4. InputStream 관련 fileleak

InputStrema 관련 fileleak 이 발생하는지의 여부를 체크

>[!Note]
관련 링크 첨부 [네이버 블로그](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=websearch&logNo=221930525766)

5. SQL 문제

부서 간 평균 연봉 구하고 평균이 x 이상인 부서 출력

```SQL
-- 코드를 작성해주세요
SELECT E.DEPT_ID AS DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(SAL),0) AS AVG_SAL
    FROM HR_EMPLOYEES AS E
    JOIN HR_DEPARTMENT  AS D
        ON E.DEPT_ID =D.DEPT_ID
    GROUP BY E.DEPT_ID 
    ORDER BY AVG_SAL DESC
```