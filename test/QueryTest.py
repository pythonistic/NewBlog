import unittest

from blog import Session, db_engine
from blog.Query import *


class QueryTest(unittest.TestCase):

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
        QueryTest.execute_sql_file('../db/test_dml.sql')

    @staticmethod
    def tearDownClass():
        QueryTest.execute_sql_file('../db/clean_test_dml.sql')

    # TODO refactor this to a common location - duplicate code from ModelTest
    def clean(self, clz, remove_id):
        """
        Remove the test record for the model class.

        :param clz:        The test record class.
        :param remove_id:  The id of the record to remove.
        """
        results = self.session.query(clz).filter(clz.id == remove_id).all()
        for result in results:
            self.session.delete(result)
        self.session.commit()

    def test_load_post_with_comments(self):
        """
        Normal blog display
        :return:
        """
        post = self.queries.load_post_with_comments_by_id(-101)
        self.assertIsNotNone(post)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.comment_count, 4)
        self.assertEqual(post.comment_count, len(post.comments))
        self.assertEqual(post, post.comments[0].post)

    def test_load_post_with_comments_failed(self):
        """
        Failed blog display
        :return:
        """
        post = self.queries.load_post_with_comments_by_id(-99)
        self.assertIsNone(post)

    def test_load_post_with_comments_by_permalink(self):
        """
        Blog display from a permalink
        :return:
        """
        post = self.queries.load_post_with_comments_by_permalink('http://post1')
        self.assertIsNotNone(post)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.comment_count, 4)
        self.assertEqual(post.comment_count, len(post.comments))
        self.assertEqual(post, post.comments[0].post)

    def test_load_post_with_comments_by_permalink_failed(self):
        """
        Failed blog display.
        :return:
        """
        post = self.queries.load_post_with_comments_by_permalink('http://post0')
        self.assertIsNone(post)

    def test_load_post_synposis(self):
        """
        Load the post for synopsis display (summary, feed, or main page)
        :return:
        """
        post_synopsis = self.queries.load_post_synopsis_by_id('-101')
        self.assertIsNotNone(post_synopsis)
        self.assertEqual(post_synopsis.title, 'Test Post')

    def test_load_post_synposis_failed(self):
        """
        Load the post for synopsis display (summary, feed, or main page)
        :return:
        """
        post_synopsis = self.queries.load_post_synopsis_by_id('-99')
        self.assertIsNone(post_synopsis)

    def test_load_post_without_comments(self):
        """
        Load the post for editing.
        :return:
        """
        post = self.queries.load_post_by_id('-101')
        self.assertIsNotNone(post)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.comment_count, 4)
        self.assertEqual(0, len(post.comments))

    def test_load_comments(self):
        """
        Load the comments for a separate comment feed
        :return:
        """
        comments = self.queries.load_comments_by_post_id('-101')
        self.assertIsNotNone(comments)
        self.assertTrue(comments)
        self.assertEqual(4, len(comments))

    def test_load_comments_failed(self):
        """
        Load the comments for a separate comment feed
        :return:
        """
        comments = self.queries.load_comments_by_post_id('-99')
        self.assertIsNotNone(comments)
        self.assertFalse(comments)

    def test_get_post_id_for_permalink(self):
        """
        Get the post ID for a given permalink, used for direct linking to the post.
        :return:
        """
        post_id = self.queries.get_post_id_for_permalink('http://post1')
        self.assertIsNotNone(post_id)
        self.assertEqual(-101, post_id)

    def test_get_post_id_for_permalink_failed(self):
        """
        Get the None post ID for a permalink that doesn't exist.
        :return:
        """
        post_id = self.queries.get_post_id_for_permalink('http://post0')
        self.assertIsNone(post_id)

    def test_load_categories_with_posts(self):
        """
        Get the registered categories for the blog (only where posts are present in the category).
        :return:
        """
        categories = self.queries.get_categories_with_posts()
        self.assertIsNotNone(categories)
        self.assertEqual(1, len(categories))
        self.assertEqual('General', categories[0].name)

    def test_load_post_synopsis_for_approval(self):
        """
        Load the post summaries for approval.
        :return:
        """
        summaries = self.queries.load_post_synopsis_for_approval()
        self.assertIsNotNone(summaries)
        self.assertEqual(1, len(summaries))
        self.assertEqual(-106, summaries[0].id)

    def test_load_comment_summaries_for_approval(self):
        """
        Load the comment summaries for approval.
        :return:
        """
        summaries = self.queries.load_comments_for_approval()
        self.assertIsNotNone(summaries)
        self.assertEqual(1, len(summaries))
        self.assertEqual(-104, summaries[0].id)
        self.assertEqual(-102, summaries[0].post_id)

    def test_load_comment(self):
        """
        Load a single comment with children.
        :return:
        """
        comment = self.queries.load_comment_by_id(-101)
        self.assertIsNotNone(comment)
        self.assertEqual(-101, comment.id)
        self.assertEqual(-101, comment.post.id)
        self.assertIsNone(comment.parent_id)
        self.assertIsNotNone(comment.children)
        self.assertEqual(1, len(comment.children))
        self.assertEqual(-105, comment.children[0].id)

    def test_load_authors(self):
        """
        Load the list of authors.
        :return:
        """

    def test_load_approval(self):
        """
        Load the list of approval statuses.
        :return:
        """

    def test_load_author_status(self):
        """
        Load the list of author statuses.
        :return:
        """

    def test_load_category(self):
        """
        Load the list of categories.
        :return:
        """

    def test_load_comment_status(self):
        """
        Load the list of comment statuses.
        :return:
        """

    def test_load_comments_by_status(self):
        """
        Load the comments by a status.
        :return:
        """

    def test_load_posts_by_status(self):
        """
        Load the posts by a status.
        :return:
        """

    def test_load_post_status(self):
        """
        Load the list of post statuses.
        :return:
        """

    def test_load_post_type(self):
        """
        Load the list of post types.
        :return:
        """

    def test_load_posts_by_type(self):
        """
        Load the posts by post type.
        :return:
        """

    def test_load_trackback_status(self):
        """
        Load the list of trackback statuses.
        :return:
        """

