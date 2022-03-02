from datetime import date
from sre_constants import SUCCESS
from urllib import request
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from task.models import Task, Todo
from .serializers import TaskSerializer, TodoSerializer

# Create your views here.
class TodoApi(APIView):
    def get(self,request,task_id=None):
        if task_id is not None:
            todos = Todo.objects.filter(category=task_id)
        else:
            todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        if len(serializer.data) == 0:
            return Response({"message": "Empty todos"})
        return Response(serializer.data)

class DateFilterTodoApi(APIView):
    def get(self,request,date_filter=None):#wihtout request throws error
        if date_filter is not None:
            DATE_FILTER_EXAMPLE = {
                "TODAY":1,
                "TOMORROW":2,
                "THIS WEEK":6,
                "THIS MONTH":30
            }

            if date_filter in DATE_FILTER_EXAMPLE:
                #get the todos from the Todo model
                # todos = Todo.objects.filter(date__gte or date__lte) 
                pass
            else:
                #return all todos
                todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        if len(serializer.data) == 0:
            return Response({"message": "Empty todos"})
        return Response(serializer.data)

# @api_view(['POST'])
# def DeleteTasksApi(request):
#     """This api function view takes the list of id to delete /
#     multiple todo objects in bulk"""
#     if request.method == "POST":
#         if not request.data:
#             return Response({"error": "Not Found"})
#         else:
#             delete_data = request.data.get('id')
#         if delete_data is None:
#             return Response({"error": "Not found"})
#         elif len(delete_data)  > 0:
#             #get more than one id to delete multiple todo items
#             print(delete_data)
#             Todo.objects.filter(id__in=delete_data.get('id')).delete()
#             return Response({"message": "deleted data"})


class DeleteTasksApi(APIView):
    """This api view takes the list of id to delete /
        multiple todo objects in bulk"""
    def post(self, request, *args, **kwargs):
        
        if not request.data:
            return Response({"error": "Not Found"})
        else:
            delete_data = request.data.get('id')
        if delete_data is None:
            return Response({"error": "Not found"})
        elif len(delete_data)  > 0:
            #get more than one id to delete multiple todo items
            print(delete_data)
            # Todo.objects.filter(id__in=delete_data.get('id')).delete()
            # return Response({"Success": "deleted successfully"})
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class TaskList(generics.ListCreateAPIView):
    '''List of category tasks for todos and
    creating new task category'''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TodoList(generics.ListAPIView):
    '''Class based Api view for Listing the todos'''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCreateApi(generics.CreateAPIView):
    '''Creating new task category'''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TaskTodoList(generics.ListAPIView):
    '''Listing the list of todo filtered from task id'''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_url_kwarg = "taskid"

    def get_queryset(self):
        taskid = self.kwargs.get(self.lookup_url_kwarg)
        todo = Todo.objects.filter(category=taskid)
        return todo

class TodoDetail(generics.RetrieveDestroyAPIView):
    '''Retrieving and deleteing todos with passed pk'''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

