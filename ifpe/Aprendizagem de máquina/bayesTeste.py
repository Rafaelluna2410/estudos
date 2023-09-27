from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
#Esta linha carrega o conjunto de dados Iris e atribui os recursos (X) e os rótulos (y) às variáveis X e y, respectivamente.
# O argumento return_X_y=True é usado para garantir que os dados sejam retornados como matrizes NumPy
X, y = load_iris(return_X_y=True) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
#Argumentos:
# O método fit() geralmente aceita dois argumentos principais:
# x_train: Os dados de entrada (também chamados de características ou atributos) do conjunto de treinamento.
# Esses são os dados que o modelo usará para aprender a fazer previsões.
# y_train: Os rótulos ou saídas esperadas correspondentes aos dados de entrada do conjunto de treinamento.
# Estes são os "rótulos verdadeiros" que o modelo tentará prever após o treinamento.
#fit = Ajuste o classificador Naive Bayes de acordo com X, y. 
#.predict = Executa a classificação em uma matriz de vetores de teste X  e passa o resultado par y_pred
y_pred = gnb.fit(X_train, y_train).predict(X_test) 
print("Number of mislabeled points out of a total %d points : %d"
                     #soma os valoares em que o resultado do y_teste é diferendte do y_pred que recebeu o x_test apos o treinamento do modelo
      % (X_test.shape[0], (y_test != y_pred).sum()))


#referências: 
# https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB
# https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB
# https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html