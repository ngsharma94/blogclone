from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('login/', views.Loginview.as_view()),
    path('api/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


# signup@drf.com

# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNDEwMDk3MywiaWF0IjoxNzAzMjM2OTczLCJqdGkiOiI1MDczYmQ2MTI4YzQ0ZmM4OTk2ZGFmOWY2NDJkODBhMiIsInVzZXJfaWQiOjl9.Jf8u--rjdT5t-8fn8oFhcXzkAWUC3i9T7d3qbmtIZ5Y",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNjY4OTczLCJpYXQiOjE3MDMyMzY5NzMsImp0aSI6Ijk2ODI4MmY2YmRiYjQzMWJiZTY2MmQwN2RjNjJmZjQwIiwidXNlcl9pZCI6OX0.wRg1x6aChHZzHXeY2XeNfXm0Sj7nj1a6K0r_YlgL-cE"

# iamadmin@admin.com

# refresh     eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMzI2Njk0OCwiaWF0IjoxNzAyNDAyOTQ4LCJqdGkiOiI0Yjk4NmViZDAxOWE0OTBjOTJmNTZkMTk2MTFlN2Q1MSIsInVzZXJfaWQiOjh9.gydthWXQN91ZZEe2PMtGQPycxjzmy2zj1bv9ZTelTbg
# access      eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyODM0OTQ4LCJpYXQiOjE3MDI0MDI5NDgsImp0aSI6IjQ1ZThkYzY2NmMwOTRmZmViOGEyMDY2YjdkMDBkMjkyIiwidXNlcl9pZCI6OH0.e1Ps2r0HQv6nw1FuIop8edfkZbUQdgcsnef5Cr7Nx7g
