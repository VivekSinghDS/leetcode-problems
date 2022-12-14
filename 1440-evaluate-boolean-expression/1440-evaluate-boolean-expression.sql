WITH CTE AS (
    SELECT left_operand, operator, right_operand, (SELECT value FROM Variables WHERE name = left_operand) AS left_operand_value, (SELECT value FROM Variables WHERE name = right_operand) AS right_operand_value FROM Expressions
)
SELECT left_operand, operator, right_operand,
CASE
    WHEN operator = "<" THEN IF(left_operand_value < right_operand_value,"true","false")
    WHEN operator = ">" THEN IF(left_operand_value > right_operand_value, "true", "false")
    ELSE IF(left_operand_value = right_operand_value, "true", "false")
END AS value
FROM CTE;