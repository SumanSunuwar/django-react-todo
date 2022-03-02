from django.urls import path

from task.views import TaskList, TodoApi, TodoDetail, TaskTodoList, TodoList, TodoCreateApi, DeleteTasksApi

app_name = "task"

urlpatterns = [

    #Url to Create single todo 
    path('todo-create/', TodoCreateApi.as_view(), name="todo-create"),

    #category tasks listing url endpoints
    path('task-list/', TaskList.as_view(), name="task-list"),

    #todos listing url endpoints
    path('todo-list/', TodoList.as_view(), name="todo-list"),

    #todos list under filtered under task id in the endpoint
    path('task-list/<int:task_id>/', TodoApi.as_view(), name="task-todo-list"),

    #Delete multiple tasks url endpoint
    # path('tasks-delete/', DeleteTasksApi, name="tasks-delete"),
    path('tasks-delete/', DeleteTasksApi.as_view(), name="tasks-delete"),



    #Detail for single todo as id passed in the url 
    path('todo-detail/<int:pk>/', TodoDetail.as_view(), name="todo-detail"),
]
