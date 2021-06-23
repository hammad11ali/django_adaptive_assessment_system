from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Area
from .models import Topic
from .models import Concept
from .models import Course
from .models import Assessment
from .models import ConceptInAssessment
from .models import ConceptInCourse
from .models import AssessmentEnrollment
from .models import AsssessmentPerformance
from .models import CourseEnrollment
from profiles_api.models import UserProfile

from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
        area_id = request.data['area']
        area = Area.objects.filter(id=area_id)[0]
        topic = Topic.objects.filter(name=name)
        if topic.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Topic.objects.create(name=name, area=area)
            return Response({'message': 'done'})

    def get(self, request, format=None):
        contents = []
        if 'id' in request.query_params.keys():
            area_id = request.query_params['id']
            contents = Topic.objects.filter(area__id=area_id).values()
        else:
            topics = Topic.objects.all()
            for topic in topics:
                t = model_to_dict(topic)
                t['area_name'] = topic.area.name
                print(t)
                contents.append(t)

        return Response({'Content': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        area_id = request.data['area']
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
        topic_id = request.data['topic']
        File = request.data['file']

        topic = Topic.objects.filter(id=topic_id)[0]
        concept = Concept.objects.filter(name=name)
        print(File)
        if concept.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            Concept.objects.create(name=name, topic=topic, qgenerator=File)
            return Response({'message': 'done'})

    def get(selt, request, format=None):
        if 'area_id' in request.query_params.keys() and 'topic_id' in request.query_params.keys():
            area_id = request.query_params['area_id']
            topic_id = request.query_params['topic_id']
            concepts = Concept.objects.filter(
                area_id=area_id, topic_id=topic_id).values()
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
                t['filename'] = concept.qgenerator.name
                t['topic_name'] = concept.topic.name
                t['selected'] = False
                contents.append(t)
            return Response({'Content': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        topic_id = request.data['topic']
        File = request.data['file']
        a = Concept.objects.get(id=id)
        oldFile = a.qgenerator
        print('old', oldFile)
        a.delete()
        topic = Topic.objects.filter(id=topic_id)[0]
        concept = Concept.objects.filter(name=name)
        print('file', File)
        if concept.count() > 0:
            return Response({'message': 'Invalid'})
        else:
            if File == 'null':
                File = oldFile
            Concept.objects.create(name=name, topic=topic, qgenerator=File)
            return Response({'message': 'done'})
        return Response({'mesa': 'as'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Concept.objects.get(id=id)
        a.delete()
        return Response({'message': 'Done'})


class Course_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        description = request.data['description']
        Image = request.data['thumbnail']
        concepts_id = request.data['ids']
        course = Course.objects.create(
            name=name, description=description, thumbnail=Image)
        if not concepts_id == '':
            concepts_id = concepts_id.split(',')
            print(concepts_id)
            for concept_id in concepts_id:
                concept = Concept.objects.filter(id=concept_id)[0]
                ConceptInCourse.objects.create(concept=concept, course=course)

        return Response({'message': 'Done'})

    def get(self, request, format=None):
        if 'id' in request.query_params.keys():
            course_id = request.query_params['id']
            course = Course.objects.filter(id=course_id).values()[0]

        else:
            course = Course.objects.values()
        return Response({'Content': course})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        description = request.data['description']
        thumbnail = request.data['thumbnail']
        course = Course.objects.filter(id=id)[0]
        if thumbnail == 'null':
            thumbnail = course.thumbnail
        concepts_id = request.data['ids']
        concepts_id = concepts_id.split(',')
        # course.delete()
        ConceptInCourse.objects.filter(course=course).delete()
        course = Course.objects.filter(id=id).update(
            name=name, description=description, thumbnail=thumbnail)
        course = Course.objects.filter(id=id)[0]
        for concept_id in concepts_id:
            concept = Concept.objects.filter(id=concept_id)[0]
            ConceptInCourse.objects.create(concept=concept, course=course)

        return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Course.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class Quiz_View(APIView):
    def generate(self, concept_id):
        print(concept_id)
        concept = Concept.objects.filter(id=concept_id).values()[0]
        file_ = os.path.basename(concept['qgenerator'])
        filename = os.path.splitext(file_)[0]
        modulename = '..'+filename
        QGenerator = import_module(
            modulename, package='contentmanager.media.Qgenerators.')
        Questions = []
        instance = QGenerator.getInstance()
        for i in range(0, 4):
            # Call Generate Question function
            statement, optionsArray, correct, detail = instance.generateQuestions()
            options = []
            for j in range(0, 4):
                isAnswer = False
                if j == correct:
                    isAnswer = True
                option = {'id': j, 'name': optionsArray[j],
                          'isAnswer': isAnswer, 'selected': False}
                options.append(option)
            Question = {'id': i, 'name': statement,
                        'options': options, 'detail': detail, 'concepts_id': concept_id}
            Questions.append(Question)
        return Questions

    def geerateCourseQuiz(self, course_id):
        concepts = ConceptInCourse.objects.filter(course__id=course_id)
        Questions = []
        for cic in concepts:
            c = cic.concept
            file_ = os.path.basename(c.qgenerator.name)
            filename = os.path.splitext(file_)[0]
            modulename = '..'+filename
            QGenerator = import_module(
                modulename, package='contentmanager.media.Qgenerators.')
            instance = QGenerator.getInstance()
            for i in range(0, 4):
                # Call Generate Question function
                statement, optionsArray, correct, detail = instance.generateQuestions()
                options = []
                for j in range(0, 4):
                    isAnswer = False
                    if j == correct:
                        isAnswer = True
                    option = {'id': j, 'name': optionsArray[j],
                              'isAnswer': isAnswer, 'selected': False}
                    options.append(option)
                Question = {'id': i, 'name': statement,
                            'options': options, 'detail': detail, 'concepts_id': c.id}
                Questions.append(Question)

        return Questions

    def generateAssessmentQuiz(self, aid):
        concepts = ConceptInAssessment.objects.filter(assessment__id=aid)
        Questions = []
        k = 0
        for cic in concepts:
            c = cic.concept
            file_ = os.path.basename(c.qgenerator.name)
            filename = os.path.splitext(file_)[0]
            modulename = '..'+filename
            QGenerator = import_module(
                modulename, package='contentmanager.media.Qgenerators.')
            instance = QGenerator.getInstance()

            for i in range(0, 4):
                # Call Generate Question function
                statement, optionsArray, correct, detail = instance.generateQuestions()
                options = []
                for j in range(0, 4):
                    isAnswer = False
                    if j == correct:
                        isAnswer = True
                    option = {'id': j, 'name': optionsArray[j],
                              'isAnswer': isAnswer, 'selected': False}
                    options.append(option)
                Question = {'id': i + (k*4), 'name': statement,
                            'options': options, 'detail': detail, 'concepts_id': c.id}
                Questions.append(Question)
            k = k+1

        return Questions

    def get(self, request, format=None):
        Content = []
        if 'id' in request.query_params.keys():
            concept_id = request.query_params['id']
            Content = self.generate(concept_id)
        elif "ids" in request.query_params.keys():
            ids = request.query_params['ids']
            ids = ids.split(",")
            allQuestions = []
            i = 0
            for concept_id in ids:
                concept_id = int(concept_id)
                questions = self.generate(concept_id)
                for j in range(0, len(questions)):
                    questions[j]['id'] = questions[j]['id'] + (i*4)
                i = i+1
                allQuestions.extend(questions)
            Content = allQuestions
        elif 'course_id' in request.query_params.keys():
            course_id = request.query_params['course_id']
            Content = self.geerateCourseQuiz(course_id)
        elif 'assessment_id' in request.query_params.keys():
            assessment_id = request.query_params['assessment_id']
            Content = self.generateAssessmentQuiz(assessment_id)

        print(Content)
        return Response({'Content': Content})


class Assessment_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        totalQuestions = request.data['totalQuestions']
        course_id = request.data["course_id"]
        course = Course.objects.filter(id=course_id)[0]
        assessment = Assessment.objects.create(
            name=name, totalQuestions=totalQuestions, course=course)
        return Response({'message': 'Done'})

    def get(self, request, format=None):
        contents = []
        if 'assessment_id' in request.query_params.keys():
            assessment_id = request.query_params["assessment_id"]
            concepts = ConceptInAssessment.objects.filter(
                assessment__id=assessment_id)
            for c in concepts:
                concept = model_to_dict(c)
                concept['name'] = c.concept.name
                contents.append(concept)
        elif 'course_id' in request.query_params.keys():
            course_id = request.query_params["course_id"]
            course = Course.objects.filter(id=course_id)[0]
            assessments = Assessment.objects.filter(course_id=course_id)
            for assessment in assessments:
                t = model_to_dict(assessment)
                t['course_name'] = course.name
                contents.append(t)
        return Response({'Content': contents})

    def put(self, request, format=None):
        name = request.data['name']
        id = request.data['id']
        totalQuestions = request.data['totalQuestions']
        course_id = request.data['course_id']
        course = Course.objects.filter(id=course_id)[0]
        Assessment.objects.filter(id=id).update(
            name=name, totalQuestions=totalQuestions, course=course)
        return Response({'message': 'done'})

    def delete(self, request, format=None):
        id = request.query_params['id']
        a = Assessment.objects.get(id=id)
        a.delete()
        return Response({'message': 'done'})


class ConceptInCourse_View(APIView):
    def get(self, request, format=None):
        contents = []
        if 'id' in request.query_params.keys():
            course_id = request.query_params['id']
            concepts = Concept.objects.all()
            for concept in concepts:
                content = model_to_dict(concept)
                content.pop("qgenerator")
                conceptsincourse = ConceptInCourse.objects.filter(
                    course__id=course_id, concept__id=concept.id)
                if conceptsincourse.count() > 0:
                    content['selected'] = True
                else:
                    content['selected'] = False
                contents.append(content)
        else:
            concepts = Concept.objects.all()
            for concept in concepts:
                # t = model_to_dict(concept)
                t = dict()
                t['id'] = concept.id
                t['name'] = concept.name
                t['topic'] = concept.topic.id
                t['selected'] = False
                contents.append(t)

        return Response({"Content": contents})


class CourseInAssessment(APIView):
    def get(self, request, format=None):
        contents = []
        if 'id' in request.query_params.keys():
            assessment_id = request.query_params['id']
            concepts = Concept.objects.all()
            for concept in concepts:
                content = model_to_dict(concept)
                content.pop("qgenerator")
                conceptsinassessment = ConceptInAssessment.objects.filter(
                    assessment__id=assessment_id, concept__id=concept.id)

        return Response({"Content": contents})


class ConceptInAssessment_View(APIView):
    def post(self, request, format=None):
        assessment_id = request.data['id']
        assessment = Assessment.objects.filter(id=assessment_id)[0]
        print(assessment)
        concepts_ids = request.data['ids']
        print(concepts_ids)
        ConceptInAssessment.objects.filter(
            assessment__id=assessment_id).delete()
        for concept_id in concepts_ids:
            concept = Concept.objects.filter(id=concept_id)[0]
            ConceptInAssessment.objects.create(
                concept=concept, assessment=assessment)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        contents = []
        if 'id' in request.query_params.keys():
            assessment_id = request.query_params['id']
            print(assessment_id)
            concepts = Concept.objects.all()
            assessment = Assessment.objects.filter(id=assessment_id)[0]
            course_id = assessment.course.id
            for concept in concepts:
                content = model_to_dict(concept)
                content.pop("qgenerator")
                conceptsincourse = ConceptInCourse.objects.filter(
                    course__id=course_id, concept__id=concept.id)
                if conceptsincourse.count() > 0:
                    conceptsinassessment = ConceptInAssessment.objects.filter(
                        assessment__id=assessment_id, concept__id=concept.id)
                    if conceptsinassessment.count() > 0:
                        content['selected'] = True
                    else:
                        content['selected'] = False

                    contents.append(content)
        else:
            concepts = Concept.objects.all()
            for concept in concepts:
                # t = model_to_dict(concept)
                t = dict()
                t['id'] = concept.id
                t['name'] = concept.name
                t['topic'] = concept.topic.id
                t['selected'] = False
                contents.append(t)
        return Response({"Content": contents})


class Performance_View(APIView):

    def get(self, request, format=None):
        contents = []
        if 'enrollment' in request.query_params.keys():
            enrollment = request.query_params['enrollment']
            performances = AsssessmentPerformance.objects.filter(
                assessmentEnrollment__id=enrollment)
            assessmentEnrollment = AssessmentEnrollment.objects.filter(
                id=enrollment).values()[0]
            for content in performances:
                newcontent = model_to_dict(content)
                newcontent['concept_name'] = content.concept.name
                newcontent['name'] = content.concept.name
                newcontent['concept_id'] = content.concept.id
                newcontent['active'] = assessmentEnrollment['is_open']
                status = 'weak'
                if content.performance >= 75:
                    status = 'strong'
                elif content.performance >= 50:
                    status = 'average'
                newcontent['status'] = status
                contents.append(newcontent)
            print(enrollment)

        return Response({'Content': contents})

    def put(self, request, format=None):
        performance = request.data['performance']
        enrollment = request.data['enrollment']
        concept_id = request.data['concept_id']
        AsssessmentPerformance.objects.filter(
            assessmentEnrollment__id=enrollment, concept__id=concept_id).update(performance=performance)
        return Response({'message': 'done'})


class AssessmentEnroll_View(APIView):
    def post(self, request, format=None):
        assessmentid = request.data['assessment_id']
        courseid = request.data['course_id']
        assessment = Assessment.objects.filter(id=assessmentid)[0]
        print(request.data)
        courseenrollment = CourseEnrollment.objects.filter(
            course__id=courseid, user__id=request.data['user_id'])[0]
        assessmentEnrollment = AssessmentEnrollment.objects.filter(
            courseEnrollment__id=courseenrollment.id)
        if assessmentEnrollment.count() > 0:
            assessmentEnrollment.update(is_active=False)
        assessmentEnrollment = AssessmentEnrollment.objects.filter(
            courseEnrollment__id=courseenrollment.id, assessment__id=assessmentid)
        is_open = False
        if assessmentEnrollment.count() > 0:
            assessmentEnrollment.delete()
            is_open = True
        assessmentenrollment = AssessmentEnrollment.objects.create(
            courseEnrollment=courseenrollment, assessment=assessment, is_active=True, is_open=is_open)
        results = request.data['array']
        for result in results:
            concept = Concept.objects.filter(id=result['concept_id'])[0]
            performance = result['performance']
            AsssessmentPerformance.objects.create(
                assessmentEnrollment=assessmentenrollment, concept=concept, performance=performance)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        contents = []
        if 'user_id' in request.query_params.keys() and 'course_id' in request.query_params.keys():
            user_id = request.query_params['user_id']
            course_id = request.query_params['course_id']
            allassessments = Assessment.objects.filter(
                course__id=course_id).values()
            ce = CourseEnrollment.objects.filter(
                course__id=course_id, user__id=user_id)[0]
            enrolledassessments = AssessmentEnrollment.objects.filter(
                courseEnrollment__id=ce.id).values()
            return Response({'all': allassessments, 'enrolled': enrolledassessments})
        return Response({'message': 'invalid'})
        # if 'id' in request.query_params.keys():
        #     id = request.query_params['id']
        #     contents = AsssessmentPerformance.objects.filter(
        #         assessmentEnrollment__id=id).values()
        # elif 'userid' in request.query_params.keys():
        # user = UserProfile.objects.filter(
        #     id=request.query_params["user_id"])[0]
        # course_id = request.query_params["course_id"]
        # course = Course.objects.filter(id=course_id)[0]
        # assessments = Assessment.objects.filter(course_id=course_id)
        # courseEnrollment = CourseEnrollment.objects.filter(user__id=user.id)[
        #     0]
        # print(user)
        # print(courseEnrollment)
        # assessmentEnrollment = AssessmentEnrollment.objects.filter(courseEnrollment__id=courseEnrollment.id)[0]
        # print(assessmentEnrollment)

        # performances = AsssessmentPerformance.objects.filter(
        #     assessmentEnrollment__id=assessmentEnrollment.id)
        # for content in performances:
        #     newcontent = model_to_dict(content)
        #     newcontent['concept_name'] = content.concept.name
        #      newcontent['course'] = courseEnrollment.course.id
        #       status = 'weak'
        #        if content.performance >= 75:
        #             status = 'strong'
        #         elif content.performance >= 50:
        #             status = 'average'
        #         newcontent['status'] = status
        #         newcontent['assessmentenrollment'] = assessmentEnrollment.assessment.id
        #         contents.append(newcontent)
        # return Response({'Content': contents})

    def put(self, request, format=None):
        assessment_id = request.data['assessment_id']
        assessmentenrollment = AssessmentEnrollment.objects.filter(
            assessment__id=assessment_id).update(is_active=False)
        return Response({'message': 'done'})

    # def delete(self, request, format=None):
    #     id = request.query_params['id']
    #     a = Topic.objects.get(id=id)
    #     a.delete()
    #     return Response({'message': 'done'})


class CourseEnrollment_View(APIView):
    def post(self, request, format=None):
        course_id = request.data['course_id']
        course = Course.objects.filter(id=course_id)[0]
        user = UserProfile.objects.filter(id=request.data['user_id'])[0]
        ce = CourseEnrollment.objects.filter(
            course__id=course_id, user__id=user.id)
        if ce.count() > 0:
            ce.delete()
        c = CourseEnrollment.objects.create(user=user, course=course)
        return Response({'message': 'done'})

    def get(self, request, format=None):
        user_id = request.query_params['id']
        courseenrollment = CourseEnrollment.objects.filter(
            user__id=user_id).values()
        courses = Course.objects.all().values()
        return Response({'enrollments': courseenrollment, 'courses': courses})


class Progress_View(APIView):
    def get(self, request, format=None):
        contents = []
        if 'user_id' in request.query_params.keys():
            user_id = request.query_params['user_id']
            ce = CourseEnrollment.objects.filter(user__id=user_id).values()
            print(ce)
            for c in ce:
                print(c['id'])
                allassessments = Assessment.objects.filter(
                    course__id=c['course_id']).count()
                ce = CourseEnrollment.objects.filter(
                    course__id=c['course_id'], user__id=user_id)[0]
                enrolledassessments = AssessmentEnrollment.objects.filter(
                    courseEnrollment__id=ce.id).count()
                course = Course.objects.filter(id=c['course_id']).values()[0]
                contents.append({"CourseName": course['name'], "id": c['course_id'],
                                 "total": allassessments, "enrolled": enrolledassessments})
        elif 'user_id' in request.query_params.keys() and 'course_id' in request.query_params.keys():
            user_id = request.query_params['user_id']
            course_id = request.query_params['course_id']
            ce = CourseEnrollment.objects.filter(
                course__id=course_id, user__id=user_id).values()[0]
            # return Response({'a':ce['id']})
            enrolledassessments = AssessmentEnrollment.objects.filter(
                courseEnrollment__id=ce['id'], is_open=True).values()[0]
            enrollment = enrolledassessments['id']
            # assessmentEnrollment = AssessmentEnrollment.objects.filter(
            #     id=enrollment).values()[0]
            performances = AsssessmentPerformance.objects.filter(
                assessmentEnrollment__id=enrollment)

            for content in performances:
                newcontent = model_to_dict(content)
                newcontent['concept_name'] = content.concept.name
                newcontent['concept_id'] = content.concept.id
                contents.append(newcontent)

        print(contents)
        return Response({'Content': contents})
