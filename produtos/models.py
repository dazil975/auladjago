from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome =  models.CharField(verbose_name='Categoria do Produto', blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoriaa'
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=200)
    contato = models.CharField(verbose_name='Contato', blank=False, null=False, max_length=200)
    cnpj = models.CharField(verbose_name='CNPJ', blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        db_table = 'fornecedor'
    
    def __str__(self):
        return (f' {self.nome} - {self.cnpj}')

class Produto(models.Model):
    nome = models.CharField(verbose_name='nome do produto', max_length=50, blank=False, null=False)
    descricao =models.CharField(verbose_name='Descrição do Produto', max_length=200)
    preco =models.DecimalField(verbose_name='Preço', max_digits= 10, decimal_places=2, blank=False, null=False )
    quantidadeEstoque =models.PositiveIntegerField(verbose_name='Quantidade em Estoque', default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True, default='images/placeholder.png')
    marca = models.CharField(max_length=200, null=True, blank=True)
    avaliacao = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    criadoEm = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        db_table = 'produto'

    def __str__(self):
        return self.nome