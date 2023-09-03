# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.shortcuts import render, redirect
# from django.views import View
#
# class SignUpView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'app_wallet/signup.html', {'form': form})
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'app_wallet/signup.html', {'form': form})