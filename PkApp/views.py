
from django.shortcuts import render, get_object_or_404
from .serializers import OrgSerializer, SeqSerializer,OrgSubdomSerializer, AuthSerializer
from .models import Org, Seq, OrgSubdom, Auth
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters


#for Org table
class OrgListCreate(ListCreateAPIView):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer

class OrgRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer

#for Seq table
class SeqListCreate(ListCreateAPIView):
    queryset = Seq.objects.all()
    serializer_class = SeqSerializer

class SeqRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Seq.objects.all()
    serializer_class = SeqSerializer
    lookup_fields = ('org_code', 'seq_num', 'seq_type')  # use for match urls

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object

#for Org_Subdom table
class OrgSubdomListCreate(ListCreateAPIView):
    queryset = OrgSubdom.objects.all()
    serializer_class = OrgSubdomSerializer

class OrgSubdomRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = OrgSubdom.objects.all()
    serializer_class = OrgSubdomSerializer
    lookup_fields = ('org_code', 'org_dom', 'org_subdom')

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)


#for Auth table
class AuthListCreate(ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer

class AuthRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
    lookup_fields = ('org_code', 'org_dom', 'org_subdom', 'org_seq')

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)











# class ListCreateStudent(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class UpdateStudent(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_fields = ('roll', 'branch')
#
#     def get_object(self):
#         queryset = self.get_queryset()  # Get the base queryset
#         queryset = self.filter_queryset(queryset)
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]:  # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         return get_object_or_404(queryset, **filter)  # Lookup the object
#
#
# class ListCreateTeacher(ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#
# class UpdateTeacher(RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
