from django_elasticsearch_dsl import Document, fields as efilds
from django_elasticsearch_dsl.registries import registry

from core.models import Book, Author, Category

@registry.register_document
class BookDocument(Document):
    categories = efilds.NestedField(
        properties={
            "id": efilds.IntegerField(),
            "name": efilds.TextField(),
            "time_stamp": efilds.DateField()
        }
    )
    authors = efilds.NestedField(
        properties={
            "id": efilds.IntegerField(),
            "first_name": efilds.TextField(),
            "second_name": efilds.TextField(),
            "paternal_last_name": efilds.TextField(),
            "maternal_last_name": efilds.TextField(),
            "country": efilds.TextField(),
            "books": efilds.NestedField(
                properties={ "pk": efilds.IntegerField() }
            ),
            "time_stamp": efilds.DateField(),
        }
    )

    class Index:
        name = "book"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

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
            "available",
            "time_stamp",
        ]
        related_models = [Author, Category]
