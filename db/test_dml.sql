insert into author values (-101, 'unittest1', 'unittest', 'unittest1@null', 'https://null', now(), 'unittest', (select id from author_status where status='active'), display_name='Unit Test 1');
insert into author values (-102, 'unittest2', 'unittest', 'unittest2@null', 'https://null', now(), 'unittest', (select id from author_status where status='pending'), display_name='Unit Test 2');
insert into author values (-103, 'unittest3', 'unittest', 'unittest3@null', 'https://null', now(), 'unittest', (select id from author_status where status='deactivated'), display_name='Unit Test 3');

insert into category values (-101, 'General', 'General Posts', 1);
insert into category values (-102, 'Special', 'Special Posts', 1);
insert into category values (-103, 'Hidden', 'Hidden Posts', 0);

insert into post values (-101, -101, now(), now(), 'Test Post', 'This is my test post...', 'This is my test post', 'This is my test post. I hope you truly enjoy it. <script>alert("Uh oh");</script>', 'This is my test post. I hope you truly enjoy it.', -101, (select id from post_status where status='publish'), (select id from approval where status='approved'), null, (select id from post_type where type='post'), 'text/plain', null, null, (select id from trackback_status where status='open'), 'I don''t know what this is for', (select id from comment_status where status='open'), 1);

