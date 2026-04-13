import time
from django.shortcuts import render, redirect
from .models import Message

def home(request):
    error_msg = None
    
    if request.method == 'POST':
        name = request.POST.get('name', 'Anonymous').strip()
        new_message = request.POST.get('message', '').strip()
        
        # 5-Second Cooldown Logic
        last_post_time = request.session.get('last_post_time', 0)
        current_time = time.time()
        
        if current_time - last_post_time < 5:
            error_msg = "Spam protection: Please wait 5 seconds between messages."
        elif new_message:
            Message.objects.create(name=name, content=new_message)
            request.session['last_post_time'] = current_time # Reset timer
            return redirect('home')
            
    # Fetch the latest 30 messages
    messages = Message.objects.all().order_by('-created_at')[:30]
    return render(request, 'board/home.html', {'messages': messages, 'error': error_msg})