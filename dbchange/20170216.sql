
ALTER TABLE blog_article ADD COLUMN groupid INTEGER;

CREATE TABLE article_group
(
  id INTEGER ,
  name TEXT,
  distribute TEXT
);

CREATE TABLE group_password
(
  id INTEGER ,
  content TEXT,
  groupid INTEGER
);