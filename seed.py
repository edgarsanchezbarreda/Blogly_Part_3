from models import User, Post, Tag, PostTag, db
from app import app

db.drop_all()
db.create_all()

Quentin = User(first_name= 'Quentin', last_name = 'Tarantino', image_url = 'https://www.indiewire.com/wp-content/uploads/2021/06/tarantino.png?resize=800,545')
Barack = User(first_name = 'Barack', last_name = 'Obama', image_url = 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg')
Rock = User(first_name = 'Dwayne', last_name = 'Johnson')



post_1 = Post(title = 'New movie!', content = 'I have a new movie coming, please be on the look out!', user_id = 1)
post_2 = Post(title = 'Hello everyone!', content = 'Hello everyone, I am new to this app please follow!', user_id = 2)
post_3 = Post(title = 'Any good restaurants?', content = 'I am new to this city does anyone know a good taco spot?', user_id = 3)
post_4 = Post(title = 'What a game!', content = "Last night's basketball game was incredible, it came down to the wire!", user_id = 1)
post_5 = Post(title = 'Books to read.', content = 'I am looking for a good book to read, any suggestions?', user_id = 2)
post_6 = Post(title = 'New role!', content = 'I am filming ANOTHER movie with Kevin Hart!', user_id = 3)



tag_1 = Tag(id = 1, name = 'Fun')
tag_2 = Tag(id = 2, name = 'Even More')
tag_3 = Tag(id = 3, name = 'Bloop')



# pt_1 = PostTag(post_id = post_1.id, tag_id = 1)
# pt_2 = PostTag(post_id = post_1.id, tag_id = 2)
# pt_3 = PostTag(post_id = post_1.id, tag_id = 3)
# pt_4 = PostTag(post_id = post_2.id, tag_id = 2)
# pt_5 = PostTag(post_id = post_2.id, tag_id = 3)
# pt_5 = PostTag(post_id = post_3.id, tag_id = 1)
# pt_6 = PostTag(post_id = post_3.id, tag_id = 3)
# pt_7 = PostTag(post_id = post_5.id, tag_id = 1)
# pt_8 = PostTag(post_id = post_5.id, tag_id = 2)
# pt_9 = PostTag(post_id = post_5.id, tag_id = 3)
# pt_10 = PostTag(post_id = post_6.id, tag_id = 2)

db.session.add(Quentin)
db.session.add(Barack)
db.session.add(Rock)
db.session.add(post_1)
db.session.add(post_2)
db.session.add(post_3)
db.session.add(post_4)
db.session.add(post_5)
db.session.add(post_6)
db.session.add(tag_1)
db.session.add(tag_2)
db.session.add(tag_3)
db.session.commit()

# db.session.add(pt_1)
# db.session.add(pt_2)
# db.session.add(pt_3)
# db.session.add(pt_4)
# db.session.add(pt_5)
# db.session.add(pt_6)
# db.session.add(pt_7)
# db.session.add(pt_8)
# db.session.add(pt_9)
# db.session.add(pt_10)
# db.session.add_all([Quentin, Barack, Rock, post_1, post_2, post_3, post_4, post_5, post_6, tag_1, tag_2, tag_3, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7, pt_8, pt_9, pt_10])

# db.session.commit()