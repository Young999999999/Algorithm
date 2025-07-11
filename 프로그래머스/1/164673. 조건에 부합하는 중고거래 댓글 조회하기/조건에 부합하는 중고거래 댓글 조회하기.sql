-- 코드를 입력하세요
SELECT TITLE,BOARD_ID,REPLY_ID,WRITER_ID,CONTENTS,CREATED_DATE
FROM(
SELECT b.TITLE,b.BOARD_ID,r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE,"%Y-%m-%d") as CREATED_DATE,b.CREATED_DATE as bc
FROM USED_GOODS_BOARD b 
JOIN USED_GOODS_REPLY r 
ON b.BOARD_ID = r.BOARD_ID) sub
WHERE bc like "%2022-10%"
ORDER BY sub.CREATED_DATE ASC, sub.TITLE ASC ;
