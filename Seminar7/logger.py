import datetime
import codecs

def info(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'debug: ' + string + '\n')
    file.close()

def debug(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'info: ' + string + '\n')
    file.close()

def warn(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'warn: ' + string + '\n')
    file.close()

def exception(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'debug: ' + string + '\n')
    file.close()

def error(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'error: ' + string + '\n')
    file.close()    

def critical(string):
    file = codecs.open('Seminar7/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'critical: ' + string + '\n')
    file.close()