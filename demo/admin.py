from django.contrib import admin


from demo.models import Message


class MessageAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ('name', 'phone',  'personal_info', 'message_c','publish')

    '''设置过滤选项'''
    list_filter = ('publish', )

    '''每页显示条目数'''
    list_per_page = 20

    '''按日期月份筛选'''
    date_hierarchy = 'publish'

    '''按发布日期排序'''
    ordering = ('-publish',)

admin.site.register(Message,MessageAdmin)
