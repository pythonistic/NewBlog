delete from comment where id < 0;
delete from post where id < 0;
delete from category where id < 0;
delete from author where id < 0;

insert into author values (-101, 'unittest1', 'unittest', 'unittest1@null', 'https://null', now(), 'unittest', (select id from author_status where status='active'), 'Unit Test 1');
insert into author values (-102, 'unittest2', 'unittest', 'unittest2@null', 'https://null', now(), 'unittest', (select id from author_status where status='pending'), 'Unit Test 2');
insert into author values (-103, 'unittest3', 'unittest', 'unittest3@null', 'https://null', now(), 'unittest', (select id from author_status where status='deactivated'), 'Unit Test 3');

insert into category values (-101, 'General', 'General Posts', 1);
insert into category values (-102, 'Special', 'Special Posts', 1);
insert into category values (-103, 'Hidden', 'Hidden Posts', 0);

insert into post values (-101, -101, now(), now(), 'Test Post', 'This is my test post...', 'This is my test post', 'This is my test post. I hope you truly enjoy it. <script>alert("Uh oh")</script>', 'This is my test post. I hope you truly enjoy it.', -101, (select id from post_status where status='publish'), (select id from approval where status='approved'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'http://post1', (select id from comment_status where status='open'), 4);
insert into post values (-102, -101, now(), now(), 'Test Post 2', 'This is my second test post...', 'This is my second test post', 'This is my second test post. I hope you truly enjoy it.', 'This is my second test post. I hope you truly enjoy it.', -101, (select id from post_status where status='publish'), (select id from approval where status='approved'), null, (select id from post_type where type='revised'), 'text/plain', null, null, (select id from trackback_status where status='closed'), 'http://post2', (select id from comment_status where status='closed'), 0);
insert into post values (-103, -101, now(), now(), 'Test Post 3', 'This is my third test post...', 'This is my third test post', 'This is my third test post. I hope you truly enjoy it.', 'This is my third test post. I hope you truly enjoy it.', -101, (select id from post_status where status='publish'), (select id from approval where status='approved'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'http://post3', (select id from comment_status where status='open'), 0);
insert into post values (-104, -101, now(), now(), 'Test Post 4', 'This is my fourth test post...', 'This is my fourth test post', 'This is my fourth test post. I hope you truly enjoy it.', 'This is my fourth test post. I hope you truly enjoy it.', -101, (select id from post_status where status='draft'), (select id from approval where status='approved'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'http://post4', (select id from comment_status where status='open'), 0);
insert into post values (-105, -101, now(), now(), 'Test Post 5', 'This is my fifth test post...', 'This is my fifth test post', 'This is my fifth test post. I hope you truly enjoy it.', 'This is my fifth test post. I hope you truly enjoy it.', -101, (select id from post_status where status='delete'), (select id from approval where status='rejected'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'http://post5', (select id from comment_status where status='open'), 0);
insert into post values (-106, -101, now(), now(), 'Test Post 6', 'This is my sixth test post...', 'This is my sixth test post', 'This is my sixth test post. I hope you truly enjoy it.', 'This is my sixt test post. I hope you truly enjoy it.', -101, (select id from post_status where status='publish'), (select id from approval where status='pending'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'http://post6', (select id from comment_status where status='open'), 0);

insert into comment values (-101, null, -101, 'No One', 'noone@null', '', '::1', null, now(), 'Test comment from a guest', (select id from approval where status = 'approved'), 'Mozilla', 'text/plain');
insert into comment values (-102, null, -101, 'Unit Test 1', 'unittest1@null', 'https://null', '::1', -101, now(), 'Test comment from a registered author', (select id from approval where status = 'approved'), 'Mozilla', 'text/plain');
insert into comment values (-103, null, -101, 'No One', 'noone@null', '', '::1', null, now(), 'Rejected comment from a guest', (select id from approval where status = 'rejected'), 'Mozilla', 'text/plain');
insert into comment values (-104, null, -102, 'No One Also', 'noone@null', '', '::1', null, now(), 'Pending comment from a guest', (select id from approval where status = 'pending'), 'Mozilla', 'text/plain');
insert into comment values (-105, -101, -101, 'Unit Test 2', 'unittest2@null', 'https://null', '::1', -101, now(), 'Test comment from a registered author', (select id from approval where status = 'approved'), 'Mozilla', 'text/plain');
