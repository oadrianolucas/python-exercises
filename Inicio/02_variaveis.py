#02_Variáveis
#
#
# Strings - Variável criada para textos
first_name = 'Adriano'
last_name  = 'Lucas'
full_name = first_name +' '+ last_name

# Integer - Variável criada para número inteiro
birth = 1998
year = 2022

# Float - Variável criada para número não inteiro
height = 174.7

# Bolean - Variável criada para atribuir True ou False
# Traduzindo: Verdadeiro ou Falso
human = True

print('Olá, meu nome é ' + full_name + ', tenho '+ str(year-birth) + ' e '+ str(height) + 'cm de altura.')
print('O '+ full_name + ' é humano?'+ '\n' + str(human))