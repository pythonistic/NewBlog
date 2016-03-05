DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS trackback_status;
DROP TABLE IF EXISTS post_type;
DROP TABLE IF EXISTS post_status;
DROP TABLE IF EXISTS comment_status;
DROP TABLE IF EXISTS approval;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS author_status;

CREATE TABLE IF NOT EXISTS `trackback_status` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `status`      VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_trackback_status (status)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `post_type` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `type`        VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_post_type (type)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `post_status` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `status`      VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_post_status (status)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `comment_status` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `status`      VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_comment_status (status)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `approval` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `status`      VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_approval_status (status)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `category` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `name`        VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL DEFAULT '',
  `visible`     INT(1)       NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  INDEX idx_category_name (name)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `author_status` (
  `id`          INT(4)       NOT NULL AUTO_INCREMENT,
  `status`      VARCHAR(20)  NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  INDEX `idx_author_status` (status)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `author` (
  `id`             BIGINT(20)    NOT NULL AUTO_INCREMENT,
  `login`          VARCHAR(128)  NOT NULL,
  `password`       VARCHAR(128)  NOT NULL,
  `email`          VARCHAR(255)  NOT NULL,
  `url`            VARCHAR(255)  NOT NULL,
  `created`        DATETIME      NOT NULL,
  `activation_key` VARCHAR(2048) NOT NULL,
  `status_id`      INT(4)        NOT NULL DEFAULT 2,
  `display_name`   VARCHAR(64)   NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY unq_author_login(login),
  UNIQUE KEY unq_display_name(display_name),
  INDEX idx_author_login (login),
  FOREIGN KEY fk_author_status_id (status_id) REFERENCES author_status (id)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS `post` (
  `id`                  BIGINT(20)   NOT NULL AUTO_INCREMENT,
  `author_id`           BIGINT(20)   NOT NULL,
  `date`                DATETIME     NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified`            DATETIME     NOT NULL DEFAULT '0000-00-00 00:00:00',
  `title`               TEXT         NOT NULL,
  `excerpt`             TEXT         NOT NULL,
  `trackback_excerpt`   TEXT         NOT NULL,
  `content`             LONGTEXT     NOT NULL,
  `content_filtered`    LONGTEXT     NOT NULL,
  `category_id`         INT(4)       NOT NULL DEFAULT 1,
  `post_status_id`      INT(4)       NOT NULL DEFAULT 1,
  `approval_id`         INT(4)       NOT NULL DEFAULT 2,
  `password`            VARCHAR(128) NOT NULL DEFAULT '',
  `post_type_id`        INT(4)       NOT NULL DEFAULT 1,
  `mime_type`           VARCHAR(100) NOT NULL DEFAULT '',
  `latitude`            FLOAT                 DEFAULT NULL,
  `longitude`           FLOAT                 DEFAULT NULL,
  `trackback_status_id` INT(4)       NOT NULL DEFAULT 1,
  `name`                VARCHAR(200) NOT NULL DEFAULT '',
  `comment_status_id`   INT(4)       NOT NULL DEFAULT 1,
  `comment_count`       BIGINT(20)   NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  INDEX `idx_post_status` (`post_status_id`),
  INDEX `idx_post_type_status_date` (`post_type_id`, `post_status_id`, `date`, `id`),
  INDEX `idx_post_author` (`author_id`),
  INDEX `idx_post_name` (`name`(191)),
  FOREIGN KEY `fk_post_author_id` (author_id) REFERENCES author (id),
  FOREIGN KEY `fk_post_category_id` (category_id) REFERENCES category (id),
  FOREIGN KEY `fk_post_post_status_id` (post_status_id) REFERENCES post_status (id),
  FOREIGN KEY `fk_post_approval_id` (approval_id) REFERENCES approval (id),
  FOREIGN KEY `fk_post_type_id` (post_type_id) REFERENCES post_type (id),
  FOREIGN KEY `fk_post_trackback_status_id` (trackback_status_id) REFERENCES trackback_status (id),
  FOREIGN KEY `fk_post_comment_status_id` (comment_status_id) REFERENCES comment_status (id)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 3;

CREATE TABLE IF NOT EXISTS `comment` (
  `id`           BIGINT(20)   NOT NULL AUTO_INCREMENT,
  `parent_id`    BIGINT(20),
  `post_id`      BIGINT(20)   NOT NULL,
  `author`       VARCHAR(255) NOT NULL,
  `author_email` VARCHAR(255) NOT NULL DEFAULT '',
  `author_url`   VARCHAR(255) NOT NULL DEFAULT '',
  `author_IP`    VARCHAR(39)  NOT NULL DEFAULT '',
  `author_id`    BIGINT(20),
  `date`         DATETIME     NOT NULL DEFAULT '0000-00-00 00:00:00',
  `content`      TEXT         NOT NULL,
  `approval_id`  INT(4)       NOT NULL DEFAULT 2,
  `agent`        VARCHAR(255) NOT NULL DEFAULT '',
  `type`         VARCHAR(20)  NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  INDEX `idx_comment_post_ID` (`post_id`),
  INDEX `idx_comment_approved_date` (`approval_id`, `date`),
  INDEX `idx_comment_date` (`date`),
  INDEX `idx_comment_parent` (`parent_id`),
  INDEX `idx_comment_author_email` (`author_email`(10)),
  FOREIGN KEY `fk_comment_parent_id` (parent_id) REFERENCES comment (id),
  FOREIGN KEY `fk_comment_post_id` (post_id) REFERENCES post (id),
  FOREIGN KEY `fk_comment_author_id` (author_id) REFERENCES author (id),
  FOREIGN KEY `fk_comment_approval_id` (approval_id) REFERENCES approval (id)
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8
  AUTO_INCREMENT = 13;


INSERT INTO `trackback_status` (id, status, description) VALUES (1, 'open', 'Accepts trackback pings');
INSERT INTO `trackback_status` (id, status, description) VALUES (2, 'closed', 'Ignores trackback pings');
INSERT INTO `trackback_status` (id, status, description) VALUES (3, 'refuse', 'Refuses trackback pings (404)');

INSERT INTO `post_type` (id, type, description) VALUES (1, 'post', 'An original post');
INSERT INTO `post_type` (id, type, description) VALUES (2, 'revision', 'A child post revising a parent post');
INSERT INTO `post_type` (id, type, description)
VALUES (3, 'revised', 'A parent post revised by a child post and now invisible');

INSERT INTO `post_status` (id, status, description) VALUES (1, 'publish', 'A visible post');
INSERT INTO `post_status` (id, status, description) VALUES (2, 'future', 'A post with a future publication date');
INSERT INTO `post_status` (id, status, description) VALUES (3, 'draft', 'A post not yet visible');
INSERT INTO `post_status` (id, status, description) VALUES (4, 'pending', 'A post awaiting approval');
INSERT INTO `post_status` (id, status, description) VALUES (5, 'delete', 'A deleted post');

INSERT INTO `comment_status` (id, status, description) VALUES (1, 'open', 'Comments permitted');
INSERT INTO `comment_status` (id, status, description)
VALUES (2, 'registered', 'Comments permitted for registered users only');
INSERT INTO `comment_status` (id, status, description) VALUES (3, 'closed', 'Comments not permitted');

INSERT INTO `approval` (id, status, description) VALUES (1, 'pending', 'Pending approval');
INSERT INTO `approval` (id, status, description) VALUES (2, 'approved', 'Approved');
INSERT INTO `approval` (id, status, description) VALUES (3, 'rejected', 'Rejected');

INSERT INTO `category` (id, name, description) VALUES (1, 'General', 'General');

INSERT INTO `author_status` (id, status, description) VALUES (1, 'active', 'Active');
INSERT INTO `author_status` (id, status, description) VALUES (2, 'pending', 'Pending confirmation');
INSERT INTO `author_status` (id, status, description) VALUES (3, 'deactivated', 'Deactivated');

