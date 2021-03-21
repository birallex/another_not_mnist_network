# another_not_mnist_network
Simple network for handwritten math formula recognition

# Да-да, это ещё одна сетка для распознавания рукописных символов(в том числе математических)

## Описание
Данная СНС позволяет находить на изображении символы и относить их к определённым классам.

В основе сети лежат свёрточные и полносвязанные слои. Классы для распознования можно найти в папке:
    `/dataset/train/` и `/dataset/test`, а также `/dataset/test`

## Результат работы:

Входное изображение:
<p align="center">    
<img src="https://github.com/birallex/another_not_mnist_network/blob/main/test_examples/test_formula.png" width="556" height="344"/>
</p>


Выходное изображение: 
<p align="center">    
<img src="https://github.com/birallex/another_not_mnist_network/blob/main/test_examples/result_of_test_formula.png" width="187" height="18"/>
</p>