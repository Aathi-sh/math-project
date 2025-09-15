from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Item


#  List all items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'pages/tables/data.html', {'items': items})


#  Create item
def item_create(request):
    if request.method == 'POST':
        item = Item(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            author=request.POST.get('author') or 'Admin',
            difficulty=request.POST.get('difficulty'),
            row=int(request.POST.get('row') or 0),
            column=int(request.POST.get('column') or 0),
            grid=request.POST.get('grid') or [],
            solution=request.POST.get('solution') or {},
            created_at=timezone.now(),
            updated_at=timezone.now(),
            created_by=0,
            updated_by=0,
            active=True,
        )
        item.save()
        messages.success(request, "Item created successfully.")
        return redirect("create_puzzles:item-list")

    return render(request, 'create_puzzles/item_form.html', {'is_update': False})


#  Update item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.title = request.POST.get('title')
        item.author = request.POST.get('author') or 'Admin'
        item.difficulty = request.POST.get('difficulty')
        item.row = int(request.POST.get('row') or 0)
        item.column = int(request.POST.get('column') or 0)
        item.grid = request.POST.get('grid') or []
        item.solution = request.POST.get('solution') or {}
        item.updated_at = timezone.now()
        item.updated_by = 0
        item.save()
        messages.success(request, "Item updated successfully.")
        return redirect('create_puzzles:item-list')

    return render(request, 'create_puzzles/item_form.html', {'item': item, 'is_update': True})


#  Confirm delete page
def item_confirm_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'create_puzzles/item_confirm_delete.html', {'item': item})


#  Delete item
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    messages.success(request, "Item deleted successfully.")
    return redirect('create_puzzles:item-list')