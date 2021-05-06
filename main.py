# import my_module  // if you need to import * from the module use this one.
from my_module import my_age, str_
# import my_package.my_package_module as m
from my_package import my_age as aux_age
# from my_module import * // not recommended
# from my_package.my_package_module import * // not recommended

# print("Hello world!")
print('main name = ', __name__)

print('my_module.my_age', my_age)
print('my_module.str_', str_)
print('my_package.my_package_module.my_age', aux_age)
