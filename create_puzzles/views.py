from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone


from .models import Item

def get_superuser():
    """Helper function to get a superuser for created_by and updated_by fields."""
    return User.objects.filter(is_superuser=True).first()

def item_list(request):
    query = request.GET.get('q', '')
    
    # Check if a sort parameter is provided in the URL
    sort_by = request.GET.get('sort_by', 'id') 
    
    # Default to ascending, but check if descending is requested
    order = request.GET.get('order', 'asc')  
    
    if order == 'desc':
        sort_by = '-' + sort_by

    # Filter items based on the search query
    items = Item.objects.filter(
        Q(id__icontains=query) |
        Q(name__icontains=query) |
        Q(title__icontains=query) |
        Q(author__icontains=query) |
        Q(created_by__username__icontains=query) |
        Q(updated_by__username__icontains=query)
    ).order_by(sort_by)

    # Automatically handle pagination
    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'create_puzzles/item_list.html', {
        'page_obj': page_obj,
        'query': query,
        'sort_by': sort_by,
        'order': order,
    })

def item_create(request):
    if request.method == 'POST':
        # Get all form data from the POST request
        name = request.POST.get('name')
        title = request.POST.get('title')
        author = request.POST.get('author')
        difficulty = request.POST.get('difficulty')
        row = request.POST.get('row')
        column = request.POST.get('column')
        grid = request.POST.get('grid')
        solution = request.POST.get('solution')
        active = request.POST.get('active') == 'on'
       
        
        
        if not (row and column and row.isdigit() and column.isdigit()):
            messages.error(request,"Row and column must be numbers between 1 and 20.")
            
            return render(request,'create_puzzles/item_form.html',{'is_update': False})
        row = int(row)
        column = int(column)
        if not (1 <= row <= 20 and 1 <= column <= 20):
            messages.error(request,"Row and column must be numbers between 1 and 20.")
            return render(request,'create_puzzles/item_form.html',{'is_update': False})
        
        # Create a new Item object and save it
        Item.objects.create(
            name=name,
            title=title,
            author=author,
            difficulty=difficulty,
            row=row,
            column=column,
            grid=grid,
            solution=solution,
            active=active,
            
        )
        return redirect('create_puzzles:item-list')
    return render(request, 'create_puzzles/item_form.html', {'is_update': False})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        # Update the item with new data
        item.name = request.POST.get('name')
        item.title = request.POST.get('title')
        item.author = request.POST.get('author')
        item.difficulty = request.POST.get('difficulty')
        item.row = request.POST.get('row')
        item.column = request.POST.get('column')
        item.grid = request.POST.get('grid')
        item.solution = request.POST.get('solution')
        item.active = request.POST.get('active') == 'on'
        
        
        if not (item.row and item.column and str(item.row).isdigit() and str(item.column).isdigit()):
            messages.error(request,"Row and column must be numbers between 1 and 20.")
            return render(request,'create_puzzles/item_form.html',{'item': item, 'is_update': True})
        item.row = int(item.row)
        item.column = int(item.column)
        item.updated_by = get_superuser()
        item.save()
        return redirect('create_puzzles:item-list')
    return render(request, 'create_puzzles/item_form.html', {'item': item, 'is_update': True})

def item_confirm_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'create_puzzles/item_confirm_delete.html', {'item': item})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('create_puzzles:item-list')
    return redirect('create_puzzles:item-list')