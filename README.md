
# NY Times - Most frequent subjects

Uma api em python que consulta artigos do New York Times e captura os assuntos mais frequentes em cada mês de determinado ano.





## Como Funciona?

Basicamente, com uma conta de Developer no site https://developer.nytimes.com/apis, é possível acessar as APIS do NY Times. Porém não existe uma API que retorna assuntos mais frequentes em artigos.

Tendo isso em vista, o script desenvolvido consulta a api "ARCHIVE" do NY Times, onde estão todos os artigos registrados (acredito que todos os que foram digitalizados). Essa api tem uma quantidade enorme de dados, então resolvi filtrar os artigos por mês e ano.

Com os artigos consultados, o programa mapeia os assuntos de cada um, e armazena junto com a quantidade que ele aparece. A saída é algo parecido com:

```code
{
    "2_2024": [
        {
            "amount": 523,
            "subject": "United States Politics and Government"
        },
        {
            "amount": 370,
            "subject": "Presidential Election of 2024"
        },
        ...
}
```

Com isso é possível descobrir o assunto mais comentado de qualquer mês de um determinado ano no New York Times.

Tendo essas informações, também foi desenvolvida uma nuvem de palavras (Wordcloud) utilizando o Streamlit.
## Deploy

Wordcloud no Streamlit
```bash
   https://wordcloud-nytimes.streamlit.app/
```
API hospedada
```bash
  https://pedrocozzati.pythonanywhere.com/subjects?month={mes}&year={ano}&key={sua-chave-nytimes}
```

## Autores

- [@PedroCozzati](https://www.github.com/PedroCozzati)


## Documentação técnica

Para o projeto, foi utilizado: 

- Python

- Flask

- Streamlit








## Documentação da API

#### Retorna os 40 assuntos mais frequentes

```http
  GET /subjects
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `month` | `string` | **Obrigatório**. O Mês que quer consultar |
| `year` | `string` | **Obrigatório**. O Ano que quer consultar |
| `key` | `string` | **Obrigatório**. Sua chave do New York Times, necessário para consumir qualquer API deles |



## Screenshots

Wordcloud no Streamlit:

![image](https://github.com/PedroCozzati/ny-times-subject-by-month/assets/80106385/ee03ec38-be03-4e8d-ba9e-f89d21148634)

Resultado da API:

![image](https://github.com/PedroCozzati/python-engdados/assets/80106385/a08cb0da-f015-4e14-a84e-f060c223afd5)

