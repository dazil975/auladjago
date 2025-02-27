from django.db import models

class Categoria(models.Model):
    nome =  models.CharField(verbose_name='Categoria do Produto', blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
    
    def __str__(self):
        return self.nome

class Fornecedores(models.Model):
    nome = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=200)
    contato = models.CharField(verbose_name='Contato', blank=False, null=False, max_length=200)
    cnpj = models.CharField(verbose_name='CNPJ', blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        db_table = 'fornecedor'
    
    def __str__(self):
        return self.nome