from rest_framework.views import APIView
from rest_framework import status

from root.response import GenericResponse


class HelloView(APIView):

	def get(self, request):
		response_data = {'data': 'hello world'}
		return GenericResponse(
			data=response_data,
			status=status.HTTP_200_OK
			)