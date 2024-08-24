from django.db import models
"""
Classe que representa um produto.
Atributos:
- nome: o nome do produto (string)
- preco: o preço do produto (decimal)
- quantidade: a quantidade em estoque do produto (inteiro)
- descricao: a descrição do produto (string)
Métodos:
- __str__: retorna uma representação em string do produto
"""
...
"""
Classe que representa um cliente.
Atributos:
- nome: o nome do cliente (string)
- sobrenome: o sobrenome do cliente (string)
- email: o email do cliente (string)
- telefone: o telefone do cliente (string)
- endereco: o endereço do cliente (string)
Métodos:
- __str__: retorna uma representação em string do cliente
"""
...

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField('Preço',max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.nome} R${self.preco} estoque: {self.quantidade}'

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField('Endereço')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    