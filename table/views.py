from django.shortcuts import render

from .models import MyTable
from django.db.models import Q

from django.core.paginator import Paginator

def table_view(request):
    query = request.GET.get('q', '')
    if query:
        results = MyTable.objects.filter(
            Q(primary_gene_symbol__icontains=query) |
            Q(symbol__icontains=query) |
            Q(concept_id__icontains=query) |
            Q(relationship__icontains=query) |
            Q(source__icontains=query)
        )
    else:
        results = MyTable.objects.all()

    paginator = Paginator(results, 10)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'table/db_view.html', {'page_obj': page_obj, 'query': query})
