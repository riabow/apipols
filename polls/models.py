from django.db import models
from pprint import pprint

class Question(models.Model):
    title = models.CharField('заголовок',max_length=200)
    descr = models.CharField('описание',max_length=200)
    start_date = models.DateTimeField('дата старта')
    finish_date = models.DateTimeField('дата окончания', null = True, blank=True )
    __original_start_date = None

    def __str__(self):
        return '(%s) %s' % (self.id , self.title)

    def __init__(self, *args, **kwargs):
        super(Question, self).__init__(*args, **kwargs)
        self.__original_start_date = self.start_date

    def save(self, *args, **kwargs):
        print("saveing Question  ........................" )
        pprint(locals())
        #if self.start_date != self.__original_start_date:
        #    self.start_date = self.__original_start_date
        if self.id is not None:
            orig = Question.objects.get(id=self.id)
            if orig.start_date != self.start_date:
                self.start_date = orig.start_date
                #print ("old data", self.start_date )

        super(Question, self).save(*args, **kwargs)



class Option(models.Model):
    title = models.CharField('заголовок', max_length=200)
    def __str__(self):
        return '(%s) %s' % (self.id , self.title)


class MultiOption(models.Model):
    title = models.CharField('заголовок', max_length=200)
    def __str__(self):
        return '(%s) %s' % (self.id , self.title)

class Answer(models.Model):
    question = models.ForeignKey( Question, on_delete=models.DO_NOTHING, verbose_name='вопрос')
    option = models.ForeignKey(Option, on_delete=models.DO_NOTHING, null = True, blank=True , verbose_name='вариант' )
    multioption = models.ManyToManyField(MultiOption, blank=True ,  verbose_name='варианты')
    userid = models.IntegerField( "номер пользователя ",null = True, blank=True  );
    text = models.CharField('текст ответа',max_length=200, null = True, blank=True )

    def __str__(self):
        return '(%s) %s' % (self.id , self.text)




'''
 авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. 
Атрибуты опроса: 
название, 
дата старта, 
дата окончания, 
описание. 
После создания поле "дата старта" у опроса менять нельзя

- добавление/изменение/удаление вопросов в опросе. 
Атрибуты вопросов: 
текст вопроса, 
тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

'''