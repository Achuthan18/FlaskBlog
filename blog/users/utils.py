
import os
import secrets
from PIL import Image
from flask_login import current_user
from flask import url_for, current_app
from flask_mail import Message
from blog import mail


#picture saving function
def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,form_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+form_ext
    picture_path=os.path.join(current_app.root_path,'static/profile_pic',picture_fn)
    
    output_size=(128,128)
    i=Image.open(form_picture)
    i.thumbnail(output_size,Image.ANTIALIAS)

    prev_picture = os.path.join(current_app.root_path, 'static/profile_pic', current_user.image_file)
    if os.path.exists(prev_picture):
        os.remove(prev_picture)

    quality_val=90
    i.save(picture_path,quality=quality_val)

    return picture_fn

#sending email for reset through a function
def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password Request Email',sender='demo@gmail.com',recipients=[user.email])
    msg.body=f''' For resetting your password click the link below
    {url_for('users.reset_token',token=token,_external=True)}

    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)


    