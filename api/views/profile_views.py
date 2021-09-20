from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404


# from ..models.mango import Mango
from ..models.profile import Profile
from ..serializers import ProfileSerializer

# Create your views here.
class NewProfile(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ProfileSerializer
    def get(self, request):
        """Index request"""
        # Get all the profiles:
        # profiles = Profile.objects.all()
        # Filter the profiles by owner, so you can only see your owned profiles
        # profiles = Profile.objects.filter(owner=request.user.id)
        profiles = Profile.objects.all()
        # Run the data through the serializer
        data = ProfileSerializer(profiles, many=True).data
        return Response({'profiles': data})

class Profiles(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ProfileSerializer
    def get(self, request):
        """Index request"""
        # Get all the owned profiles:
        userprofile = Profile.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ProfileSerializer(userprofile, many=True).data
        return Response({'userprofile': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['profile']['owner'] = request.user.id
        # Serialize/create profile
        profile = ProfileSerializer(data=request.data['profile'])
        # If the profile data is valid according to our serializer...
        if profile.is_valid():
            # Save the created profile & send a response
            profile.save()
            return Response({ 'profile': profile.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        profile = get_object_or_404(Profile, pk=pk)
        # Only want to show owned mangos?
        if request.user != profile.owner:
            raise PermissionDenied('Unauthorized, this is not your profile')

        # Run the data through the serializer so it's formatted
        data = ProfileSerializer(profile).data
        return Response({ 'profile': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate profile to delete
        profile = get_object_or_404(Profile, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != profile.owner:
            raise PermissionDenied('Unauthorized, this is not your profile.')
        # Only delete if the user owns the  mango
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Profile
        # get_object_or_404 returns a object representation of our Mango
        profile = get_object_or_404(Profile, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != profile.owner:
            raise PermissionDenied('Unauthorized, this is not your profile.')

        # Ensure the owner field is set to the current user's ID
        request.data['profile']['owner'] = request.user.id
        # Validate updates with serializer
        data = ProfileSerializer(profile, data=request.data['profile'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
