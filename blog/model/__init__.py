from sqlalchemy.ext.declarative import declarative_base

# required for Models
Base = declarative_base()

from Model import Approval
from Model import Author
from Model import AuthorStatus
from Model import Category
from Model import Comment
from Model import CommentStatus
from Model import Post
from Model import PostStatus
from Model import PostType
from Model import TrackbackStatus
from Model import PostSynopsis