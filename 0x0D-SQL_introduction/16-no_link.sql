-- this cmmd list all rows having a name value
-- ordred descending
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
