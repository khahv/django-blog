from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, MachineTemplate
from .forms import PostForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json, logging

# Create your views here.
# def home(request):
#   return render(request, 'home.html', {})
logger = logging.getLogger('myapp')

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-post_date']
  
class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'

class AddPostView(CreateView): 
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__'

class AddCategoryView(CreateView): 
  model = Category
  # form_class = PostForm
  template_name = 'add_category.html'
  fields = '__all__'
class AddMachineTemplateView(CreateView): 
  model = MachineTemplate
  # form_class = PostForm
  template_name = 'add_machine_template.html'
  fields = '__all__'

class UpdatePostView(UpdateView):
  model = Post
  template_name = 'update_post.html'
  form_class = PostForm
  # fields = ['title', 'body']
class DeletePostView(DeleteView):
  model = Post
  template_name = "delete_post.html"
  success_url = reverse_lazy('home')


@csrf_protect  # Allow POST requests without CSRF token for testing (use CSRF token in production)
def button_action(request):
  if request.method == 'POST':
    try:
      # Parse the JSON payload
      data = json.loads(request.body)
      button_id = data.get('button_id')
      button_data = data.get('button_data')
      # Check if the button_id matches the special value
      if button_id == 'machine-template-id':
        # Perform the backend action
        # Example: Update a database entry or send a notification
        logger.debug("Backend should trigger starting machine with template id: " + str(button_data))
        logger.info("Backend should trigger starting machine with template id: " + str(button_data))
        
        return JsonResponse({'success': True, 'message': 'Special action performed!'})
      elif button_id == 'answer-id':
        #Logic to check the content of answer here:
        #if button_data == 'this is the correct answer':

        logger.debug("Backend should check the answer : " + str(button_data))
        logger.info("Backend should check the answer : " + str(button_data))
        return JsonResponse({'success': True, 'message': 'Special action performed!'})
      else:
        return JsonResponse({'success': False, 'message': 'Invalid button ID'})
    except Exception as e:
      return JsonResponse({'success': False, 'message': str(e)})
  return JsonResponse({'success': False, 'message': 'Invalid request method'})