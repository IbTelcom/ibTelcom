insert into ib_telcom.servicios_estado (idEstado, nombreEstado) values
(1, "Aguascalientes"),
(2, "Baja California"),
(3, "Baja California Sur"),
(4, "Campeche"),
(5, "Coahuila"),
(6, "Colima"),
(7, "Chiapas"),
(8, "Chihuahua"),
(9, "CDMX"),
(10, "Durango"),
(11, "Guanajuato"),
(12, "Guerrero"),
(13, "Hidalgo"),
(14, "Jalisco"),
(15, "Estado de MÃ©xico"),
(16, "MichoacÃ¡n"),
(17, "Morelos"),
(18, "Nayarit"),
(19, "Nuevo León"),
(20, "Oaxaca"),
(21, "Puebla"),
(22, "Querétaro"),
(23, "Quintana Roo"),
(24, "San Luis Potosí"),
(25, "Sinaloa"),
(26, "Sonora"),
(27, "Tabasco"),
(28, "Tamaulipas"),
(29, "Tlaxcala"),
(30, "Veracruz"),
(31, "Yucatán"),
(32, "Zacateca");

insert into ib_telcom.servicios_municipio (nombreMunicipio, idEstadoFK_id) values
("SANTA ROSA",	22),
("DOCTOR MORA",	11),
("DOLORES HIDALGO",	11),
("SAN JOSÉ ITURBIDE",	11),
("SAN LUIS DE LA PAZ",	11),
("SAN MIGUEL DE ALLENDE",	11),
("TIERRA BLANCA",	11);

insert into ib_telcom.servicios_colonia (nombreColonia, idMunicipioFK_id) values
("VERSOLILLA", 1),
("LUZ", 1),
("PALMA", 1),
("RINCON DE OJO DE AGUA", 1),
("PALO ALTO", 1),
("DOCTOR MORA", 2),
("BEGOÑA", 2),
("CERRITO", 2),
("COLONIA CANTERA", 2),
("DERRAMADERO DE CHARCAS", 2),
("DERRAMADERO DE EN MEDIO", 2),
("DONCELLA", 2),
("DURAZNOS", 2),
("DURAZNOS DE ARRIBA", 2),
("EJIDO VAGUI", 2),
("ESTANCIA", 2),
("LA FORTUNA", 2),
("JESUS MARIA", 2),
("LAS FLORES", 2),
("MORISQUILLAS", 2),
("NORIA", 2),
("OBRAJITOS DE ABAJO", 2),
("PRESA DEL GATO", 2),
("PALMA", 2),
("PEÑA RODADA", 2),
("PURISIMA", 2),
("RANCHITO DE SAN JOSÉ", 2),
("SAN AGUSTIN", 2),
("SAN RAFAEL", 2),
("VAGUI", 2),
("SAN PEDRO PALO MACHO", 3),
("SAN JOSÉ ITURBIDE", 4),
("COLONIA LA CANTERA", 4),
("VIVORILLAS", 4),
("COLONIA RINCONADA DE LOS ANGELES", 4),
("ADJUNTAS", 4),
("ARROLLO ONDO DE SAN DIEGO DE LAS TRASQUILAS", 4),
("ATONGUITO", 4),
("BORDO EL CAPULIN", 4),
("BUENAVISTILLA", 4),
("CANELA", 4),
("CAPULIN", 4),
("CHAVEZ", 4),
("CIENEGA DEL CAPULIN", 4),
("COLONIA CINCO DE MAYO", 4),
("CINTA", 4),
("COLONIA BUENA VISTA", 4),
("COLONIA LOMAS DE GUADALUPE", 4),
("COLONIA PINITO", 4),
("COLORADO", 4),
("CONCEPCION", 4),
("CONCHA", 4),
("CONSTRUCTURA Y FRACCIONAMIENTO CAMPESTRE NO. 4", 4),
("CRUZ DE LA MASA", 4),
("CRUZ DE LA MAZA/CONCHA", 4),
("EL NACIMIENTO", 4),
("EL SALITRE", 4),
("ENCINOS", 4),
("ESCONDIDA", 4),
("ESTANCIA", 4),
("FRACCIONAMIENTO CERRO BLANCO", 4),
("GALOMO", 4),
("JARALILLO", 4),
("JARDIN DE LOS ARROYOS", 4),
("LA ASCENCION", 4),
("LA CANTERA", 4),
("LOMAS DEL CALVARIO", 4),
("LOMAS DEL VERGEL", 4),
("LOS RODRIGUEZ", 4),
("LOS VEGA DE ARRIBA", 4),
("MASTRANTO", 4),
("MEDINA", 4),
("MIRANDA", 4),
("PALMITA", 4),
("POZO BLANCO DE GALOMO", 4),
("POZO BLANCO DEL CAPULIN", 4),
("PRADOS DEL ROSARIO", 4),
("PUEBLO NUEVO", 4),
("PUERTO CARRZA", 4),
("RANCHO LARGO", 4),
("RANCHO NUEVO LA VENTA", 4),
("RANCHO VIEJO", 4),
("REAL DE SAN JOSE", 4),
("SAN ANTONIO DEL LLANO", 4),
("SAN ANTONIO VIVORILLAS", 4),
("SAN DIEGO DE LAS TRASQUILAS", 4),
("SANTA ANITA", 4),
("SANTA BRIGIDA", 4),
("SAUCITO", 4),
("SOLEDAD", 4),
("TEPOZANES", 4),
("TERREROS", 4),
("TULILLO DE ABAJO", 4),
("TULILLO DE ARRIBA", 4),
("BOLUDO", 5),
("SAN CRISTOBAL", 5),
("CHARCO", 5),
("DERRAMADERO SEGUNDO (INFIERNILLO)", 5),
("DOLORES", 5),
("EL CARMEN DE LOS VEGA", 5),
("ESPINAS BLANCAS", 5),
("ESTACION DE LOURDES", 5),
("FRACCION DE LOURDES", 5),
("GARIBALDI", 5),
("HUERTA", 5),
("HUERTA 1", 5),
("INFIERNILLO", 5),
("INFIERNILLO SAN ANTONIO SEGUNDO", 5),
("LAGUNA", 5),
("LUZ", 5),
("MERCED", 5),
("MISION DE ARRIBA", 5),
("POZOS", 5),
("PUERTO BLANCO", 5),
("PUERTO BLANCO 2", 5),
("RANCHO DE JALAPA (PRESA VAQUEROS)", 5),
("RANGELES", 5),
("REFUGIO", 5),
("SAN ANTONIO PRIMERO", 5),
("SAN ANTONIO SEGUNDO", 5),
("SAN CRISTOBAL", 5),
("SAN ERNESTO", 5),
("SAN JOSE DE GUERRERO", 5),
("SANTANA Y LOBOS", 5),
("SAUZ", 5),
("VALLE DE GUADALUPE", 5),
("VAQUEROS", 5),
("CALERA", 6),
("CRUCES", 6),
("FRAILE", 6),
("SAN JOSÉ DE VIBORILLAS", 6),
("TRES PALMAS", 6),
("TRES PALMAS DE ARRIBA", 6),
("AGUILA", 6),
("VALDERAS", 6),
("BEGOÑA DEL PROGRESO", 6),
("CAÑADA DE LAS FLORES", 6),
("CARMEN", 6),
("CLAVELLINAS", 6),
("COLORADO", 6),
("CORRAL DE PIEDRA", 6),
("CORRAL DE PIEDRAS DE ARRIBA", 6),
("EL ROSARIO (RANCHO PRIVADO)", 6),
("ESTANCIA DE SAN ANTONIO", 6),
("FRACCIONES", 6),
("GUADALUPE DE BARCENAS (SAUZ)", 6),
("HOYOS", 6),
("JESUS MARIA", 6),
("LA LUZ DE SAN MIGUELITO", 6),
("LAGUNA ESCONDIDA", 6),
("LANDETA", 6),
("LOMA DE CABRAS", 6),
("LOMA DE COCINAS", 6),
("LOS REYES", 6),
("LOS RODRIGUEZ", 6),
("MARAVILLAS", 6),
("MARROQUIN CHIQUITO", 6),
("MASTRANTO", 6),
("MEDINA", 6),
("PALMILLA", 6),
("PAREDON", 6),
("PASO DE CABRAS", 6),
("PEDREGAL DE JERICO", 6),
("PEÑON DE LOS BAÑOS", 6),
("POZO DE LICEA", 6),
("PROVIDENCIA DE URBINA", 6),
("PUERTA", 6),
("PUERTO DE SOSA", 6),
("RANCHO SIETE HERMANOS", 6),
("RANCHO BONITO", 6),
("RANCHO NUEVO DE GAVILANES", 6),
("SAN ANTONIO", 6),
("SAN ANTONIO SEGUNDO", 6),
("SAN CRISTOBAL", 6),
("SAN ERNESTO", 6),
("SAN FRANCISCO", 6),
("SAN FRANCISCO DEL FRAILE", 6),
("SAN JOSE DE LA AMISTAD", 6),
("SAN JOSE DE GRACIA", 6),
("SAN JOSE DE LA CRUZ (TRES PALMAS)", 6),
("SAN JOSE DE LAS PALMAS", 6),
("SAN JOSE DE VIVORILLAS", 6),
("SAN JUAN", 6),
("SAN JUAN LOS TREJOS", 6),
("SAN MARTIN DEL PAREDON", 6),
("SAN MIGUELITO", 6),
("SAN RAFAEL", 6),
("SAN RAFAEL EL CHICO", 6),
("SANTA BARBARA", 6),
("SANTA CLARA", 6),
("SANTA ELENA", 6),
("SANTA FE", 6),
("SAUZ", 6),
("SIRANDARO", 6),
("TALEGAS", 6),
("TANQUE BLANCO", 6),
("TEPOZANES", 6),
("TOVARES", 6),
("TRES PALMAS", 6),
("VISTA HERMOSA", 6),
("VIZNAGA", 6),
("RINCON DEL CANO", 7),
("SAN ISIDRO", 7);