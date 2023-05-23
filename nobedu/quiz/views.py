from django.shortcuts import redirect,render
from .forms import *
from .models import QuesModel
from django.views.generic.base import TemplateView
from django.views.generic import ListView

class TestPageView(TemplateView):
    template_name = "pages/testmanager.html"

class TestDetailView(ListView):
    model = QuesModel
    template_name = 'quiz/test1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_questions = self.kwargs['typeq']
        context['questions'] = QuesModel.objects.filter(typeq=type_questions).all()
        return context

def test1(request):
    typeq = '1'
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        #typeq = request.POST.get('n')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            if  (q.typeq) == typeq:
                total+=1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
        percent = score/(total*10) *100
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request,'quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions,
            'typeq': typeq
        }
        return render(request,'quiz/test1.html',context)
def test2(request):
    typeq = '2'
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        #typeq = request.POST.get('n')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            if  (q.typeq) == typeq:
                total+=1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
        percent = score/(total*10) *100
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request,'quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions,
            'typeq': typeq
        }
        return render(request,'quiz/test1.html',context)

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz/addQuestion.html',context)
    else: 
        return redirect('/')