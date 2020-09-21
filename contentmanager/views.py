from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Area
from .models import Topic
from .models import Concept
from .models import Chapter
import os
from importlib import import_module
from django.forms.models import model_to_dict


class Area_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        area = Area.objects.filter(name=name)
        if area.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Area.objects.create(name=name)
            return Response({'message': 'done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            area_id = request.query_params['id']
            area = Area.objects.filter(id=area_id).values()
        else:
            area = Area.objects.values()
        return Response({'Content': area})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area = Area.objects.filter(name=name)
        if area.count() > 0:
            return Response({'message': 'Invalid'})
        else:
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
        topic = Topic.objects.filter(name=name)
        if topic.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Topic.objects.create(name=name, area=area)
            return Response({'message': 'done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            area_id = request.query_params['id']
            topics = Topic.objects.filter(area__id=area_id).values()
        else:
            topics = Topic.objects.all()
            contents = []
            for topic in topics:
                t = model_to_dict(topic)
                t['area_name'] = topic.area.name
                print(t)
                contents.append(t)

        return Response({'Content': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area_id = request.data['area_id']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(name=name)
        if topic.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            topic = Topic.objects.filter(
                id=id).update(name=name, area=area)
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
        File = request.data['file']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(id=topic_id)[0]
        concept = Concept.objects.filter(name=name)
        if concept.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Concept.objects.create(name=name, area=area,
                                   topic=topic, qgenerator=File)
            return Response({'message': 'done'})

    def get(selt, request, format=None):
        if 'area_id' in request.query_params.keys() and 'topic_id' in request.query_params.keys():
            area_id = request.query_params['area_id']
            topic_id = request.query_params['topic_id']
            concepts = Concept.objects.filter(
                area__id=area_id, topic__id=topic_id).values()
            return Response({'Content': concepts})
        elif 'area_id' in request.query_params.keys():
            area_id = request.query_params['area_id']
            concepts = Concept.objects.filter(area__id=area_id).values()
            return Response({'Content': concepts})
        elif 'topic_id' in request.query_params.keys():
            topic_id = request.query_params['topic_id']
            concepts = Concept.objects.filter(topic__id=topic_id).values()
            return Response({'Content': concepts})
        elif 'concept_id'in request.query_params.keys():
            concept_id = request.query_params['concept_id']
            concept = Concept.objects.filter(id=concept_id)[0]
            return Response({'Content': concept})
        elif 'ids'in request.query_params.keys():
            print(request.query_params['ids'])
            ids = request.query_params['ids']
            for id in ids:
                print(id)
            ids = ids.split(",")[:-1]
            print(ids)
            concepts = []
            for i in ids:
                c = Concept.objects.filter(id=i).values()[0]
                concepts.append(c)
                # add area_name and add Topic_name
            return Response({'Content': concepts})
        else:
            concepts = Concept.objects.all()
            contents = []
            for concept in concepts:
                t = model_to_dict(concept)
                t['area_name'] = concept.area.name
                t['topic_name']=concept.topic.name
                print(t)
                contents.append(t)
            print(concepts)
            return Response({'Content': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area_id = request.data['area_id']
        topic_id = request.data['topic_id']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(id=topic_id)[0]
        concept = Concept.objects.filter(name=name)
        if concept.count() > 0:
            return Response({'message': 'Invalid', })
        else:
            concept = Concept.objects.filter(
                id=id).update(name=name, area=area, topic=topic)
            return Response({'message': 'done', 'concept': concept})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Concept.objects.get(id=id)
        a.delete()
        return Response({'message': 'Done'})


class Course_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        description = request.data['description']
        course = Course.objects.filter(name=name)
        if course.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Course.objects.create(name=name, description=description)
            return Response({'message': 'Done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            course_id = request.query_params['id']
            course = Course.objects.filter(id=area_id).values()
        else:
            course = Course.objects.values()
        return Response({'Course': course})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        description = request.data['description']
        course = Course.objects.filter(name=name)
        if course.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            course = Course.objects.filter(id=id).update(name=name)
            return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Course.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class Chapter_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        description = request.data['description']
        course_id = request.data['course_id']
        course = Course.objects.filter(course_id=id)[0]
        Course.objects.create(
            name=name, description=description, course=course)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            course_id = request.query_params['id']
            chapters = Chapter.objects.filter(course__id=course_id).values()
        else:
            chapters = Chapter.objects.all()
            contents = []
            for chapter in chapters:
                t = model_to_dict(chapter)
                t['area_name'] = chapter.course.name
                print(t)
                contents.append(t)
            print(contents)
        return Response({'Chapter': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        description = request.data['description']
        course_id = request.data['course_id']
        course = Course.objects.filter(id=course_id)[0]
        chapter = Chapter.objects.filter(id=id).update(
            name=name, description=description, course=course)
        return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Chapter.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class Quiz_View(APIView):
    def generate(self, concept_id):
        concept = Concept.objects.filter(id=concept_id).values()[0]
        file_ = os.path.basename(concept['qgenerator'])
        filename = os.path.splitext(file_)[0]
        modulename = '..'+filename
        QGenerator = import_module(
            modulename, package='contentmanager.media.Qgenerators.')
        Questions = []
        instance = QGenerator.getInstance()
        for i in range(0, 10):
            # Call Generate Question function
            statement, optionsArray, correct = instance.generateQuestions()
            options = []
            for j in range(0, 4):
                isAnswer = False
                if j == correct:
                    isAnswer = True
                option = {'id': j, 'name': optionsArray[j],
                          'isAnswer': isAnswer, 'isSelected': False}
                options.append(option)
            Question = {'id': i, 'name': statement,
                        'options': options, 'concepts_id': concept_id}
            Questions.append(Question)
        return Questions

    def get(self, request, format=None):
        Content = []
        if 'id' in request.query_params.keys():
            concept_id = request.query_params['id']
            Content = self.generate(concept_id)
        elif "ids" in request.query_params.keys():
            ids = request.query_params['ids']
            ids = ids.split(",")[:-1]
            allQuestions = []
            for concept_id in ids:
                concept_id = int(concept_id)
                questions = self.generate(concept_id)
                allQuestions.extend(questions)
            Content = allQuestions

        return Response({'Content': Content})
