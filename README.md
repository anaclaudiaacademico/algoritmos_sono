# algoritmos_sono
Os experimentos foram realizados com 3 algoritmos.
- **esparso e com sono** - o modelo é criado retirando uma porcentagem dos pesos(epsilon) entre as camadas e entre cada treino outra fração de pesos menos significativos são removidos e outros são adicionados randomicamente.
- **esparso e sem sono** - o modelo é criado retirando uma porcentagem dos pesos(epsilon) entre as camadas mas não são removidos nem adicionados novos pesos entre treinos
- **denso** - rede densa e sem a remoção/adição de pesos entre treinos.

_A rede "densa" e "esparsa sem sono" possuem códigos identicos, inclusive os resultados estão nos mesmo arquivos. O que as difere ´e o fato da rede densa possuir a esparsialidade(epsilon) igual a zero._

### Gráficos
Nesta seção estão os códigos referentes aos gráficos utilizados para a análise dos resultados

### Resultados
Os resultados possuem terminação .out e estão em formatados em csv. Oa experimentos foram separados nos datasets: MNIST[0-4], MNIST[0-9], Fashion-MNIST, CIFAR-10 e CIFAR-100.

Cada arquivo .out possui os campos:

- **experimento** - descrevendo se é esparse com sono o esparse sem sono.
- **alpha** - número de neurônios na camada central do modelo. Importante antentar que para saber o número exato de neurônios nas camadas intermediárias vai depender do dataset. Nas bases MNIST o número total de neurônios nas camadas intermediárias será alpha x 3, nas bases CIFAR será alpha x 9. Exemplo: se no dataset MNIST[0-4] o alpha é 4, ele terá 12 neurônios nas camadas intermediárias, se o experimento foi realizado com alpha = 4 na base CIFAR-10, ele terá 36 neurônios nas camadas intermediárias.
- **epsilon** - porcentagem dos pesos que foram retirados entre as camadas intermediárias.
- **esparso** - este valor foi criado no inicio dos experimentos para validação dos modelos depois se tornou inútil e consta como null nos modelos- 
- **acuracia** - acurácia final do modelo após 1000 épocas.
- **seed** - valor do seed no experimento
- **dataset** - conjunto de dados utilizados no experimento
- **peso** - número total de pesos utilizados no experimento

