from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from core.models import Book, Author, Category

@registry.register_document
class BookDocument(Document):
    categories = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
            "time_stamp": fields.DateField()
        }
    )

    authors = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "first_name": fields.TextField(),
            "second_name": fields.TextField(),
            "paternal_last_name": fields.TextField(),
            "maternal_last_name": fields.TextField(),
            "books": fields.NestedField(
                properties={ "pk": fields.IntegerField() }
            ),
            "time_stamp": fields.DateField(),
        }
    )

    class Index:
        name = "book"

    class Django:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "cover",
            "edition",
            "language",
            "page_number",
            "publishier",
            "rating",
            "price",
            "available",
            "time_stamp",
        ]
        related_models = [Category, Author]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Author):
            return related_instance.books.all()
        elif isinstance(related_instance, Category):
            return related_instance.books.all()
