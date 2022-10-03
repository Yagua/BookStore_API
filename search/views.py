from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from elasticsearch_dsl import Q

from library.serializers import BookSerializer
from .documents import BookDocument

class SearchBook(GenericAPIView):
    """
    Seach a book in the database using elasticseach
    """

    serializer_class = BookSerializer
    document_class = BookDocument

    def get(self, request):
        try:
            sq = request.query_params.get("query", None)
            query = Q(
                "multi_match",
                query=sq,
                fields = [
                    "title",
                    "description",
                    "edition",
                ],
                fuzziness="auto",
            )

            search = self.document_class.search().query(query)
            response = search.to_queryset()

            serializers = self.serializer_class(response, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)

            # get restult with pagination
            # result = self.paginate_queryset(response)
            # serializers = self.serializer_class(result, many=True)
            # return self.get_paginated_response(serializers.data)

        except Exception as e:
            return Response({
                "message": "Something went wrong during searching process",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
