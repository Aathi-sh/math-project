from django.shortcuts import render,redirect ,get_object_or_404
from .models import MathPuzzle
from .forms import MathPuzzleForm
from django.core.paginator import Paginator




def puzzle_list(request):
    sort_by = request.GET.get('sort_by','id')
    puzzles =MathPuzzle.objects.all().order_by(sort_by)
    paginator = Paginator(puzzles,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'puzzles':'puzzles'}
    return render(request,'create_puzzles/puzzle_list.html',{'page_obj':page_obj,'sort_by':sort_by})

def puzzle_create(request):
    if request.method =='POST':
        form = MathPuzzleForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('puzzle-list')
    else:
        form = MathPuzzleForm()
    return render(request,'create_puzzles/puzzle_form.html',{'form':form})

def puzzle_update(request,pk):
    puzzle = get_object_or_404(MathPuzzle,pk =pk)
    if request.method =='POST':
        form = MathPuzzleForm(request.POST,instance=puzzle)
        if form.is_valid():
           form.save()
           return redirect('puzzle-list')   
    else:
        form = MathPuzzleForm(instance=puzzle)
        return render(request,'create_puzzles/puzzle_form.html',{'form':form})
    
    
def puzzle_delete(request,pk):
        puzzle = get_object_or_404(MathPuzzle,pk= pk)   
        if request.method =='POST':
            puzzle.delete()
            return redirect('puzzle-list')
        return render(request,'create_puzzles/puzzle_confirm_delete.html',{'puzzle':puzzle})