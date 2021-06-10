


### SQL에 입력하시면 됩니다.  

## recipe _category 

INSERT INTO recipes_categories(name) values ('국/찌개/전골');
INSERT INTO recipes_categories(name) values ('반찬/김치');
INSERT INTO recipes_categories(name) values ('면류/파스타');
INSERT INTO recipes_categories(name) values ('베이킹');


#요리 -----------------------------------

INSERT INTO recipes(name,category_id,image_url) values ('소시지 야채구이',2,'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Sausage_fry_with_tomato.jpg/640px-Sausage_fry_with_tomato.jpg');

INSERT INTO recipes(name,category_id,image_url) values ('넓은 면두부 파스타',3,'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pasta_dishes_of_Turkey.jpg/640px-Pasta_dishes_of_Turkey.jpg');

INSERT INTO recipes(name,category_id,image_url) values ('슈퍼푸드 블루베리로 만든 머핀',4,'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Vegan_Blueberry_Muffins_%284972870642%29.jpg/640px-Vegan_Blueberry_Muffins_%284972870642%29.jpg');



## main_category -----------------

INSERT INTO ingredients_main_categories(name,created_at) values ('농산물','2000-11-11');
INSERT INTO ingredients_main_categories(name,created_at) values ('축산물','2000-11-11');
INSERT INTO ingredients_main_categories(name,created_at) values ('수산물','2000-11-11');
INSERT INTO ingredients_main_categories(name,created_at) values ('양념/면류','2000-11-11');
INSERT INTO ingredients_main_categories(name,created_at) values ('간식/유제품','2000-11-11');
INSERT INTO ingredients_main_categories(name,created_at) values ('간편식품','2000-11-11');




## sub_category ---------------------------------------------------------------------

INSERT INTO ingredient_sub_categories(name,main_category_id) values ('채소',1);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('버섯류',1);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('돼지고기',2);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('소고기',2);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('계란',2);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('닭고기',2);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('갑각류',3);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('어패류',3);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('생선',3);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('장류',4);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('양념',4);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('오일',4);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('밀가류/면류',4);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('유제품',5);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('간식',5);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('레트로트',6);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('가공식품',6);
INSERT INTO ingredient_sub_categories(name,main_category_id) values ('반찬',6);




## ingredients ---------------------------------------------------------------------


INSERT INTO ingredients(name, price, storage, info, category_id,image_url) values ('비비쿡 처음먹는 까망소시지 (300g)',13000,'냉동','제주 흑돼지와 영양만점 블랙푸드로 만든 건강 소시지',17,'https://upload.wikimedia.org/wikipedia/commons/8/8b/Kielbasa7.jpg');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('파프리카 빨강 1개',2000,'싱싱','아침에 먹기좋은',1,'https://images.unsplash.com/photo-1609869882409-a5274ce68923?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('파프리카 노랑 1개',2000,'싱싱','아침에 먹기좋은',1,'https://images.unsplash.com/photo-1611669306348-24faf153df80?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80');


INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('무농약 양파(800g)',2600,'싱싱','아침에 먹기좋은',1,'https://images.unsplash.com/photo-1580201092675-a0a6a6cafbb1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80');


INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('친환경 양송이버섯 (180g전후)',2600,'싱싱','향이 좋고 쫄깃한 갈색 양송이',2,'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Corner_shop_mushrooms_in_Haringey%2C_London%2C_England.jpg/640px-Corner_shop_mushrooms_in_Haringey%2C_London%2C_England.jpg');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('유기농 먹어봤니 토마토 바질파스타 소스 (709g)',9800,'냉장','유기농 토마토를 사용한',11,'https://images.unsplash.com/photo-1445847562439-f251c3799ea5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=632&q=80');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('유기농 블루베리 (500g,냉동)',10900,'냉동','유기농 농법으로 안전하게 키운 100% 유기농 블루베리',11,'https://images.unsplash.com/photo-1577916082233-f97ed22e4df8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('프레지덩 무염버터 200g(10g*20개)',7500,'냉장',"따로 포장되어 휴대하기 간편하고,보관하기 편한 실용만점 버터!",14,'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/NCI_butter.jpg/2560px-NCI_butter.jpg');

INSERT INTO ingredients(name,price, storage, info, category_id,image_url) values ('우리밀 고소한 백밀가루 (750g)',3900,'실온','고소한 냄새, 쫄깃하고 부드러운 맛!',13,'https://images.unsplash.com/photo-1615227233267-193d25d405f7?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80');


