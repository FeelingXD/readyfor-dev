---
theme: gaia
_class: lead
paginate: true
height: 100%
title: 
color: #000
backgroundColor: #fff
backgroundImage: url('https://www.duranno.com/gospelproject/data/8551/2%EB%8B%A8%EC%9B%90%20%EB%B0%B0%EA%B2%BD%20%EC%9D%B4%EB%AF%B8%EC%A7%80.jpg')
marp: true
---

# **Criteria**

`코드`로 `쿼리` 를 구성하는 API



---
# 1. Criteria API 

Criteria API는 Java Persistence API (JPA)의 일부로, 프로그래밍 방식으로 데이터베이스 쿼리를 생성하는 API입니다.

- 타입 안전성 보장
- 동적 쿼리 생성 용이성
- 객체 지향적 쿼리 작성입니다.

---

# Criteria 기초
```Java
public class Item implements Serializable {

    private Integer itemId;
    private String itemName;
    private String itemDescription;
    private Integer itemPrice;
}
```
```Java
Session session = HibernateUtil.getHibernateSession();
CriteriaBuilder cb = session.getCriteriaBuilder();
CriteriaQuery<Item> cr = cb.createQuery(Item.class);
Root<Item> root = cr.from(Item.class);
cr.select(root);

Query<Item> query = session.createQuery(cr);
List<Item> results = query.getResultList();
```
---
# JPA 를 이용한조회 -1

![bg left 50%](https://i.namu.wiki/i/prluxbmek2GiALL9y0wpE90q1Phd5m8m-MCK1KpyZLyi_a6Xykw_TG1ZIx2PDOfe30IgG-Il8boBfa0YNVfsCmAVirhTAhmgD1swDdLh6xUvIh1Kozj9PMkxGq73J2pO3bthlDxMJy1fMLNZRyzjtg.webp)

---
# JPA 를 이용한조회 -2

|칼럼|타입|설명|
|------|---|---|
|id|Long|인덱스 번호|
|price|Int|가격|
|weight|Double|무게(kg)|
```kotllin
// 

@Repository
interface MenuRepository: JpaRepository<WaterMelon,Long>{
    fun findByLessThanPrice(price : Long)
    fun findByLessThanPriceAndGreaterThanWeight(price: Long,weight:Double)  
}
```

---
# Criteria 사용법과 이점


---
# QueryDsl vs Criteria

Criteria API와 QueryDSL은 모두 타입 안전한 동적 쿼리 생성을 위한 도구이지만, 몇 가지 차이점이 있습니다



---
# khipster Criteria

위즈에서 사용하는 blueprint 툴인 khipster 또한 criteria를 지원합니다.


