from django.shortcuts import render
from django.http import JsonResponse
from .forms import MessageForm, FileUploadForm, ImageUploadForm, VoiceUploadForm
from .models import UploadedFile, UploadedImage, VoiceRecording

def index(request):
    message_form = MessageForm()
    file_form = FileUploadForm()
    image_form = ImageUploadForm()
    voice_form = VoiceUploadForm()
    return render(request, 'index.html', {
        'message_form': message_form,
        'file_form': file_form,
        'image_form': image_form,
        'voice_form': voice_form,
    })

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            # Handle message sending logic here
            return JsonResponse({'status': 'Message sent', 'message': message})
    return JsonResponse({'status': 'Error'}, status=400)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = UploadedFile(file=form.cleaned_data['file'])
            uploaded_file.save()
            return JsonResponse({'status': 'File uploaded'})
    return JsonResponse({'status': 'Error'}, status=400)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = UploadedImage(image=form.cleaned_data['image'])
            uploaded_image.save()
            return JsonResponse({'status': 'Image uploaded'})
    return JsonResponse({'status': 'Error'}, status=400)

def record_voice(request):
    if request.method == 'POST':
        form = VoiceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            voice_recording = VoiceRecording(voice=form.cleaned_data['voice'])
            voice_recording.save()
            return JsonResponse({'status': 'Voice recording uploaded'})
    return JsonResponse({'status': 'Error'}, status=400)
