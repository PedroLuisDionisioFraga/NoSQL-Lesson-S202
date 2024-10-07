// 1.a
MATCH (n)
RETURN n

// 1.b
MATCH (g:Game)
WHERE g.ano > 2012
RETURN g

// 1.c
MATCH (g:Game)
WHERE g.genero = 'Terror'
RETURN  g

// 1.d
MATCH (j:Jurado)-[r:JOGOU]->(g:Game)
WHERE r.nota >= 7
RETURN g.titulo, r.nota, j.nome;


// 2.a
CREATE (g:Game {titulo: 'Elden Ring', genero: 'RPG', ano: 2022});
CREATE (g:Game {titulo: 'Animal Crossing: New Horizons', genero: 'Simulação', ano: 2020});
CREATE (g:Game {titulo: 'The Witcher 3: Wild Hunt', genero: 'RPG', ano: 2015});
CREATE (g:Game {titulo: 'Metroid Dread', genero: 'Metroidvania', ano: 2021});

// 2.b
CREATE (j1:Jurado {nome: 'Alice'});
CREATE (j2:Jurado {nome: 'Bruno'});
CREATE (j3:Jurado {nome: 'Carla'});

// 2.c
MATCH (j1:Jurado {nome: 'Alice'}), (g1:Game {titulo: 'Cyberpunk 2077'})
CREATE (j1)-[:JOGOU {nota: 8, horas: 50}]->(g1);

MATCH (j2:Jurado {nome: 'Bruno'}), (g2:Game {titulo: 'Among Us'})
CREATE (j2)-[:JOGOU {nota: 7, horas: 100}]->(g2);

MATCH (j3:Jurado {nome: 'Carla'}), (g3:Game {titulo: 'Valorant'})
CREATE (j3)-[:JOGOU {nota: 9, horas: 300}]->(g3);
