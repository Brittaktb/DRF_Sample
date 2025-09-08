# blog_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from .models import BlogPost, Task
from .serializers import BlogPostSerializer, TaskSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Name the class according to what it's supposed to do
class BlogPostListCreate(APIView):
    # List all Blog Posts
    def get(self, request):
    # Retrieve all posts
        blog_posts = BlogPost.objects.all()

    # Use the serializer to convert the data to JSON
        serializer = BlogPostSerializer(blog_posts, many=True)
        
    # Return a response
        return Response(serializer.data) # JSON

    def post(self, request):
        #Deserialize the incoming data
        serializer = BlogPostSerializer(data=request.data) # works only with model-data
        
        # Validate and save the data if valid
        if serializer.is_valid():
            # save the new post
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Name the class according to the model its working with
class TaskViewSet(ViewSet):
    
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # Declare the queryset as a class attribute
    queryset = Task.objects.all()
        
    # Get the full list of tasks
    def list(self, request):
        # Serialize the objects in the queryset
        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    def retrieve(self, request, pk=None):
        task = get_object_or_404(self.queryset, id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.
                        HTTP_200_OK)