-- this cmmd list all the rows with the score is the same
-- ordred with desc
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
