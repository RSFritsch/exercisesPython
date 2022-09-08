#  Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
#  O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
#  Qual é o custo total de atacado para 60 cópias?

umLivro= 24.95
descontoDasLivrarias= 0.4
transportePrimeiroExemplar= 3.00
transporteExemplarAdicional= 0.75
numeroTotalDeLivros= 60

valorLivroComDesconto= umLivro * descontoDasLivrarias
precode60livros= valorLivroComDesconto * numeroTotalDeLivros 
custoDoTransporte= transporteExemplarAdicional* 59 + transportePrimeiroExemplar 
custoTotal= precode60livros + custoDoTransporte
print("o valor de atacado total para as 60 copias do livro sera de {:.2f}".format(custoTotal),"reais")