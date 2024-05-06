DROP TABLE IF EXISTS node;
DROP TABLE IF EXISTS edge;
CREATE TABLE node(
    id INTEGER,
    description VARCHAR(50)
);
CREATE TABLE edge(
    id INTEGER PRIMARY KEY,
    node1 INTEGER,
    node2 INTEGER
);
INSERT INTO node(id,description) VALUES
(1,'高度不超过几米'),
(2,'在开花和结果后会整个植株枯死'),
(3,'茎部柔软'),
(4,'茎部中空'),
(5,'叶子为长条形或披针形'),
(6,'花为黄色'),
(7,'果实为荚果'),
(8,'植物为攀援植物或灌木'),
(9,'花为白色或粉色'),
(10,'果实为蒴果'),
(11,'叶子为心形或箭头形'),
(12,'叶子为羽状复叶'),
(13,'果实为豆荚状'),
(14,'花为紫色或白色'),
(15,'植物的高度超过2米'),
(16,'草本植物'),
(17,'向日葵'),
(18,'凌霄花'),
(19,'豌豆'),
(20,'紫丁香');
INSERT INTO edge(node1,node2) VALUES
(1,16),
(2,16),
(3,16),
(4,17),
(5,17),
(6,17),
(7,17),
(8,18),
(9,18),
(10,18),
(11,18),
(12,19),
(13,19),
(14,19),
(11,20),
(13,20),
(14,20),
(15,20),
(16,17),
(16,18);