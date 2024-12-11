-- 코드를 입력하세요
SELECT DISTINCT i.FLAVOR FROM FIRST_HALF as f
JOIN ICECREAM_INFO as i
on i.flavor = f.flavor
WHERE i.INGREDIENT_TYPE = "fruit_based" and f.TOTAL_ORDER > 3000
