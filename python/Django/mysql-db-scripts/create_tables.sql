CREATE TABLE t_mysite_user (  
  id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,  
  userId char(36),  
  lastLoginTime timestamp,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
  
-- 插入测试数据  
insert into t_mysite_user(userId) values ('admin'), ('baochen')  ;  
