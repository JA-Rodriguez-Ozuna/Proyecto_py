'''
List types and Range
'''
#student_grade = list(range(0,11)) #imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(student_grade)


#student_grade1 = list(range(1,9,2)) #imprime: [1, 3, 5, 7] el tercer numero dice de cuanto en cuanto osea va de 2 en 2
#print(student_grade1)

'''
Data Type Attributes
'''
#dir(lo que sea) te muestra todos los atributos o todo lo que puedes hacer con lo que pusiste en el parentesis
#dir(__builtins__) lista completa de funciones que podemos usar
#help(str.upper) te explica que hace esa funcion 
#"hello".upper() #imprime: HELLO en mayuscula
#"hello".title() #imprime: Hello primer letra en mayuscula
#myword = "hello"
#mymord.title() #imprime: HELLO en mayuscula

'''
#modulos en python

#modulos son archivos que contienen funciones y variables que podemos usar en nuestro programa

import sys #importamos el modulo sys
sys.builtin_module_names #imprime: {'_ast', '_bisect', '_codecs', '_collections', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha512', '_signal', '_sitebuiltins', '_socket', '_sqlite3', '_sre', '_stat', '_string', '_struct', '_symtable', 'array', 'binascii'...}
#dir(sys) #imprime: ['__builtins__', '__doc__', '__name__', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'getcheckinterval', 'getdefaultencoding'...]

import time #importamos el modulo time
dir(time) #imprime: ['__builtins__', '__doc__', '__name__', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'gmtime', 'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', 'sleep', 'strptime', 'time', 'timezone', 'tzset']
help(time.sleep) #imprime: sleep(seconds) #Suspends execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.
#time.sleep(5) #hace una pausa de 5 segundos

# modulo os
# import os #importamos el modulo os
# dir(os) #imprime: ['DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOINPUT', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', '_EnvironProxy', '_get_exports_list', '_putenv', '_unsetenv', '__builtins__', '__doc__', '__file__', '__name__', '__spec__', '_exit', '_exitstatus_to_exitcode'...]
# help(os) #imprime: Help on built-in module os:

'''