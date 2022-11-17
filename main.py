import io
from aiohttp import web
from db import db_get_list, db_create_extension, db_delete_list, db_create_image
from PIL import Image


routes = web.RouteTableDef()


@routes.get('/list')
async def get_list(request):
    return web.json_response(db_get_list())  


@routes.get('/list/{extension}')
async def get_extension_list(request):
    res = db_get_list(extension=request.match_info['extension'])
    return web.json_response(res)


@routes.post('/list')
async def create_extension_list(request):
    extension = request.rel_url.query.get('extension')
    print(f'Extension {extension}')
    if extension is not None:
        db_create_extension(extension)
        result = {'status': 'success'}
    else:
        result = {'status': 'error'}
    return web.json_response(result)


@routes.delete('/list/{extension}')
async def delete_extension_list(request):
    db_delete_list(request.match_info['extension'])
    result = {'status': 'success'}
    return web.json_response(result)


@routes.post('/image')
async def create_image(request):
    image_name = request.rel_url.query.get('image_name')
    result = {'status': 'error'}
    if image_name:
        post = await request.post()
        image = post.get("image")
        if image: 
            img_content = Image.open(io.BytesIO(image.file.read()))
            extension = img_content.format.lower()
            db_create_image(extension, image_name)
            result = {'status': 'success'}
    return web.json_response(result)


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


main()