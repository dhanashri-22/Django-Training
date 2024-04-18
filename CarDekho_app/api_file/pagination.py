from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class Reviewlistpagination(PageNumberPagination):
    page_size = 2
    page_query_param='pa'
    page_size_query_param = 'record'
    max_page_size = 2
    last_page_strings='last'

class Reviewlistlimitoffpage(LimitOffsetPagination):
    default_limit = 3