DROP TABLE IF EXISTS node;
DROP TABLE IF EXISTS edge;
CREATE TABLE node(
    id INTEGER PRIMARY KEY,
    description VARCHAR(50),
    ans BOOLEAN
);
CREATE TABLE edge(
    id INTEGER PRIMARY KEY,
    node1 INTEGER,
    node2 INTEGER
);
INSERT INTO node(id,description,ans) VALUES
(1,'高度不超过几米',0),
(2,'在开花和结果后会整个植株枯死',0),
(3,'茎部柔软',0),
(4,'茎部中空',0),
(5,'叶子为长条形或披针形',0),
(6,'花为黄色',0),
(7,'果实为荚果',0),
(8,'植物为攀援植物或灌木',0),
(9,'花为白色或粉色',0),
(10,'果实为蒴果',0),
(11,'叶子为心形或箭头形',0),
(12,'叶子为羽状复叶',0),
(13,'果实为豆荚状',0),
(14,'花为紫色或白色',0),
(15,'植物的高度超过2米',0),
(16,'草本植物',0),
(17,'向日葵',1),
(18,'凌霄花',1),
(19,'豌豆',1),
(20,'紫丁香',1);
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