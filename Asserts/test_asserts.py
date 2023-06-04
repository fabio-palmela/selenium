assert True
num_esperado = 2
num_obtido = 2
#assert num_esperado > num_obtido, f"Esperado {num_esperado} não é maior que o número atual: {num_obtido}."

text_esp = "Selenium"
text_obt = "Selenium w"
# assert text_esp == text_obt, f"Texto não são equivalentes"

assert text_esp in text_obt, f"Esperado {text_esp} dentro da string {text_obt}."
assert text_esp not in text_obt, f"{text_esp} não deveria estar no texto {text_obt}."