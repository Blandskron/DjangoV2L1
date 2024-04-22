from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Author, Blog, Entry

def manage_data(request):
    if request.method == 'GET':
        # Obtener todos los blogs
        blogs = Blog.objects.all()
        # Construir la respuesta JSON
        data = [{'title': blog.title, 'content': blog.content, 'authors': [author.name for author in blog.authors.all()]} for blog in blogs]
        # Retornar la respuesta JSON
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        # Realizar operaciones de creación o actualización según los parámetros recibidos
        action = request.POST.get('action')
        
        if action == 'create_entry':
            title = request.POST.get('title')
            description = request.POST.get('description')
            author = request.POST.get('author')
            created_at = request.POST.get('created_at')
            Entry.objects.create(title=title, description=description, author=author, created_at=created_at)
        elif action == 'update_entry':
            entry_id = request.POST.get('entry_id')
            try:
                entry = Entry.objects.get(pk=entry_id)
            except Entry.DoesNotExist:
                return JsonResponse({'error': 'Entry does not exist'}, status=404)
            title = request.POST.get('title')
            content = request.POST.get('content')
            author_name = request.POST.get('author')
            entry.title = title
            entry.content = content
            entry.author = author_name
            entry.save()
        elif action == 'create_author':
            name = request.POST.get('name')
            Author.objects.create(name=name)
        elif action == 'create_blog':
            title = request.POST.get('title')
            content = request.POST.get('content')
            Blog.objects.create(title=title, content=content)
        
        return redirect('success_page')  # Redirige a una página de éxito

    return render(request, 'manage_data.html')

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Author.objects.create(name=name)
        return redirect('success_page')  # Redirige a una página de éxito
    return render(request, 'author_form.html')

def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = request.POST.get('author')  # Obtener el ID del autor desde el formulario

        # Verificar si el autor seleccionado existe
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author does not exist'}, status=404)

        # Crear el nuevo blog con el autor correcto
        Blog.objects.create(title=title, content=content, author=author)
        return redirect('success_page')  # Redirige a una página de éxito

    # Si la solicitud no es POST, renderiza el formulario vacío
    return render(request, 'blog_form.html')


def add_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author_id = request.POST.get('author')  # Obtener el ID del autor desde el formulario
        created_at = request.POST.get('created_at')

        # Verificar si el autor seleccionado existe
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author does not exist'}, status=404)

        # Crear la nueva entrada con el autor correcto
        Entry.objects.create(title=title, description=description, author=author, created_at=created_at)
        return redirect('success_page')  # Redirige a una página de éxito

    # Si la solicitud no es POST, renderiza el formulario vacío
    authors = Author.objects.all()
    return render(request, 'entry_form.html', {'authors': authors})

def success_page(request):
    return render(request, 'success.html')
