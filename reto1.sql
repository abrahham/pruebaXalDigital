/*
	1. Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?

	*** en el documento PDF en la tabla aeropuerto sale el atributo nombre_aerolinea, pero supongo que se refería a nombre_aeropuerto ***
*/
SELECT nombre_aeropuerto,(SELECT COUNT(id_movimiento) FROM movimientos WHERE id_aeropuerto = a.id_aeropuerto) AS cant FROM aeropuertos a ORDER BY cant DESC LIMIT 0,1;

/*
	2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante
	el año?
*/

/*Tomando en cuenta que un vuelos es un movimiento donde haya 'salida' */
SELECT nombre_aerolinea, 
	(SELECT COUNT(id_aerolinea) FROM vuelos v WHERE id_aerolinea = a.id_aerolinea AND id_movimiento = (SELECT id_movimiento FROM movimientos WHERE descripcion = "SALIDA")) as vuelosHechos
	FROM aerolineas a ORDER BY vuelosHechos DESC LIMIT 0,1;

/* 
	Si se tomaran como vuelos tanto entradas como salidas el siguiente script abarcaría los dos puntos
	
	SELECT nombre_aerolinea, (SELECT COUNT(id_aerolinea) FROM vuelos v WHERE id_aerolinea = a.id_aerolinea) as vuelosHechos FROM aerolineas 	a WHERE vuelosHechos ORDER BY vuelosHechos DESC LIMIT 0,1;

*/
 
 
/*
	3. ¿En qué día se han tenido mayor número de vuelos?
*/
SELECT dia,COUNT(id_movimiento) AS vuels FROM vuelos v WHERE id_movimiento = (SELECT id_movimiento FROM movimientos WHERE descripcion = "SALIDA") GROUP BY dia ORDER BY vuelos DESC LIMIT 0,1
/*
	Si se tomaran como vuelos tanto entradas como salidas el siguiente script abarcaría los dos puntos
		
	SELECT dia,COUNT(id_movimiento) AS vuels FROM vuelos v GROUP BY dia ORDER BY vuelos DESC LIMIT 0,1
*/

/*
	4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?
*/
SELECT nombre_aerolinea, (SELECT COUNT(id_movimiento) FROM vuelos WHERE id_aerolinea = a.id_aerolinea) as movs FROM aerolineas a HAVING movs > 2;



