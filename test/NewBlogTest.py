import unittest

from blog import NewBlog, Session, db_engine
from blog.model import Category, PostStatus, Approval, Author, AuthorStatus, CommentStatus, PostType, TrackbackStatus
from blog.Query import Query


class NewBlogTest(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.queries = Query(self.session)

    def tearDown(self):
        self.session.close()

    @staticmethod
    def execute_sql_file(file):
        buffer = ''
        f = open(file, 'r')
        for line in f:
            buffer += line
        f.close()

        statements = buffer.split(';')
        for statement in statements:
            line = statement.strip()
            if line:
                db_engine.execute(line)

    @staticmethod
    def setUpClass():
        NewBlogTest.execute_sql_file('../db/test_dml.sql')

    @staticmethod
    def tearDownClass():
        NewBlogTest.execute_sql_file('../db/clean_test_dml.sql')

    def test_load_status_singletons(self):
        NewBlog.load_status_singletons()
        self.assertIsNotNone(AuthorStatus.active)
        self.assertIsNotNone(AuthorStatus.deactivated)
        self.assertIsNotNone(AuthorStatus.pending)
        self.assertIsNotNone(Approval.approved)
        self.assertIsNotNone(Approval.pending)
        self.assertIsNotNone(Approval.rejected)
        self.assertIsNotNone(CommentStatus.closed)
        self.assertIsNotNone(CommentStatus.open)
        self.assertIsNotNone(CommentStatus.registered)
        self.assertIsNotNone(PostStatus.delete)
        self.assertIsNotNone(PostStatus.draft)
        self.assertIsNotNone(PostStatus.future)
        self.assertIsNotNone(PostStatus.pending)
        self.assertIsNotNone(PostStatus.publish)
        self.assertIsNotNone(PostType.post)
        self.assertIsNotNone(PostType.revised)
        self.assertIsNotNone(PostType.revision)
        self.assertIsNotNone(TrackbackStatus.closed)
        self.assertIsNotNone(TrackbackStatus.open)
        self.assertIsNotNone(TrackbackStatus.refuse)

    def test_load_categories(self):
        NewBlog.load_categories()
        self.assertIsNotNone(Category.General)

    def test_get_posts(self):
        NewBlog.load_status_singletons()
        posts = NewBlog.get_posts()
        self.assertIsNotNone(posts)
        self.assertEqual(1, len(posts))
