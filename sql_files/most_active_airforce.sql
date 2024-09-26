
--indexing
CREATE INDEX idx_mission_date_year
ON mission ((EXTRACT(YEAR FROM mission_date)));

CREATE INDEX idx_air_force
ON mission (air_force);


SELECT air_force, COUNT(*) AS mission_count
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
  AND air_force IS NOT NULL
GROUP BY air_force
ORDER BY mission_count DESC
LIMIT 1;