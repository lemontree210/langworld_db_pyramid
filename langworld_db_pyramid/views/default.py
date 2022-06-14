from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='all_doculects', renderer='langworld_db_pyramid:templates/all_doculects.jinja2')
def view_all_doculects(request):
    try:
        all_doculects = request.dbsession.scalars(select(models.Doculect).order_by(models.Doculect.name_en)).all()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return {'doculects': all_doculects, 'project': 'Languages of the World Database'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
