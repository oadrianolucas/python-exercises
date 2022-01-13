#04_String_Methodos
#
#
name = 'Adriano'

# O método len() conta a quantidade 
# de caracteres em uma string;
print(len(name))

# O método find() retira o caractere selecionado e realiza
# a contabilidade da string sem o mesmo;
print(name.find('o'))

# O método capitalize() retorna uma string onde o
# primeiro caractere é maiúsculo e o restante é minúsculo;
print(name.capitalize())

# O método upper() retorna uma string onde
# todos os caracteres são maiúsculos;
print(name.upper())

# O método upper() retorna uma string onde
# todos os caracteres são minúsculo;
print(name.lower())

# O método isdigit() retorna True se todos os caracteres
# forem numéricos, caso contrário, False;
print(name.isdigit())