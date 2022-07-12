from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from .. import models
from langworld_db_pyramid.maputils.generate_map_icons import generate_map_icons


@view_config(route_name='feature', renderer='langworld_db_pyramid:templates/feature.jinja2')
@view_config(route_name='feature_localized', renderer='langworld_db_pyramid:templates/feature.jinja2')
def view_feature(request):
    try:
        feature = request.dbsession.scalars(
            select(models.Feature).where(models.Feature.man_id == request.matchdict['feature_man_id'])
        ).one()
    except SQLAlchemyError:
        return Response('Database error', content_type='text/plain', status=500)

    values = sorted(
            [value for value in feature.values if value.type.name == 'listed'],
            key=lambda value: len(value.doculects),
            reverse=True
        )

    icon_for_value = {}
    for value, icon_html in zip(values, generate_map_icons()):
        icon_for_value[value] = icon_html

    return {
        'feature_name': getattr(feature, f'name_{request.locale_name}'),
        'man_id': feature.man_id,
        'values': values,
        'icon_for_value': icon_for_value
    }
    # TODO not adding tests yet because I might use React to do entire feature profile
