SELECT air_force, COUNT(*) AS mission_count
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
  AND air_force IS NOT NULL
GROUP BY air_force
ORDER BY mission_count DESC
LIMIT 1;