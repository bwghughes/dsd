from fbv.decorators import render_html

@render_html("index.html")
def index_view(request):
    return {"data": 123}

