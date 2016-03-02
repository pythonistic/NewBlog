import unittest

from sqlalchemy.orm import session

from blog import Session

from blog.Model import *


class ModelTest(unittest.TestCase):

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_approval(self):
        ID = -1

        results = self.session.query(Approval).filter(Approval.id == ID).all()
        for result in results:
            self.session.delete(result)
        self.session.commit()

        approval = Approval()
        approval.id = ID
        approval.status = 'foo'
        approval.description = 'description'

        self.session.add(approval)
        self.session.commit()

        loaded_approval = self.session.query(Approval).filter(Approval.id == ID).first()
        self.assertEqual(approval.id, loaded_approval.id)
        self.assertEqual(approval.status, loaded_approval.status)
        self.assertEqual(approval.description, loaded_approval.description)
        self.assertEqual(str(approval), str(loaded_approval))

        self.session.delete(loaded_approval)
        self.session.commit()
