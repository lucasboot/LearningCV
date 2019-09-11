# Detecção de  para controle de apresentações a partir de Suport Vector Machine

## Introdução
A equipe de desenvolvimento é formada por Lucas Figueredo Varela Alves e Luis Felipe Vanin Martins, discentes da disciplina de Tópicos Avançados em Informática I, ministrada pelo docente Orivaldo Vieira de Santana.
&nbsp;
 
O portal Healthline publicou, em 2018, uma matéria a respeito de bactérias presentes em telas sensíveis ao toque ao redor do mundo. Por exemplo, em telas de check-in de aeroportos ou de museus interativos, encontram-se cerca de 253.857 unidades de colônia por área de polegar, elas são originadas, principalmente, da boca, do intestiono e do nariz dos usuários. Dentre os possíveis danos, a bactéria Enterococcus faecalis pode causar desde febre à meningite e infecção urinária. Nesse contexto, faz-se importante dispor de uma alternativa plausível na substituição desses dispotivos em um meio de acesso público.


&nbsp;
A sugestão é, então, uma tecnologia treinada a partir da Support Vector Machine(SVM) com o auxílio da PoseEstimation disponibilizada pelo TensorFlow à guisa de identificar decisões do usuário ao manusear equipamentos desse tipo.



## Metodologia 
No campo do aprendizado de máquina, SVM é um tipo de técnica de aprendizado baseado em classificações supervisionadas calculadas a partir de regressões analíticas. Na prática, esse modelo representa os dados como pontos no espaço que são divididos por uma distância, a qual é a maior possível, no intuito de distinguir tais classes. Além da classificação linear, esse modelo também pode ter resultados satisfatórios em problemas não lineares, a partir do kernel trick, o qual possibilita a aplicação dos métodos em espaços com N dimensões.

No banco de dados para o modelo, faz-se necessário a presença de informações do tipo de coordenadas (x, y) seguidos da classe ao qual pertencem, neste caso, tratando de museus, apresentar e parar a execução da obra. Com esses dados, busca-se um hiperplano, que é uma função de dimensão N, a qual tem a maior distância de um ponto X mais próximo de cada classe.
![](https://miro.medium.com/max/291/1*lSnqrKcgwCcdKcLh9xbqSA.png)

Figura 1: Equação para m dimensões do hiperplano.
Fonte: TowardsDataScience.com
![](https://miro.medium.com/max/781/1*MPnxatC0-O_HhzLWd83bGA.png)
Figura 2: Separação feita pelo hiperplano 2D.
Fonte: TowardsDataScience.com

Neste problema, as informações utilizados são as posições x e y referentes às partes do corpo, como nariz, cotovelo, olhos etc. Elas foram extraídas dos frames de um vídeo que capturou momentos nos quais a pessoa está com um ou dois braços/cotovelos alinhados com o tórax, sendo um o comando de iniciar a apresentação e, dois, o de finalizá-la.


## Códigos 
Uma das etapas mais importantes é a divisão do database em treino e teste, para um total de 84 capturas, utilzou-se uma divisão de 25% para o teste e o restante para treinar o modelo.
```py
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

```
A etapa mais importante do código é a utilização do método fit do objeto referente à biblioteca do modelo utilizado. Com ele, a base de dados é inserida para calcular a equação mais adequada para o hiperespaço.

```py
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)
```
Em seguida, é possível utilizar o método predict para analisar se o modelo está retornando respostas adequadas. Uma alternativa, que é utilizada, é a matrix de confusão, que permite a visualização de dados que foram classificados erroneamente para uma classe ou outra.
```py
y_pred = classifier.predict(X_test)
y_pred2 = classifier.predict(X_train)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm2 = confusion_matrix(y_train, y_pred2)
```


## Experimentos 
A matriz de confusão teve o seguinte retorno:
```py
[[12  0]
 [ 0  9]]

[[42  0]
 [ 0 21]]
```
Com isso, fez-se possível observar que não ocorreu desvio na execução do algoritmo para nenhuma das labels, sendo todas as imagens bem categorizadas.
Em suma, a detecção precisa das partes do corpo pela PoseEstimation retornou uma boa execução do algoritmo de SVM, possibilitando, assim, sua execução para aplicações diversas, como as citadas neste trabalho.