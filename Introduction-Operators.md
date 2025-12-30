Os operadores podem ser divididos em **5 categorias diferentes:**

- *Operadores Aritméticos*
- *Operadores de comparação*
- *Operadores de atribuição*
- *Outros operadores booleanos*
- *Operadores Lógicos*

Um operador é como uma função, é encapsulado (junto) tudo dentro de um único caractere ou alguns caracteres.

Por exemplo: um operador de **adição** (*um exemplo de operador aritmético*)

```python
2 + 3
```

Os operadores podem ser escritos como uma função, imaginando por um segundo que o Python não tenha operadores.

Por exemplo: todas as operações deveriam ser feitas como uma função

```python
add(2, 3)

###########

def add(a, b): 
	return a + b
...
add(2, 3)
... 
5
```

# Aridade do operador

Os operadores **exigem** um determinado número de **“operandos”** para funcionar e/ou “operar”.

Por exemplo o operador (”+”) requer **dois elementos** (*2 + 3*)

Esse número de “objetos” necessários determinam a aridade do operador

**Por exemplo:** O operador (”+”) é um operador **binário** (*aridade = **2***)

```python
print(2 + 3) # *Adição*
print(5 + 5) # *Adição*
print(2 * 3) # *Multiplicação*
```

Alguns operadores também serão **unários** (*un-ários, aridade=1*) 

**Por exemplo:** o operador de **subtração** (”-”)

```python
x = 3
-x
```

Também pode ser usado como um operador **binário**:

```python
print(5 - 2)
print(10 - 8)
print(2 - 9)
```
