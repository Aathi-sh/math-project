from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import crossMath, Difficulty, puzzleLevel




def levels_list(request):
    items = puzzleLevel.objects.all()
    return render(request, 'pages/tables/levelTable1.html', {'items': items})



# Create item

def item_create(request):
    difficulties = Difficulty.objects.all()  # Dynamic difficulty options
    if request.method == 'POST':
        difficulty_value = int(request.POST.get('difficulty'))
        difficulty_obj = get_object_or_404(Difficulty, value=difficulty_value)

        item = crossMath(
            difficulty=difficulty_obj,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            created_by=0,
            updated_by=0,
           
        )
        item.save()
        messages.success(request, "Item created successfully.")
        return redirect("create_puzzles:levels-list")

    return render(request, 'create_puzzles/item_form.html', {
        'is_update': False,
        'difficulties': difficulties
    })
    
    
    # Update item

def item_update(request, pk):
    item = get_object_or_404(crossMath, pk=pk)
    difficulties = Difficulty.objects.all()  # Dynamic difficulty options

    if request.method == 'POST':
        difficulty_value = int(request.POST.get('difficulty'))
        difficulty_obj = get_object_or_404(Difficulty, value=difficulty_value)

        
        item.difficulty = difficulty_obj
        item.updated_at = timezone.now()
        item.updated_by = 0
        item.save()
        messages.success(request, "Item updated successfully.")
        return redirect('create_puzzles:levels-list')

    return render(request, 'create_puzzles/item_form.html', {
        'item': item,
        'is_update': True,
        'difficulties': difficulties
    })
    
    # Confirm delete page

def item_confirm_delete(request, pk):
    item = get_object_or_404(crossMath, pk=pk)
    return render(request, 'create_puzzles/item_confirm_delete.html', {'item': item})


# Delete item

def item_delete(request, pk):
    item = get_object_or_404(crossMath, pk=pk)
    item.delete()
    messages.success(request, "Item deleted successfully.")
    return redirect('create_puzzles:levels-list')

