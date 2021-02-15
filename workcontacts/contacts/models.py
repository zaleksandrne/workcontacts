from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название компании")
    description = models.CharField(max_length=300, verbose_name="Описание")

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    second_name = models.CharField(max_length=200, verbose_name="Фамилия")
    patronymic_name = models.CharField(max_length=200,
                                       verbose_name="Отчество",
                                       blank=True,
                                       null=True
                                       )
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                related_name="employees",
                                verbose_name="Название компании",
                                ) 

    def __str__(self):
        return self.second_name[:15]


class Communication(models.Model):
    name = models.CharField(max_length=200, verbose_name="Вид связи")
    value = models.CharField(max_length=200, verbose_name="Номер")
    employee = models.ForeignKey(Employee,
                                 on_delete=models.CASCADE,
                                 related_name="communications",
                                 blank=True,
                                 null=True,
                                 verbose_name="Сотрудник",
                                 )
