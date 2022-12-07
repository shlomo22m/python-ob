class SingeltoneClass:

 _instance=None

 def __new__(cls):
     if cls._instance is None:
         print('create')
         cls._instance=super(SingeltoneClass,cls).__new__(cls)
     return cls._instance

