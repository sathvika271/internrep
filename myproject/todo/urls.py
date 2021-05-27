from django.urls import path
from . import views

#urlpatterns = [
    #path('', views.index, name='index'),
    #path('add', views.addTodo, name='add'),
    #path('complete/<todo_id>', views.completeTodo, name='complete'),
    #path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    #path('deleteall', views.deleteAll, name='deleteall')
#]
app_name = 'todo'
urlpatterns = [
    path('', views.index, name="Home"),
    path('/addTask', views.addTask, name="Add Task"),
    path('/deleteTask/<int:id>', views.deleteTask, name="Delete Task"),
    path('/completedTask/<int:id>', views.completedTask, name="Task Completed"),
    path('/updateTask/<int:id>', views.updateTask, name="Update Task"),
    path('/deleteAllCompleted', views.deleteAllCompleted, name="Delete all Completed"),
    path('/deleteAll', views.deleteAll, name="Delete All"),
]