-- indexing
CREATE INDEX idx_mission_bomb_damage_airborne
ON mission (airborne_aircraft, bomb_damage_assessment, target_country);


EXPLAIN ANALYZE SELECT bomb_damage_assessment, COUNT(target_country) FROM mission
	WHERE bomb_damage_assessment IS NOT NULL
	AND airborne_aircraft > 5
	GROUP BY target_country, bomb_damage_assessment
	ORDER BY COUNT(bomb_damage_assessment) DESC LIMIT 1