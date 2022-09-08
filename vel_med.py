#se você correr 10 km em 42 min e 42 seg, qual é o seu passo médio em milhas por horas?
km= 10
milhas= 1.609
minutos= 42
segundos= 60
segundos_restantes= 42
milhas_totais= km / milhas
segundos_totais= minutos * segundos + segundos_restantes
horas= segundos_totais/3600
velocidade_media= milhas_totais/horas
print ("a velocidade media sera de {:.2f}".format(velocidade_media),"milhas/h")