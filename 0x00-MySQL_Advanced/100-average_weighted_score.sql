-- Create the stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;
    SELECT SUM(c.score * p.weight) INTO weighted_sum
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    SELECT SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight = 0 THEN
        SET avg_score = 0;
    ELSE
        SET avg_score = weighted_sum / total_weight;
    END IF;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //

DELIMITER ;