# ass2

---------------------create------------
{
        
        "title": "hello",
        "completed": true
    }

--------------update------------

{
        "id": 1,
        "title": "hello",
        "completed": true
    }

-------------all-urls--------------

{
    "List": "/task-list/",
    "Detail View": "/task-detail/<str:pk>/",
    "Create": "/task-create/",
    "Update": "/task-update/<str:pk>/",
    "Delete": "/task-delete/<str:pk>/"
}