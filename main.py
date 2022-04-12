from controllers.user_controller import UserController
from dao.jsonrepo import JsonRepository
from dao.repository_base import Repository
from dao.blogger_repository import BloggerRepository
from entity.blog import Blog
from entity.blogger import Blogger
from entity.post import Post
from entity.comment import Comment
from services.login_service import Login
from services.phasher import PassHasher
from services.register_service import RegistrationService
from services.uuidgenerator import UuidGenerator
from entity.blog import Blog
from utils.view_settings import center_resize_window
from tkinter import *

from views.components.anonymous_view import AnonymousFrame
from views.mainview import MainView

if __name__ == '__main__':
    root = Tk()
    center_resize_window(root, 800, 400)
    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0, weight=1)
    hasher = PassHasher()
    idgen = UuidGenerator()
    blogger_repo = BloggerRepository(idgen, 'bloggers_db.json')
    login_service = Login(hasher, blogger_repo)

    reg_service = RegistrationService(blogger_repo, hasher)
    user_controller = UserController(login_service, reg_service)
    #main_view = MainView(root)
    anon_frame = AnonymousFrame(root,user_controller)
    user_controller.view = anon_frame
    root.mainloop()
