from typing import Any

from pyramid.request import Request
from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from sqlalchemy.sql.expression import Select


def get_all(request: Request, select_: Select) -> list[Any]:
    """Accepts a SQLAlchemy `select()` statement
    (which produces a Select object)
    and a Pyramid request. Returns all results.
    """
    return _get(request, select_).all()


def get_by_man_id(request: Request, model: type, man_id: str) -> Any:
    """Accepts a Pyramid request, mapped class (model) and 'man_id'
    of the required object (e.g. doculect of family). Returns this object.
    """
    # noinspection PyUnresolvedReferences
    return _get_one(request, select(model).where(model.man_id == man_id))


def _get(request: Request, select_: Select) -> ScalarResult:
    """Executes the `select()` statement on `request.dbsession`.

    **Note**: API for Request object does not include `.dbsession`
    attribute, but `models/__init__.py` creates it with
    `config.add_request_method()`.
    """
    return request.dbsession.scalars(select_)


def _get_one(request: Request, select_: Select) -> Any:
    """Accepts a SQLAlchemy `select()` statement
    (which produces a Select object)
    and a Pyramid request. Returns one result.
    """
    # This function will only be used indirectly, via `get_by_man_id`,
    # because searching by man_id is the only situation where there is exactly one object returned.
    return _get(request, select_).one()
