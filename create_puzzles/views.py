from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Item, Difficulty


# List all items (full table)

def item_list(request):
    items = Item.objects.all()
    return render(request, 'pages/tables/data.html', {'items': items})


# Level table view (only numeric difficulty)

def level_item_list(request):
    items = Item.objects.only(
        'id', 'difficulty_id', 'created_at', 'updated_at', 'created_by', 'updated_by', 'active'
    )
    return render(request, 'pages/tables/leveltable.html', {'items': items})


# Create item

def item_create(request):
    difficulties = Difficulty.objects.all()  # Dynamic difficulty options
    if request.method == 'POST':
        difficulty_value = int(request.POST.get('difficulty'))
        difficulty_obj = get_object_or_404(Difficulty, value=difficulty_value)

        item = Item(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            author=request.POST.get('author') or 'Admin',
            difficulty=difficulty_obj,
            row=int(request.POST.get('row') or 0),
            column=int(request.POST.get('column') or 0),
            grid=request.POST.get('grid') or [],
            solution=request.POST.get('solution') or {},
            choices=request.POST.get('choices') or [],
            created_at=timezone.now(),
            updated_at=timezone.now(),
            created_by=0,
            updated_by=0,
            active=True,
        )
        item.save()
        messages.success(request, "Item created successfully.")
        return redirect("create_puzzles:item-list")

    return render(request, 'create_puzzles/item_form.html', {
        'is_update': False,
        'difficulties': difficulties
    })


# Update item

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    difficulties = Difficulty.objects.all()  # Dynamic difficulty options

    if request.method == 'POST':
        difficulty_value = int(request.POST.get('difficulty'))
        difficulty_obj = get_object_or_404(Difficulty, value=difficulty_value)

        item.name = request.POST.get('name')
        item.title = request.POST.get('title')
        item.author = request.POST.get('author') or 'Admin'
        item.difficulty = difficulty_obj
        item.row = int(request.POST.get('row') or 0)
        item.column = int(request.POST.get('column') or 0)
        item.grid = request.POST.get('grid') or []
        item.solution = request.POST.get('solution') or {}
        item.choices = request.POST.get('choices') or []
        item.updated_at = timezone.now()
        item.updated_by = 0
        item.save()
        messages.success(request, "Item updated successfully.")
        return redirect('create_puzzles:item-list')

    return render(request, 'create_puzzles/item_form.html', {
        'item': item,
        'is_update': True,
        'difficulties': difficulties
    })


# Confirm delete page

def item_confirm_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'create_puzzles/item_confirm_delete.html', {'item': item})


# Delete item

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    messages.success(request, "Item deleted successfully.")
    return redirect('create_puzzles:item-list')