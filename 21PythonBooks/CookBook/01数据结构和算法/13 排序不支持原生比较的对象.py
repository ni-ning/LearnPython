#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return "User(%s)" % self.user_id

    __repr__ = __str__


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

from operator import attrgetter
# 和 itemgetter类似
print(sorted(users, key=attrgetter('user_id')))

# 同理使用于 max、min
