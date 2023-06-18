<div class="container">
<p> To see this intro in project first clone the project >> run the project <code>python manage.py runserver</code> >> then go to <code>into/</code> URL </p>
    <div class="code">
        To login to the admin URL - <code>admin/</code>:<br>
        Username: talentsumo<br>
        Password: Django@123<br>
    </div>
    <hr>
    <h1>Django REST API Example</h1>
    <p>This is a simple web page that explains the URLs in a Django REST API project. The project allows users to register, login, create, view and share notes with text, video or audio.</p>
    <h2>URLs</h2>
    <p>The project has the following URLs:</p>
    <ul>
        <li><code>reg/</code>: This URL allows users to register by providing a username, email and password. It uses the <code>POST</code> method and returns a JSON response with the user's details or an error message. The view class for this URL is <code>Reg_view</code>.</li>
        <li><code>api/token/</code>: This URL allows users to obtain a pair of JWT access and refresh tokens by providing a username and password. It uses the <code>POST</code> method and returns a JSON response with the tokens or an error message. The view class for this URL is <code>TokenObtainPairView</code>, which is provided by the <code>djangorestframework-simplejwt</code> package.</li>
        <li><code></code>: This URL allows users to view and create notes. It uses the <code>GET</code> method to return a JSON response with a list of all the notes created by the user, and the <code>POST</code> method to create a new note by providing text, video or audio data. The view class for this URL is <code>Notes</code>.</li>
        <li><code>shared/</code>: This URL allows users to view and share notes with other users. It uses the <code>GET</code> method to return a JSON response with a list of all the notes shared by other users to the user, and the <code>POST</code> method to share a note by providing the note id and the username of the recipient. The view class for this URL is <code>Shared</code>.</li>
    </ul>
    <hr>
    <h2>Example Code</h2>
    <p>The following code snippet shows how to define the URLs in the <code>urls.py</code> file:</p>
    <div class="code">
        from django.urls import path <br>
        from rest_framework_simplejwt.views import TokenObtainPairView<br>
        from . import views<br>
        <br>
        urlpatterns = [<br>
            path('reg/', views.Reg_view.as_view(), name="reg"),<br>
            path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),<br>
            path('', views.Notes.as_view(), name="notes"),<br>
            path('shared/', views.Shared.as_view(), name="share"),<br>
        ]<br>
    </div>
</div>
