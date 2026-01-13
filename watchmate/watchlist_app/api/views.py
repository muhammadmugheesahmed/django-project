from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewCreate(generics.CreateAPIView):
   serializer_class=ReviewSerializer
   
   def get_queryset(self):
      return Review.objects.all()
   
   def perform_create(self,serializer):
      
      pk=self.kwargs['pk']
      watchlist=WatchList.objects.get(pk=pk)
      review_user=self.request.user
      review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user)
      if review_queryset.exists():
         raise ValidationError("Your are allowed to review only once")
      
      serializer.save(watchlist=watchlist,review_user=review_user)

class ReviewList(generics.ListCreateAPIView):
   #queryset=Review.objects.all()
   serializer_class=ReviewSerializer
   permission_classes=[IsAuthenticatedOrReadOnly]
   
   def get_queryset(self):
      pk=self.kwargs['pk']
      return Review.objects.filter(watchlist=pk)
   

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes=[IsAuthenticatedOrReadOnly]
   queryset=Review.objects.all()

   serializer_class=ReviewSerializer
   
   
# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#    queryset = Review.objects.all()
#    serializer_class = ReviewSerializer
   
#    def get(self,request, *args, **kwargs):
#       return self.retrieve(request, *args, **kwargs)
   

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#    queryset = Review.objects.all()
#    serializer_class = ReviewSerializer
   
#    def get(self,request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)
   
#    def post(self,request, *args, **kwargs):
#       return self.create(request, *args, **kwargs)
   

############CLASS BASED VIEWS##############
class StreamPlatformAV(APIView):
   def get(self,request):
      streamplatform = StreamPlatform.objects.all()
      serializer = StreamPlatformSerializer(streamplatform, many=True)
      return Response(serializer.data)
      
   def post(self,request):
      serializer = StreamPlatformSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)    
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   

class StreamPlatformDetailAV(APIView):
      def get(self,request,pk):
         try:
             streamplatform = StreamPlatform.objects.get(pk=pk)
         except StreamPlatform.DoesNotExist:
             return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
         serializer = StreamPlatformSerializer(streamplatform)
         return Response(serializer.data)
            
      def put(self,request,pk):
         streamplatform = StreamPlatform.objects.get(pk=pk)
         serializer = StreamPlatformSerializer(streamplatform,data=request.data)
         if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)    
         else:
          return Response(serializer.errors)
      
      def delete(self,request,pk):
         streamplatform = StreamPlatform.objects.get(pk=pk)
         streamplatform.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
      
   


class WatchListAV(APIView):
      def get(self,request):
         watchList = WatchList.objects.all()
         serializer = WatchListSerializer(watchList,many=True)
         return Response(serializer.data)
      
      def post(self,request):
         serializer = WatchListSerializer(data=request.data)
         if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)    
         else:
               return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):
      def get(self,request,pk):
         try:
             watchList = WatchList.objects.get(pk=pk)
         except WatchList.DoesNotExist:
             return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
         serializer = WatchListSerializer(watchList)
         return Response(serializer.data)
            
      def put(self,request,pk):
         watchList = WatchList.objects.get(pk=pk)
         serializer = WatchListSerializer(watchList,data=request.data)
         if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)    
         else:
          return Response(serializer.errors)
      
      def delete(self,request,pk):
         watchList = WatchList.objects.get(pk=pk)
         watchList.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
      
       
############FUNCTION BASED VIEWS##############

# @api_view([ 'GET','POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#      movies = Movie.objects.all()
#      serializer = MovieSerializer(movies,many=True)
#      return Response(serializer.data)
 
#     if request.method == 'POST':
#      serializer = MovieSerializer(data=request.data)
#      if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data,status=status.HTTP_201_CREATED)    
#      else:
#          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
              

# @api_view([ 'GET','PUT','DELETE'])
# def movie_detail(request,pk):
    
#    if request.method == 'GET': 
#       try:
#        movies = Movie.objects.get(pk=pk)
#       except Movie.DoesNotExist:
#        return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#       serializer = MovieSerializer(movies)
#       return Response(serializer.data)
   
#    if request.method == 'PUT': 
#        movies = Movie.objects.get(pk=pk)
#        serializer = MovieSerializer(movies,data=request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)    
#        else:
#           return Response(serializer.errors)
  
#    if request.method == 'DELETE': 
#       movies = Movie.objects.get(pk=pk)
#       movies.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)