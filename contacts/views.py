from django.shortcuts import render
from .models import Comment
from django.contrib import messages


def addComment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        comment = Comment.objects.create(
            name=name, email=email, subject=subject, message=message)
        comment.save()
        messages.success(request, 'Comment send!')
        return render(request, 'pages/contact.html')
