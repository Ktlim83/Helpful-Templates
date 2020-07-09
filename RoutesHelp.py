# from django.urls import path, include
# from django.shortcuts import redirect


# URLS PROJECT FILE

# TO AVOID ISSUES WITH LOADING PAGE ON LOCAL HOST YOU CAN ADD A FUNCTION TO SIMPLY REDIRECT

# def index(request):
#     return redirect('/courses')



# urlpatterns = [
    
#     THEN WITH THE EMPTY PATH IT CALLS YOUR FUNCTION
    
#     path('',index),
    
    
#     path('courses/', include("bootcamp_app.urls")),
# ]


                        
                        
                        
# ROUTING

# IF THE SLASH IS BEFORE IT WILL REPLACE ADDRESS WITH        
# <a href="   /courses/{{ course.id }}/delete">Delete</a>


# IF NO SLASH BEFORE IT WILL APPEND ADDRESS WITH        
# <a href="   courses/{{ course.id }}/delete">Delete</a>
