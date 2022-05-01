from unittest import TestCase
from urllib import response
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

default_img = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'

class UserViewsTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        user = User(first_name = 'Bob', last_name = 'Ross', image_url = 'https://www.bobross.com/content/bob_ross_img.png')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Users</h2>', html)
            self.assertIn('Create a user', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "Test", "last_name": "Person", "image_url": default_img}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test Person", html)
            self.assertEqual(d['image_url'], default_img)

    def test_user_details(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Edit', html)
            self.assertIn('Delete', html)
            self.assertIn('Bob Ross', html)

    def test_delete_user(self):
        test = User(first_name = 'Albert', last_name = 'Einstein', image_url = 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTc5ODc5NjY5ODU0NjQzMzIy/gettyimages-3091504.jpg')
        db.session.add(test)
        db.session.commit()

        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Albert Einstein', html)

            db.session.delete(test)
            db.session.commit()

            resp2 = client.get(f"/{self.user_id}")
            html2 = resp2.get_data(as_text=True)

            self.assertNotIn('Albert Einstein', html2)
            
