from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def addition():
    return {"message":"successfull"}


# # from __future__ import absolute_import, unicode_literals

# from celery import task ,shared_task

# @task()
# def task_number_two():
#     pass


# # # from __future__ import absolute_import, unicode_literals


# @shared_task
# def add(x, y):
#     return x + y


# # @shared_task
# # def mul(x, y):
# #     return x * y


# # @shared_task
# # def xsum(numbers):
# #     return sum(numbers)