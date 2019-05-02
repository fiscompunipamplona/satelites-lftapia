#TALLER 1 EJERCICIO DEL SATELITE

#Escribir un programa para estimar h (altura)  apartir de un periodo T dado.

G=6.67e-11 #Constante gravitacional
Mt=5.97e24 #Masa de la tierra
Rt=6371e3 #Radio de la tierra
pi=3.1416 
T=float(input("Digite el periodo T (en segundos) :"))
h=(((G*Mt*T**2)/(4*pi**2))**(1/3))-Rt #Ecuacion para calcular la altura dependiente del periodo
h=h*(1e-3)
print("La altura en Km es:",h)

#Altura para un periodo de 90 minutos 
T=5400 #90 minutos = 5400 segundos 
h=(((G*Mt*T**2)/(4*pi**2))**(1/3))-Rt
h=h*(1e-3)
print("La altura para un periodo de 90 minuto en Km  es:",h)

#Altura para un periodo de 45 minutos
T=2700 #45minutos = 2700 segundos
h=(((G*Mt*T**2)/(4*pi**2))**(1/3))-Rt
h=h*(1e-3)
print("La altura para un periodo de 45 minutos en Km es:",h)

#Altura para un dia
T=86400 #24 horas = 86400 segundos
h=(((G*Mt*T**2)/(4*pi**2))**(1/3))-Rt
print("La altura para un dia normal (24 horas) en Km es:",h*(1e-3))

#Diferencia de altura entre un dia normal y un dia sideral
T1=86148
h1=(((G*Mt*T1**2)/(4*pi**2))**(1/3))-Rt
print("La diferencia de alturas entre un dia normal y un sideral en Km es:",(h-h1)*(1e-3))
 
