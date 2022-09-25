    path('search/', views.retrieve_user, name='retrieve-user'),
    path('update/<int:pk>', views.update_user, name='update-user'),
    path('delete/<int:pk>', views.delete_user, name='delete-user'),