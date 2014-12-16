from django.db.models.query import QuerySet

class Model(object):
    _meta = None
    objects = None

    id = None
    pk = None

    MultipleObjectsReturned = None
    DoesNotExist = None

class Manager(QuerySet):
    pass
