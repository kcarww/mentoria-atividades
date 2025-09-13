Criar um novo projeto para loja

```
django-admin startproject loja .
```

* Criar um novo app para produtos

```
django-admin startapp produtos
```

* Adicionar o app produtos em INSTALED_APPS

* Incluir a url de produtos no arquivo urls.py do projeto loja

```
path('produtos/' includes('produtos.urls'))
```

* Criar o arquivo urls.py na pasta do app produtos

* Adicionar o path para cadastro de produtos em urls.py do app produtos
```
path('cadastrar/', includes(views.cadastrar))
```


* Criar a função cadastrar no arquivo *views.py*
```
def cadastrar(request):
    return render(request, 'cadastro.html')
```

* Criar a pasta templates no app produtos e criar o arquivo cadastro.html

* Criar o formulário de cadastro


* Repetir os mesmos passos para o app clientes

