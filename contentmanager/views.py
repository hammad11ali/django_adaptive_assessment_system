from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Area
from .models import Topic
from .models import Concept


class Area_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        Area.objects.create(name=name)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            area_id = request.query_params['id']
            area = Area.objects.filter(id=area_id).values()
        else:
            area = Area.objects.values()
        return Response({'Areas': area})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area = Area.objects.filter(id=id).update(name=name)
        return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Area.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class Topic_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        area_id = request.data['area_id']
        area = Area.objects.filter(id=area_id)[0]
        Topic.objects.create(name=name, area=area)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            area_id = request.query_params['id']
            topics = Topic.objects.filter(area__id=area_id).values()
        else:
            topics = Topic.objects.values()
        return Response({'Topics': topics})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        topic = Topic.objects.filter(
            id=id).update(name=name)
        return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Topic.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class Concept_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        area_id = request.data['area_id']
        topic_id = request.data['topic_id']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(id=topic_id)[0]
        Concept.objects.create(name=name, area=area, topic=topic)
        return Response({'message': 'done'})

    def get(selt, request, format=None):
        if 'area_id' in request.query_params.keys() and 'topic_id' in request.query_params.keys():
            area_id = request.query_params['area_id']
            topic_id = request.query_params['topic_id']
            concepts = Concept.objects.filter(
                area__id=area_id, topic__id=topic_id).values()
            return Response({'Concepts': concepts})
        elif 'area_id' in request.query_params.keys():
            area_id = request.query_params['area_id']
            concepts = Concept.objects.filter(area__id=area_id).values()
            return Response({'Concepts': concepts})
        elif 'topic_id' in request.query_params.keys():
            topic_id = request.query_params['topic_id']
            concepts = Concept.objects.filter(topic__id=topic_id).values()
            return Response({'Concepts': concepts})
        else:
            concepts = Concept.objects.values()
            return Response({'Concepts': concepts})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area_id = request.data['area_id']
        topic_id = request.data['topic_id']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(id=topic_id)[0]
        concept = Concept.objects.filter(
            id=id).update(name=name, area=area, topic=topic)
        return Response({'message': 'done', 'concept': concept})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Concept.objects.get(id=id)
        a.delete()
        return Response({'message': 'Done'})
