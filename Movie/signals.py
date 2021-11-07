from django.core.mail import send_mail
from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver
from .models import Movie

@receiver(post_save, sender=Movie)
def create_handler(**kwargs):
    instance=kwargs.get('instance')
    send_mail(subject='a new movie has been created',
              message='Dear Users {} has been created'.format(instance.name),
              from_email='sahar.mamdouh93@gmail.com',
              recipient_list=['saharmamdouh246@gmail.com','hassanmahmoud607@gmail.com'],
              fail_silently=False)
    #print("the created movie is {}".format(instance.name))


# @receiver(post_save, sender=Movie)
# def my_handler(sender, instance, created, *args, **kwargs):
#     if created:
# # do_something
#
# send_mail(subject='a new movie has been created', body='Dear Users {} has been created'.format(request.POST.get('name')),
#         sender= 'sahar.mamdouh93@gmail.com',receiver= ['saharmamdouh246@gmail.com','hassanmahmoud607@gmail.com'], fail_silently=False
#                       )