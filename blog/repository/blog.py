from .. import schemas, database,  models
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from PIL import Image, ImageDraw, ImageFont
import qrcode

def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id : int,db : Session ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} is not available')
    return blog

def update_blog(id : int, request : schemas.Blog,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} is not available')
    blog.update(dict(request))
    db.commit()
    return 'Updated'

def delete_blog(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def generate_certificate():
    
    qr_code = qrcode.QRCode(box_size=6)
    qr_code.add_data("https://www.youtube.com/watch?v=bLsJ8HkIjwU")
    qr_code.make()
    qr_image = qr_code.make_image()

    open_image = Image.open("templates/certificate5.png")
    print(open_image.size)
    draw_image = ImageDraw.Draw(open_image)
    open_image.paste(qr_image, (900, 980))
    my_font = ImageFont.truetype('font/Amsterdam.ttf', 240)
    my_font2 = ImageFont.truetype('font/Poppins-Medium.ttf', 40)
    my_font3 = ImageFont.truetype('font/Poppins-Medium.ttf', 40)
    my_font4 = ImageFont.truetype('font/Poppins-Medium.ttf', 35)
    
    
    draw_image.text((1000, 690), "Hansraj Deghun", font=my_font, fill=(69, 69, 69), anchor='mm')
    draw_image.text((570, 1070), "2021-12-12", font=my_font2, fill=(209, 182, 86), anchor='mm')

    
    draw_image.text((1470, 1070), "Laxmikant", font=my_font3, fill=(209, 182, 86), anchor='mm')
    draw_image.text((1470, 1170), "CEO", font=my_font4, fill=(20,20,20), anchor='mm')

    img_reduced_size = open_image.resize((1000, 707))
    img_reduced_size.save("certificates/certificate1.png")