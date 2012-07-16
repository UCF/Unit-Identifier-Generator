# Create your views here.

def index(request):
    return render_to_response('polls/index.html')