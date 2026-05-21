-- =========================
-- COUNT REVIEWS PER BANK
-- =========================
SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- =========================
-- AVERAGE RATING PER BANK
-- =========================
SELECT b.bank_name, AVG(r.rating) AS avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- =========================
-- CHECK NULL VALUES
-- =========================
SELECT *
FROM reviews
WHERE review_text IS NULL
   OR rating IS NULL
   OR review_date IS NULL;