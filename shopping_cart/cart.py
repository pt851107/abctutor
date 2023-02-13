from decimal import Decimal
from django.conf import settings
from summercamp.models import Camp
from lessons.models import Lesson
from activities.models import Activity

class Cart(object):
    
    def __init__(self, request):
    #Initializing Cart
        self.session=request.session
        shopping_cart = self.session.get(settings.CART_SESSION_ID)
        if not shopping_cart:
            shopping_cart = self.session[settings.CART_SESSION_ID]={}
        self.shopping_cart=shopping_cart    
        
    def add(self,camp,quantity=1,override_quantity=False):
        camp_id = str(camp.id)
        if camp_id not in self.shopping_cart:
            self.shopping_cart[camp_id]={'quantity':0, 'fees':str(camp.fees)}
            
        if override_quantity:
            self.shopping_cart[camp_id]['quantity']=quantity
        else:
            self.shopping_cart[camp_id]['quantity'] += quantity 
        self.save() 
    
    def add(self,lesson,quantity=1,override_quantity=False):
        lesson_id = str(lesson.id)
        if lesson_id not in self.shopping_cart:
            self.shopping_cart[lesson_id]={'quantity':0, 'fees':str(lesson.fees)}
            
        if override_quantity:
            self.shopping_cart[lesson_id]['quantity']=quantity
        else:
            self.shopping_cart[lesson_id]['quantity'] += quantity 
        self.save() 
        
    def add(self,activity,quantity=1,override_quantity=False):
        activity_id = str(activity.id)
        if activity_id not in self.shopping_cart:
            self.shopping_cart[activity_id]={'quantity':0, 'fees':str(activity.fees)}
            
        if override_quantity:
            self.shopping_cart[activity_id]['quantity']=quantity
        else:
            self.shopping_cart[activity_id]['quantity'] += quantity 
        self.save()         
        
    def save(self):
        self.session.modified = True 
        
    def remove(self, camp):
        camp_id = str(camp.id)
        if camp_id in self.shopping_cart:
            del self.shopping_cart[camp_id]
            self.save()
            
    def remove(self, lesson):
        lesson_id = str(lesson.id)
        if lesson_id in self.shopping_cart:
            del self.shopping_cart[lesson_id]
            self.save()    
            
    def remove(self, activity):
        activity_id = str(activity.id)
        if activity_id in self.shopping_cart:
            del self.shopping_cart[activity_id]
            self.save()                   
            
    def __iter__(self):
        camp_ids = self.shopping_cart.keys()
        camps = Camp.objects.filter(id__in=camp_ids)
        
        shopping_cart = self.shopping_cart.copy()
        for camp in camps:
            shopping_cart[str(camp.id)]['camp'] = camp
        
        for item in shopping_cart.values():
            item['fees'] = Decimal(item['fees'])
            item['total_fees'] = item['fees'] * item['quantity']
            yield item

    def __iter__(self):
        lesson_ids = self.shopping_cart.keys()
        lessons = Lesson.objects.filter(id__in=lesson_ids)
        
        shopping_cart = self.shopping_cart.copy()
        for lesson in lessons:
            shopping_cart[str(lesson.id)]['lesson'] = lesson
        
        for item in shopping_cart.values():
            item['fees'] = Decimal(item['fees'])
            item['total_fees'] = item['fees'] * item['quantity']
            yield item

    def __iter__(self):
        activity_ids = self.shopping_cart.keys()
        activities = Activity.objects.filter(id__in=activity_ids)
        
        shopping_cart = self.shopping_cart.copy()
        for activity in activities:
            shopping_cart[str(activity.id)]['activity'] = activity
        
        for item in shopping_cart.values():
            item['fees'] = Decimal(item['fees'])
            item['total_fees'] = item['fees'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.shopping_cart.values())
    
    def get_total_fees(self):
        return sum(Decimal(item['fees']* item['quantity']) for item in self.shopping_cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()