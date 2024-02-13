-- displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)

SELECT city, AVG(value) AS temps
FROM temperatures
GROUP BY city
ORDER BY temps DESC;
