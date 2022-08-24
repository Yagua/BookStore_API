from rest_framework.response import Response
from rest_framework import status
from django.db.models import Model

def get_instance(model, *args, **kwargs):
    """
    Get an instance of the given model.

    return a tuple which contains a boolean that indicates if the model instance
    exists or not, and the result of the query operation, that can be the model
    object itself or an HTTP_404_NOT_FOUND response.
    """

    assert issubclass(model, Model), \
        "The given model is not a django model sub-class."

    instance = model.objects.filter(*args, **kwargs)
    if not instance.exists():
        model_name = model.__name__.lower()
        return (
            False,
            Response({
                "error": f"The specified {model_name} does not exists." },
                status=status.HTTP_404_NOT_FOUND
        ))
    return (True, instance.first())

