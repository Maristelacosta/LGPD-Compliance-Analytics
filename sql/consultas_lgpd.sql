SELECT
tipo,
COUNT(*) AS total
FROM incidentes
GROUP BY tipo;
